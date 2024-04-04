def test_get_param_src_file_name(test_param_src_file_name):
    """
    GIVEN a parameter of soutce file name
    WHEN get_src_file_name is called
    THEN valid sousce file name is returned
    """
    assert test_param_src_file_name == "/static/test_input.csv"


def test_get_param_dst_file_name(test_param_dst_file_name):
    """
    GIVEN a parameter of destination file name
    WHEN get_dst_file_name is called
    THEN valid destination file name returned
    """
    assert test_param_dst_file_name == "/static/test_output.csv"


def test_get_param_output_limit(test_param_output_limit):
    """
    GIVEN an output limit value
    WHEN get_output_limit is called
    THEN value of uotput limit is returned
    """
    assert test_param_output_limit == 3


def test_get_param_by_index(test_param_by_index):
    """
    GIVEN a parameter index
    WHEN get_param_by_index is called
    THEN value of index is returned
    """
    assert test_param_by_index == "/static/test_input.csv"
