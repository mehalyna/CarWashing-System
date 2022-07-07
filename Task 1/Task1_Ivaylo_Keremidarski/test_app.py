import logging
import sys
import time


def main():
    """Main function of module."""

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    log = logging.getLogger('my_first_docker_app')

    while True:

        log.info('It works, go to the next iteration.')
        time.sleep(3)

if __name__ == "__main__":
    sys.exit(main())
