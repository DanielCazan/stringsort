Feature: Input and output file control
  Explore the desired behavior related to CSV file inputs and outputs

  Scenario: Simple input.csv file and no output.csv in the folder
    Given the script is called with default arguments
    And the file input.csv is available in the directory
    And the file output.csv is not available in the directory
    When the output file is generated
    Then a file output.csv is generated with the sorted output

  Scenario: Simple input.csv file and output.csv in the folder
    Given the script is called with default arguments
    And the file input.csv is available in the directory
    And the file output.csv already exists in the directory
    When the output file is generated
    Then a file output_timestamp.csv is generated with the sorted output

  Scenario: Missing input.csv file
    Given the script is called with default arguments
    And the file input.csv is not available in the directory
    When the script is run
    Then no output file is generated
    And the script print out a message that the input was not available

  Scenario: Specified input file
    Given the script is called with default output and a specified available input file
    When the script is run
    Then a file output.csv is generated with the sorted output

  Scenario: Specified output file
    Given the script is called with default input and a specified available output file
    When the script is run
    Then the specified output file is generated with the sorted output