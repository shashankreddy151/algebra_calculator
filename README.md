# Algebra Calculator

This is a simple Python project that serves as an **Algebra Calculator**. It can solve linear and quadratic equations, simplify algebraic expressions, and expand algebraic expressions using the **SymPy** library.

## Features

1. **Linear Equation Solver**: Solves equations of the form `ax + b = 0`.
2. **Quadratic Equation Solver**: Solves quadratic equations of the form `ax^2 + bx + c = 0`.
3. **Simplify Algebraic Expressions**: Simplifies expressions like `x^2 + 2*x + 1`.
4. **Expand Algebraic Expressions**: Expands expressions like `(x + 1)^2`.

## Requirements

- Python 3.x
- [SymPy](https://www.sympy.org/) library

Install the SymPy library using pip:

```bash
pip install sympy
```

<<<<<<< HEAD
<<<<<<< HEAD
## How to Run

1. **Clone the Repository**: First, clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/algebra-calculator.git
   ```

## How to Run

1. **Clone the Repository**: First, clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/algebra-calculator.git
   ```
=======
>>>>>>> cb132b50688117cd402f600a3a233fbdb35eb1a2
=======
## How to Run
>>>>>>> 901c29f7c53e0857bb1aef43881e34463eca8da1

1. **Clone the Repository**: First, clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/algebra-calculator.git
   ```
2. **Navigate to the Project Directory**: Change your current working directory to the project folder:

   ```bash
   cd algebra-calculator
   ```
3. **Run the Script: Use the following command to execute the script:

   ```bash
   python algebra_calculator.py
   ```

# Usage Instructions

Upon running, you will see a welcome message and a menu with the following options:
```bash
1. Solve a linear equation (ax + b = 0)
2. Solve a quadratic equation (ax^2 + bx + c = 0)
3. Simplify an algebraic expression
4. Expand an algebraic expression
```
## Select an Option

Enter the number corresponding to your choice (1-4) and press Enter.

### Input Requirements

- **For Linear Equation Solver (Option 1)**:
  You will be prompted to enter the coefficient \( a \) and the constant \( b \).
  - **Example**: For the equation \( 2x + 4 = 0 \), input \( a = 2 \) and \( b = 4 \).

- **For Quadratic Equation Solver (Option 2)**:
  You will be prompted to enter the coefficients \( a \), \( b \), and the constant \( c \).
  - **Example**: For the equation \( x^2 - 3x + 2 = 0 \), input \( a = 1 \), \( b = -3 \), and \( c = 2 \).

- **For Simplifying an Algebraic Expression (Option 3)**:
  Enter the expression you want to simplify in standard Python syntax.
  - **Example**: For \( x^2 + 2x + 1 \), input `x**2 + 2*x + 1`.

- **For Expanding an Algebraic Expression (Option 4)**:
  Enter the expression you want to expand.
  - **Example**: For \( (x + 1)^2 \), input `(x + 1)**2`.

### View Results

The program will output the result based on your input. Follow the on-screen prompts to see the solutions or simplified expressions.

## Example of Using the Calculator

Here’s a quick example of how to solve a quadratic equation:
```bash
Welcome to the Algebra Calculator!
1. Solve a linear equation (ax + b = 0)
2. Solve a quadratic equation (ax^2 + bx + c = 0)
3. Simplify an algebraic expression
4. Expand an algebraic expression

Enter your choice (1-4): 2

Solve Quadratic Equation (ax^2 + bx + c = 0):
Enter the coefficient a: 1
Enter the coefficient b: -3
Enter the constant c: 2
Solutions: x = [1, 2]
```

## License

This project is licensed under the MIT License.

## Contributor

Shashank Reddy kallem
