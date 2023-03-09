import sys

from cmdline import input_loop, single_request


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        single_request(args[0])
        sys.exit(0)
    input_loop()


if __name__ == '__main__':
    main()