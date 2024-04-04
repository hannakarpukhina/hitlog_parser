import pytest
import os
from extract_top_articles import (
    get_counts,
    is_registration_url,
    is_article_url,
    is_header,
    EXPECTED_HEADER,
    get_fields,
)
from extract_top_articles import main
from services.params_service import (
    get_src_file_name,
    get_dst_file_name,
    get_output_limit,
    get_param_by_index,
)


@pytest.fixture(scope="module")
def get_test_counts():
    return get_counts(("/test_url", 50))


@pytest.fixture(scope="module")
def test_registration_url():
    return is_registration_url("/register")


@pytest.fixture(scope="module")
def test_not_registration_url():
    return is_registration_url("/test_url/")


@pytest.fixture(scope="module")
def test_article_url():
    return is_article_url("/articles/some_test")


@pytest.fixture(scope="module")
def test_not_article_url():
    return is_article_url("/test_url/")


@pytest.fixture(scope="module")
def test_header():
    return is_header(EXPECTED_HEADER)


@pytest.fixture(scope="module")
def test_get_fields():
    return get_fields(EXPECTED_HEADER)


@pytest.fixture(scope="module")
def test_param_src_file_name():
    return get_src_file_name("/static/test_input.csv")


@pytest.fixture(scope="module")
def test_param_dst_file_name():
    return get_dst_file_name("/static/test_output.csv")


@pytest.fixture(scope="module")
def test_param_output_limit():
    return get_output_limit(3)


@pytest.fixture(scope="module")
def test_param_by_index():
    return get_param_by_index(1, "/static/test_input.csv")


@pytest.fixture(scope="module")
def test_top_articles():
    input_file = "tests/static/test_input.csv"
    output_file = "tests/static/test_output.csv"
    if os.path.exists(output_file):
        os.remove(output_file)
    main(input_file, output_file, 3)
