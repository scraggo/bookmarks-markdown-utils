import sys

from utils import arg_utils

rest_of_args = arg_utils.get_rest_of_args(sys.argv[1:])
arg_utils.execute_args(rest_of_args)
