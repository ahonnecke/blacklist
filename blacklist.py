from __future__ import absolute_import, print_function, unicode_literals

import argparse


# TODO make this configurable
def search_file(filename, bad_string):
    retv = 0

    with open(filename, "rb") as f:
        contents_bytes = f.read()

    try:
        contents_text = contents_bytes.decode("UTF-8")
    except UnicodeDecodeError:
        print("{} is non-utf8 (not supported)".format(filename))
        return 1

    if bad_string not in contents_text:
        return 0

    with open(filename) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if bad_string in line:
                print(f"{filename}: {cnt}")
                line = fp.readline()
                cnt += 1
                retv = 1

    return retv


def fix_file(filename):
    return search_file(filename, "NOCOMMIT")


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
