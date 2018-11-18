import sys
import os
import optparse                 # allows OptionParser for command line options
import time                     # used to timestamp files

version = '0.1.1'


class CSVStringSorter:
    def __init__(self, input_file, output_file, limit, verbose=True):
        self.input_file = input_file
        self.output_file = output_file
        self.limit = limit
        self.verbose = verbose

        self.input_line = None          # mvp scope: only parse a single line a file, else would use array

    def sort_input(self):
        if self.verbose:
            print("1. Loading Input")
        if not self.load_input():
            return False

        if self.verbose:
            print("2. Sorting Line")
        sorted_line = self.sort_line()

        if self.verbose:
            print("3. Writing Output")
        self.write_output(sorted_line=sorted_line)

    def sort_line(self):
        # TODO: Perform sort
        return self.input_line

    def write_output(self, sorted_line):
        output_file = self.output_file
        try:
            if os.path.exists(output_file):
                # adjust the filename to create a unique time-stamped file for the output (non-destructive)
                output_file = self.get_unique_file_name(output_file)
            with open(output_file, "w+") as f:
                f.write(sorted_line)
            print("Output written to: {0}".format(output_file))
        except IOError:
            print("Error: Unable to write output to: {0}".format(output_file))
            return True
        return False

    @staticmethod
    def get_unique_file_name(input_name):
        timestr = time.strftime("%Y%m%d%H%M%S")
        filename, file_extension = os.path.splitext(input_name)
        output_file = "{0}_{1}".format(filename, timestr)
        if file_extension:
            output_file = "{0}{1}".format(output_file, file_extension)
        return output_file

    def load_input(self):
        # Traditionally I would do checks / fail if input is not correct: Look Before You Leap
        #  if not self.input_file:
        #     print("Input failed: No input file specified")
        # if not os.path.exists(self.input_file):
        #     print("Input failed: Input file does not exist")

        # However, the Pythony design philosophy is 'Easier to Ask for Forgiveness than Permission'
        # https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/
        try:
            with open(self.input_file) as open_file:
                # using readline() because it is only first line.
                # would not use readlines() as that would try to read the whole file into memory -> 'for line in f'
                if not self.limit:
                    self.input_line = open_file.readline()
                else:
                    self.input_line = open_file.readline(self.limit)
        except IOError:
            print("Error: Unable to read input file: {0}".format(self.input_file))
            self.input_line = None
            return False
        # as per PEP 8, not using broad exception, handling specific situations, allowing exceptional failures

        if self.verbose:
            print("Input line: {0}".format(self.input_line))
        return True


def main():
    print("Executing 'CSVStringSorter' {0}".format(version))
    options = parse_options()
    print("\tInput file: {0}".format(options.input_file))
    print("\tOutput file: {0}".format(options.output_file))

    sorter = CSVStringSorter(input_file=options.input_file, output_file=options.output_file,
                             limit=options.limit, verbose=options.verbose)
    sorter.sort_input()

    sys.exit(0)


def parse_options():
    p = optparse.OptionParser(
        description="Sort a comma-separated string",
        prog="stringsorter",
        usage="\n%prog (optional)--input [inputfile] (optional)--output [outputfile]\n"
    )

    p.add_option('--input', '-i', action="store", dest="input_file", type="string", default="input.csv",
                 help="(opt) CSV file being sorted (def) input.csv")
    p.add_option('--output', '-o', action="store", dest="output_file", type="string", default="output.csv",
                 help="(opt) CSV file being written (if it exists, will append timestamp to new one) (def) output.csv")
    p.add_option('--limit', '-l', action="store", dest="limit", type="int",
                 help="(opt) Specify a maximum number of bytes to read from very long lines")
    p.add_option('--verbose', '-v', action="store_true", dest="verbose", default=True,
                 help="(opt) Enable extensive prints for debug purposes")
    options, args = p.parse_args()
    return options


if __name__ == "__main__":
    main()
    sys.exit(0)
