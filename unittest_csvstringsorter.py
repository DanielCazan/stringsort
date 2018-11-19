import  unittest
from csvstringsorter import CSVStringSorter


# At this time picking unittest over pytest because it is boilerplate and easy to read / understand / run
#   In a bigger project I would likely explore pytest more extensively
# This also deviates somewhat for the specified sorting.features tests - those are intended for automated test suite
#   Component automated tests are intended to give constant clear answers over large suites, and should have single
#   points of failure.  Just seeing which tests fail should clearly indicate what the problem is, and they are often
#   black-box tests so we don't want to exercise multiple behaviors
#   Unit-tests are best used by developers as quick sanity-checks, and are usually white-box tests.  The space exercised
#   is small by-design, if something breaks it should be easy to pick out what happened, and fast development is more
#   important than single-purpose testing
class TestSorting(unittest.TestCase):
    def test_three_word_mixedcase(self):
        test_string = "Copenhagen,Stockholm,oslo"
        expected_output = "Stockholm,oslo,Copenhagen"
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def test_three_word_spaces(self):
        test_string = "Copenhagen ,Stock holm, oslo"
        expected_output = "Stock holm,oslo,Copenhagen"
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def test_empty_string(self):
        test_string = ""
        expected_output = ""
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def test_empty_bad_commas(self):
        test_string = ",Copenhagen,,Stockholm, ,oslo,"
        expected_output = "Stockholm,oslo,Copenhagen"
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def test_empty_numerical(self):
        test_string = "3, 201,21"
        expected_output = "3,21,201"
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def test_empty_alphanumerical(self):
        test_string = "3, a, B, X, z, 201,21"
        expected_output = "z,X,B,a,3,21,201"
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def test_empty_ascii(self):
        test_string = "#,P,{,s,a,]"
        expected_output = "{,s,P,a,],#"
        self._sort_and_compare(expected_output=expected_output, test_string=test_string)

    def _sort_and_compare(self, expected_output, test_string):
        sorter = CSVStringSorter(input_file=None, output_file=None, limit=None, verbose=False)
        sorter.set_input_line(test_string)
        self.assertEqual(expected_output, sorter.sort_line())


if __name__ == '__main__':
    unittest.main()
