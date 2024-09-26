import sympy as sp

# Linear Equation Solver (ax + b = 0)
def solve_linear(a, b):
    x = sp.symbols('x')
    equation = a * x + b
    solution = sp.solve(equation, x)
    return solution

# Quadratic Equation Solver (ax^2 + bx + c = 0)
def solve_quadratic(a, b, c):
    x = sp.symbols('x')
    equation = a * x**2 + b * x + c
    solutions = sp.solve(equation, x)
    return solutions

# Simplifying algebraic expressions
def simplify_expression(expression):
    return sp.simplify(expression)

# Expanding algebraic expressions
def expand_expression(expression):
    return sp.expand(expression)

# Menu for the algebra project
def algebra_calculator():
    print("Welcome to the Algebra Calculator!")
    print("1. Solve a linear equation (ax + b = 0)")
    print("2. Solve a quadratic equation (ax^2 + bx + c = 0)")
    print("3. Simplify an algebraic expression")
    print("4. Expand an algebraic expression")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("\nSolve Linear Equation (ax + b = 0):")
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the constant b: "))
        solution = solve_linear(a, b)
        print(f"Solution: x = {solution}")

    elif choice == 2:
        print("\nSolve Quadratic Equation (ax^2 + bx + c = 0):")
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the constant c: "))
        solutions = solve_quadratic(a, b, c)
        print(f"Solutions: x = {solutions}")

    elif choice == 3:
        print("\nSimplify Algebraic Expression:")
        expression = input("Enter the algebraic expression (e.g., 'x^2 + 2*x + 1'): ")
        simplified_expr = simplify_expression(expression)
        print(f"Simplified Expression: {simplified_expr}")

    elif choice == 4:
        print("\nExpand Algebraic Expression:")
        expression = input("Enter the algebraic expression (e.g., '(x + 1)^2'): ")
        expanded_expr = expand_expression(expression)
        print(f"Expanded Expression: {expanded_expr}")

    else:
        print("Invalid choice. Please select a valid option.")

# Run the algebra calculator
if __name__ == "__main__":
    algebra_calculator()
