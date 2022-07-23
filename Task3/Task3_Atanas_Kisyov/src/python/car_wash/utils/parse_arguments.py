import argparse
import logging


def add_arguments() -> dict:
    """Initialize available arguments for user to pass to the program"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-rw', '--rw', action='store_true')
    parser.add_argument('-ro', '--ro', action='store_true')
    args = vars(parser.parse_args())
    return args
