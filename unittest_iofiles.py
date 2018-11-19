import os
import unittest
import glob
from csvstringsorter import CSVStringSorter


class TestFileIO(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.input_file = "unittest_in.csv"
        self.output_file = "unittest_out.csv"
        self.source_line = "Copenhagen,Stockholm,Oslo"
        self.expected_output = "Stockholm,oslo,Copenhagen"

    # clean set after every test
    def setUp(self):
        # create a fresh unit test input-file
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        with open(self.input_file, "w+") as f:
            f.write(self.source_line)

    # clean up after every test
    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)

        output_files = glob.glob("unittest_out*csv")
        for file in output_files:
            os.remove(file)

    def test_no_input_file(self):
        file_name = "nofile.csv"
        sorter = CSVStringSorter(input_file=file_name, output_file=None, limit=None, verbose=False)
        self.assertFalse(sorter.sort_input())

    def test_input_output(self):
        self.assertTrue(os.path.exists(self.input_file))

        sorter = CSVStringSorter(input_file=self.input_file, output_file=self.output_file, limit=None, verbose=False)
        self.assertTrue(sorter.sort_input())
        self.assertTrue(self._confirm_output(target_file=self.output_file, expected_output=self.expected_output))

    def test_duplicate_output(self):
        self.assertTrue(os.path.exists(self.input_file))

        sorter_1 = CSVStringSorter(input_file=self.input_file, output_file=self.output_file, limit=None, verbose=False)
        self.assertTrue(sorter_1.sort_input())

        sorter_2 = CSVStringSorter(input_file=self.input_file, output_file=self.output_file, limit=None, verbose=False)
        self.assertTrue(sorter_2.sort_input())

        output_files = glob.glob("unittest_out*csv")
        self.assertEqual(len(output_files), 2)
        self.assertTrue(self._confirm_output(target_file=output_files[0], expected_output=self.expected_output))
        self.assertTrue(self._confirm_output(target_file=output_files[1], expected_output=self.expected_output))

    def test_character_limit(self):
        test_string = "123, 678,012"
        limit = 7
        expected_output = "78,123"

        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        with open(self.input_file, "w+") as f:
            f.write(test_string)

        sorter = CSVStringSorter(input_file=self.input_file, output_file=self.output_file, limit=limit, verbose=False)
        self.assertTrue(sorter.sort_input())
        self.assertTrue(self._confirm_output(self.output_file, expected_output))

    @staticmethod
    def _confirm_output(target_file, expected_output):
        try:
            with open(target_file) as open_file:
                actual_output = open_file.readline()
                return actual_output == expected_output
        except Exception:
            return False


if __name__ == '__main__':
    unittest.main()