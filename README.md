# FuzzyLogic_Assignment
Part of the coursework for the CS4047 Computational Intelligence course at the University of Aberdeen

### Problem description
Given a text file, containing a set of rules, a set of `n` variables with their 4-tuple fuzzy representation and a set of real life values for `n - 1` of these variables, provide a real life value for the missing variable.

A detailed description of the project can be found in the `CS4047_Report_Pavlova_SS.pdf` file.

### Problem Representation
The problem is provided to the program in the form of a text file where all the rules, the
variables and their 4-tuple fuzzy representation and the real world values of the variables
are given. A sample problem can be found in the `currentRulebase.txt` file

### Running the system

To run the system, you need to have Python 2.7 installed.

To run the entire system 

1. Open a terminal
2. Navigate to the folder where the `__init__.py` file is located
3. Type python `__init__.py` in the command line

This will run the `__init__.py` file.
You will get the result for the tippingRulebase.txt file.



To test the system on another file:

1. Place the file in the same directory as the `__init__.py` file
2. Open the `__init__.py` file in an editor
3. Replace "tippingRulebase.txt" on line 9 with the name of your file
4. Run `__init__.py`

Two more sample files are available in the same directory as `__init__.py`,
namely currentRulebase.txt and drugRulebase.txt.


