from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse


def fix_file(filename):
    with open(filename, "rb") as f:
        contents_bytes = f.read()

    try:
        contents_text = contents_bytes.decode("UTF-8")
    except UnicodeDecodeError:
        print("{} is non-utf8 (not supported)".format(filename))
        return 1

    # TODO make this configurable
    if "NOCOMMIT" in contents_text:
        return 1

    return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= fix_file(filename)
    return retv


if __name__ == "__main__":
    exit(main())
