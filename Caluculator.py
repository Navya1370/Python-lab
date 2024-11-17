# Define the functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Display options
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")

                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")

            except ValueError:
                print("Invalid input. Please enter numbers.")
            
            # Ask if the user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the calculator
calculator()
