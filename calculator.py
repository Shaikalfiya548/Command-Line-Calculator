
# Command Line Calculator

# Addition function
def add(a, b):
    return a + b


# Subtraction function
def subtract(a, b):
    return a - b


# Multiplication function
def multiply(a, b):
    return a * b


# Division function
def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


# Main calculator function
def calculator():
    while True:

        print("\n===== COMMAND LINE CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "6":
            print("Thank you for using Calculator!")
            break

        elif choice == "5":
            print("Calculator cleared!")
            continue

        elif choice in ["1", "2", "3", "4"]:

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)

                elif choice == "2":
                    result = subtract(num1, num2)

                elif choice == "3":
                    result = multiply(num1, num2)

                elif choice == "4":
                    result = divide(num1, num2)

                print("Result:", result)

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Please select 1 to 6.")


# Start the calculator
calculator()
