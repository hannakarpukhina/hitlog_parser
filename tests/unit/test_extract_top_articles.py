def test_get_counts(get_test_counts):
    """
    GIVEN url and hits count tuple
    WHEN get_counts is called
    THEN valid count value is returned
    """
    assert get_test_counts == 50


def test_is_registration_url(test_registration_url):
    """
    GIVEN a registration url
    WHEN is_registration_url is called
    THEN True is returned
    """
    assert test_registration_url == True


def test_is_registration_url_negative(test_not_registration_url):
    """
    GIVEN not a registration url
    WHEN is_registration_url is called
    THEN False is returned
    """
    assert test_not_registration_url == False


def test_is_article_url(test_article_url):
    """
    GIVEN an article url
    WHEN is_article_url is called
    THEN True is returned
    """
    assert test_article_url == True


def test_is_article_url_negative(test_not_article_url):
    """
    GIVEN not an article url
    WHEN is_article_url is called
    THEN False is returned
    """
    assert test_not_article_url == False


def test_is_header(test_header):
    """
    GIVEN a header dictionary
    WHEN is_header is called
    THEN True is returned
    """
    assert test_header == True


def test_get_fields(test_get_fields):
    """
    GIVEN a row dictionary
    WHEN get_fields is called
    THEN valid fields tuple is returned
    """
    assert test_get_fields == ("user-id", "page-url", "timestamp", "page-name")
