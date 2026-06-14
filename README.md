# BMI Calculator

## Project Description

The BMI (Body Mass Index) Calculator is a Python-based command-line application that calculates a user's BMI using their weight and height. Based on the calculated BMI value, the program classifies the user into a health category such as Underweight, Normal Weight, Overweight, or Obese.

This project demonstrates the use of mathematical calculations, user input handling, and conditional statements in Python.

## Features

* Accepts user weight in kilograms
* Accepts user height in meters
* Calculates BMI using the standard BMI formula
* Displays BMI rounded to two decimal places
* Categorizes BMI into health ranges
* Simple command-line interface

## Technologies Used

* Python 3

## Project Structure

```text
BMI-Calculator/
│
├── bmi_calculator.py
└── README.md
```

## How to Run

### Step 1: Download the Project

Save the Python file on your computer.

### Step 2: Run the Program

```bash
python bmi_calculator.py
```

## Example Usage

```text
=== BMI Calculator ===

Enter weight (kg): 70
Enter height (meters): 1.75

Your BMI: 22.86
Category: Normal weight
```

## BMI Formula

BMI is calculated using:

BMI = Weight (kg) / Height² (m²)

## BMI Categories

| BMI Range    | Category      |
| ------------ | ------------- |
| Below 18.5   | Underweight   |
| 18.5 - 24.9  | Normal Weight |
| 25 - 29.9    | Overweight    |
| 30 and above | Obese         |

## How It Works

1. The user enters weight and height.
2. The application calculates BMI using the standard formula.
3. The BMI value is displayed.
4. The user is classified into the appropriate health category.

## Concepts Used

* User Input Handling
* Mathematical Calculations
* Conditional Statements
* Data Validation
* Python Basics

## Error Handling

The application checks whether the height entered is greater than zero before performing the BMI calculation.

## Future Improvements

* Graphical User Interface (GUI)
* BMI history tracking
* Data storage for multiple users
* BMI trend analysis
* Graphical reports and charts
* Health recommendations based on BMI

## Learning Outcomes

This project helped in understanding:

* BMI calculation logic
* User input validation
* Decision-making using conditional statements
* Building simple health-related applications in Python

## Author

Gokulnath S

Python Programming Internship Project
