# dynamic_import_test.py

import importlib

def main():
    # Dynamically import the math_operations module
    math_operations = importlib.import_module('math_operations')

    # Create an instance of the Calculator class
    calculator = math_operations.Calculator()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print(f"Addition: {calculator.add(num1, num2)}")
        print(f"Subtraction: {calculator.subtract(num1, num2)}")
        print(f"Multiplication: {calculator.multiply(num1, num2)}")
        print(f"Division: {calculator.divide(num1, num2)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()