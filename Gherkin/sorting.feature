Feature: Sorting CSV input
  A single comma-separated line will sort what is between commas in descending alphabetical order

  Scenario: Sorting simple word list
    Given the script has loaded a simple list with multiple out-of-order comma-separated words
    When the script provides output
    Then the output is each word in descending alphabetical order by the first letter of each word
    And case in the input is ignored for the purpose of sorting
    And case is maintained in the output

  Scenario: Sorting an empty list
    Given the script has loaded a simple list with no content
    When the script provides output
    Then the output is empty

  Scenario: Sorting a list of phrases
    Given the script has loaded a simple list with multiple words between each comma
    When the script provides output
    Then the output is each set of words in descending alphabetical order by the first letter of the first word

  Scenario Outline: Sorthing through bad comma formatting
    Given the script has loaded a simple list with bad csv <formatting>
    When the script provides output
    Then the output is only of the <valid> words
    And the output is each word in descending alphabetical order by the first letter of each word

    Examples:
      | formatting |  valid |
      | b, a, c,   |  c,b,a |
      | ,b, a, c   |  c,b,a |
      | ,b, ,c     |  c,b   |

  Scenario Outline: Sorting with Alphanumeric characters
    Given the script has loaded a simple list with <alphanumeric> leading characters
    When the script provides output
    Then the output is each csv-separated segment in descending <alphanumeric_order>
    And the output has any number-led segments at the end of the output
    And the output has numbers sorted alphabetically rather than numerically

    Examples:
      | alphanumeric    |  alphanumeric_order |
      | 2, 1, 3         |  3,2,1              |
      | b, 2, c         |  c,b,2              |
      | b, 2, 20        |  b,20,2             |
      | b, 201, 21      |  b,21,201           |
      | 3, 201, 21      |  3,21,201           |

  Scenario: Sorting with Ascii characters
    Given the script has loaded a simple list with mixed-ascii characters in front of some of the words
    When the script provides output
    Then the output is each csv-separated segment in descending order based on the position in the ascii table
    And the output uses the lower-case equivalent of any letters to determine their position in the table