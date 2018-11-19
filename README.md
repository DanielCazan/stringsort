# stringsort
Personal project file, not for re-distribution
Author: Daniel Cazan . danielcazan@danielcazan.com

==========
Scope

Given: 
* CSV file containing
** single line
** comma-separated string
** terminated with new line character
* default input name: 'input.csv'
When:
* strings are sorted into descending alphabetical order
Then:
* sorted strings are outputted into a new CSV
* default output name: 'output.csv'

Constraints:
* solution is runnable with a Docker command (include a Dockerfile)
* Gherkin tests for the program
** Do not have to write step definitions (tests do not have to be executable)
* Attach a write-up file with additional questions and answers

==========
Execute

Required (see Docs/Assumptions.txt):
* Persistent directory or volume that contains the input and output files
Run:
* $ docker build -t csvstringsort-docker -f Dockerfile.build .
* $ docker run --rm -v /shared_target:/app/csvstringsorter -it csvstringsort-docker python csvstringsorter.py
*   where /shared_target is a location that contains the input.csv file and will contain the output 
* Alternatively, any other way to get the input file into and out of /app/csvstringsorter on the container are fine
* Alternatively, assuming /shared_target is mapped and input.csv exists, ./quick_run.sh will build, run, and clean up
Arguments
* $ ... python csvstringsorter.py -i inputFileName.csv -o outputFileName.csv -l maxCharacterLimit --verbose

==========
Docs and Resources

Docs/Assumptions.txt - assumptions made over the course of the development, and why they were made
Docs/Changelog.txt - progress on the project (matched to commits)
Docs/ExerciseResponse.txt - answers to the questions asked in the exercise
Gherkin/* - Gherkin behaviour tests (not related to running Docker, as Docker functionality is out of scope)
References/* - unrelated python sorting algorithm samples, since python 'makes-easy' on the sorting in the exercise
Dockerfile.build - Dockerfile for building the image 
quick_run.sh - if '/shared_target' is mapped to a location with an input file, goes through a potential end-to-end flow
input.csv - sample csv file.  only the first line is read.  