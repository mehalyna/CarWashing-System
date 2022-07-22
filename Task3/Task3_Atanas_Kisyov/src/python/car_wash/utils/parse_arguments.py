import argparse


def add_arguments() -> dict:
    """Initialize available arguments for user to pass to the program"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-ro, -rw', '--read-only, --read-write', default='-ro')
    args = parser.parse_args()
    return args
