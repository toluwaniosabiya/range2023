range
==============================

A range problem

Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    ├── notebooks
    ├── reports
    │   └── figures
    └── src
        ├── data
        ├── external
        ├── models
        ├── tools
        └── visualization


# Range 2023
This repository has the code to solve the range problem related with the Data Workshop - LIDA 23

## Scenarios

### Scenario 1 - point

- Parameters: [[13, 0], [0, 4.5]]
- Result: [0, 0]

### Scenario 2 - No overlap

- Parameters: [[-3, -1], [0, 4.5]]
- Result: "No overlap"

### Scenario 3 - Not enough parameters

- Parameters: [13, 1]
-Result: "Enter at least two ranges"

### Scenario 4 - equal ranges

- Parameters: [[-3, 2], [-3, 2]]
- Result: [-3, 2]

### Scenario 5 - Range example

- Parameters: [[-3, 5], [0, 4.5], [-1, 2]]
- Result: [0,2]