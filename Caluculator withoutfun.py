print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take user input for operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        try:
        
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the selected operation
            if choice == '1':
                result = num1 + num2
                print(f"The result is: {result}")

            elif choice == '2':
                result = num1 - num2
                print(f"The result is: {result}")

            elif choice == '3':
                result = num1 * num2
                print(f"The result is: {result}")

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers.")
        
    
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid choice. Please enter a valid option.")
