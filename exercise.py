def add(num1, num2):
    try:
        result = float(num1) + float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

def subtract(num1, num2):
    try:
        result = float(num1) - float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

def multiply(num1, num2):
    try:
        result = float(num1) * float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

def divide(num1, num2):
    try:
        result = float(num1) / float(num2)
        return result
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")


def driver():
    while True:
        print("\nSimple Calculator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        try:
            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Invalid choice! Please choose a valid option.")
        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    driver()