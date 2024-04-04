import csv
import math
import itertools
from services.file_service import FileService
from services.params_service import (
    get_src_file_name,
    get_dst_file_name,
    get_output_limit,
)

DEFAULT_SRC_FILE_NAME = "source_csv/hitlog.csv"
DEFAULT_DST_FILE_NAME = "top_3_articles.csv"
DEFAULT_OUTPUT_LIMIT_AMOUNT = 3
PAGE_NAME_COLUMN = "page-name"
USER_ID_COLUMN = "user-id"
TIMESTAMP_COLUMN = "timestamp"
PAGE_URL_COLUMN = "page-url"
TOTAL_COLUMN = "total"
REGISTRATION_PAGE_URL = "/register"
INPUT_FIELDS = [PAGE_NAME_COLUMN, PAGE_URL_COLUMN, USER_ID_COLUMN, TIMESTAMP_COLUMN]
OUTPUT_FIELDS = [PAGE_NAME_COLUMN, PAGE_URL_COLUMN, TOTAL_COLUMN]
EXPECTED_HEADER = {
    PAGE_NAME_COLUMN: PAGE_NAME_COLUMN,
    PAGE_URL_COLUMN: PAGE_URL_COLUMN,
    USER_ID_COLUMN: USER_ID_COLUMN,
    TIMESTAMP_COLUMN: TIMESTAMP_COLUMN,
}


def get_counts(article_counts):
    return article_counts[1]


def is_registration_url(page_url):
    return page_url == REGISTRATION_PAGE_URL


def is_article_url(page_url):
    return page_url.startswith("/articles/")


def is_header(row):
    return row == EXPECTED_HEADER


def get_fields(row):
    return (
        row[USER_ID_COLUMN],
        row[PAGE_URL_COLUMN],
        row[TIMESTAMP_COLUMN],
        row[PAGE_NAME_COLUMN],
    )


registered_users = dict()
unique_articles = dict()
unique_users_articles = dict()


def main(src_file_name, dst_file_name, output_limit_amount):
    with open(src_file_name, mode="r") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=INPUT_FIELDS)
        # read input csv row by row
        for row in reader:
            if is_header(row):
                continue
            user_id, page_url, timestamp, page_name = get_fields(row)

            # collect all unique registered users with the registration timestamp
            if is_registration_url(page_url):
                registered_users[user_id] = timestamp

            if is_article_url(page_url):
                # collect all unique articles with their names
                if page_url not in unique_articles:
                    unique_articles[page_url] = page_name

                # collect all unique user-article combinations with the first visit timestamp
                article_url = (user_id, page_url)
                if timestamp < unique_users_articles.get(article_url, str(math.inf)):
                    unique_users_articles[article_url] = timestamp

    article_counts = {}
    for article_url, timestamp in unique_users_articles.items():
        user_id = article_url[0]
        article_url = article_url[1]
        # collect all unique articles with the count of users registered after visit
        if user_id in registered_users and timestamp < registered_users[user_id]:
            article_counts[article_url] = article_counts.get(article_url, 0) + 1

    # sort articles by number of registered users
    article_counts = dict(sorted(article_counts.items(), key=get_counts, reverse=True))
    final_content = []

    # extract top articles only
    top_articles = itertools.islice(article_counts.items(), output_limit_amount)
    for article_url, count in top_articles:
        final_content.append([unique_articles[article_url], article_url, count])

    # write the output to a csv file
    FileService.write_content(dst_file_name, OUTPUT_FIELDS, final_content)


if __name__ == "__main__":
    src_file_name = get_src_file_name(DEFAULT_SRC_FILE_NAME)
    dst_file_name = get_dst_file_name(DEFAULT_DST_FILE_NAME)
    output_limit_amount = get_output_limit(DEFAULT_OUTPUT_LIMIT_AMOUNT)
    print(
        f'Source file = "{src_file_name}", Destination file = "{dst_file_name}", Output limit = {output_limit_amount}'
    )
    main(src_file_name, dst_file_name, output_limit_amount)
    print(
        f'Processing of "{src_file_name}" done, top articles stored to "{dst_file_name}".'
    )
