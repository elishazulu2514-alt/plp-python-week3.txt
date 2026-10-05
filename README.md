# Week 3 Assignment on Conditions and Loops

## Project Description
- `grade_reporter.py`: Processes student scores to print grades (A, B, C, F), counts passes and fails, and calculates the overall rounded average score.
- `bug_hunt.py`: Fixes syntax and logic bugs in a while-loop program to correctly sum numbers from 1 to 5.

## Reflection
The hardest bug to find in Part B was the off-by-one logic error (`count < 5` stopping before 5). Unlike the missing colon or string concatenation errors, this bug produced no runtime error message and allowed the script to run cleanly. I realized there was a bug because the printed output was `10` instead of the expected sum of `15`.
