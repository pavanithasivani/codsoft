def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Choose an operation (1-5): "))

            if choice == 5:
                print("Exiting...")
                break

            if choice < 1 or choice > 5:
                print("Invalid choice. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = add(num1, num2)
                operation = "Addition"

            elif choice == 2:
                result = subtract(num1, num2)
                operation = "Subtraction"

            elif choice == 3:
                result = multiply(num1, num2)
                operation = "Multiplication"

            elif choice == 4:
                try:
                    result = divide(num1, num2)
                    operation = "Division"
                except ZeroDivisionError as e:
                    print(e)
                    continue

            print(f"\nResult of {operation}: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    calculator()
