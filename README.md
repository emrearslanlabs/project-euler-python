# Project Euler Python

A repository for solving Project Euler problems using Python while improving algorithmic thinking, problem-solving skills, and writing clean code.

## Goals

- Improve Python programming skills
- Develop algorithmic thinking
- Learn mathematical problem solving with code
- Practice time and space complexity analysis
- Build clean and readable solutions

## Workflow

For each problem:

1. Understand the problem.
2. Design an algorithm.
3. Implement the solution in Python.
4. Analyze time and space complexity.
5. Document the approach and possible optimizations.

## Solution Format

Each solution generally includes:

- Problem description
- Approach
- Time and space complexity
- Optimization notes
- Python implementation

## Technologies

- Python
- VS Code
- Git
- GitHub
- Ubuntu Linux

## Project Structure

```text
project-euler-python/
├── problem_XXX.py
├── problem-specific data files
├── .gitignore
└── README.md
```

Each `problem_XXX.py` file contains the solution for the corresponding Project Euler problem.

## Progress

Solutions are added progressively as I work through Project Euler problems.


## Running solutions

Python 3.8 or later is required (`math.comb` and `math.isqrt` are used).
All solutions use the Python standard library; no packages are required.

```bash
python3 problem_043.py
```

Problems 22 and 42 load their data next to the script, so they can also
be run from another directory. `problem_000.py` is a practice exercise,
not an official Project Euler problem.

## Verification

Run the regression checks for every solution:

```bash
python3 -m unittest discover -s tests -v
```

The checks run each script from a temporary directory and compare its
output with an independently specified expected answer. Each script has
a 60-second timeout. Problem 39 uses a cubic search and can take longer
than the other solutions.
