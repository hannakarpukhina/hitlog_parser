import sys


def get_param_by_index(param_index, default_val):
    if len(sys.argv) > param_index:
        return sys.argv[param_index]
    else:
        return default_val


def get_src_file_name(default_val):
    return get_param_by_index(1, default_val)


def get_dst_file_name(default_val):
    return get_param_by_index(2, default_val)


def get_output_limit(default_val):
    return get_param_by_index(3, default_val)
