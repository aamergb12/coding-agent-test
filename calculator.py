class Calculator:
    def __init__(self):
        pass

    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Raise a to power of b"""
        return a ** b

    def square_root(self, a: float) -> float:
        """Calculate square root of a number"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5