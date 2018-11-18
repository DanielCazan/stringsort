#!/usr/bin/env python
import optparse         # allows OptionParser for command line options
import sys              # allows sys.exit

from alg_sort import ArraySorter


def main():
    options = parse_options()

    unsorted_list_20 = [1, 15, 8, 11, 14, 2, 17, 7, 18, 4, 5, 9, 20, 19, 6, 10, 16, 3, 13, 12]

    print("Executed main with options")
    if options.sort_op:
        print("sort_op: {0}".format(options.sort_op))
        array_sorter = ArraySorter(sortable_array=unsorted_list_20)
        array_sorter.sort_functions(sort_op=options.sort_op)

    sys.exit(0)


def parse_options():
    # https://docs.python.org/2/library/optparse.html
    p = optparse.OptionParser(
        description="",
        prog="sort_and_search",
        usage="\n%prog --sort] [type]\n"
    )
    # Currently only implemented sort

    sort_options = "selection, insertion, quick, merge, bubble, bucket, heap"

    p.add_option('--sort', '-o', action="store", dest="sort_op", type="string",
                 help="Sort a prepared list of data.  Ops: {0}".format(sort_options))
    options, args = p.parse_args()
    return options


if __name__ == "__main__":
    main()
    sys.exit(0)
