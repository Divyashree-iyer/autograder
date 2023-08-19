# C++ Assignment Autograding

This is an example of using Python and the autograding-utils library to implement autograding for a C++ assignment. In this assignment, you can have multiple exercises within a single assignment file, and the communication with the student's code is done exclusively through standard input (std::cin).

## Assignment Overview

This assignment consists of multiple exercises where students are required to write C++ programs to solve specific problems. We use Python and the autograding-utils library to automate the testing process. The student's code will be compiled and executed, and the results will be compared with reference solutions to determine the test case outcomes.

## Building and Executing Code

To be filled

## Adding Test Cases

To add test cases for this assignment, follow these guidelines:

- Create a new directory within the `test_data` directory for each test case.
- For each test case, include the following files:
  - **input**: This file contains the input data that will be provided to the student's program via standard input (std::cin).
  - **output**: This file serves as the reference output for the test case. The student's program's output will be compared against this file to determine if the test case passed or failed.
  - **settings.yml**: This file can hold various settings for the test case. You can specify the weight assigned to the test case in this file, or any other relevant configuration.

Please note that the 'settings.yml' file mentioned above can be used for future enhancements or additional configurations but is currently not implemented in this example.

## Example Program

An example C++ program is provided as a reference for this assignment. You can find it here: [`exercise_1.cpp`](https://github.com/Divyashree-iyer/autograder/blob/main/test_data/exercise_1/exercise_1.cpp). This program demonstrates a simple scenario for illustration purposes.

## Providing Input to the Program

You can provide input to the student's program by:
- Include the input data within the 'input' file for each test case, which will be fed to the program via standard input (std::cin).

## Generated Output

This program generates a `result.json` file, which is stored inside the `results` folder. The `result.json` file is used by the autograder to show results to students who have uploaded their code.

Feel free to customize this structure and adapt the language to suit your specific assignment and requirements. Good luck with your C++ assignment autograding!
