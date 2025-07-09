#!/usr/bin/env python3
"""
Calculator Application Entry Point
Provides a command-line interface for the calculator operations
"""
from calculator import Calculator
from utils import clear_screen, get_user_input

def display_menu():
    """Display the calculator menu options"""
    print("\n==== Python Calculator ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("========================")

def main():
    """Main function to run the calculator program"""
    calculator = Calculator()
    
    while True:
        clear_screen()
        display_menu()
        
        choice = get_user_input("Enter your choice (1-5): ")
        if choice == '5':
            print("Thank you for using Python Calculator!")
            break
            
        try:
            num1 = float(get_user_input("Enter first number: "))
            num2 = float(get_user_input("Enter second number: "))
            
            if choice == '1':
                result = calculator.add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
            elif choice == '4':
                result = calculator.divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nInvalid choice! Please select 1-5.")
                
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero!")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()