# math_operations.py

class Calculator:
    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers."""
        return a * b

    def divide(self, a, b):
        """Divides two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b