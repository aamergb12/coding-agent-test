class Calculator:
    def add(self, x, y):
        """Add two numbers"""
        return x + y

    def subtract(self, x, y):
        """Subtract two numbers"""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y

    def divide(self, x, y):
        """Divide two numbers"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

def main():
    calc = Calculator()
    
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice!")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print("Result:", calc.add(num1, num2))
        elif choice == '2':
            print("Result:", calc.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calc.multiply(num1, num2))
        elif choice == '4':
            try:
                print("Result:", calc.divide(num1, num2))
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()