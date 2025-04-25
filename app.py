def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user can select one of the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage (calculates num1 as a percentage of num2)

    The function prompts the user to input their choice of operation and two numeric values.
    It then performs the selected operation and displays the result.

    Error Handling:
    - If the user enters an invalid choice, an error message is displayed.
    - If the user enters non-numeric input, an error message is displayed.
    - Division by zero is handled with an appropriate error message.

    Returns:
        None
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("5. Percentage (num1 as a percentage of num2)")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please select a valid operation.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"The result is: {num1 + num2}")
        elif choice == 2:
            print(f"The result is: {num1 - num2}")
        elif choice == 3:
            print(f"The result is: {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"The result is: {num1 / num2}")
        elif choice == 5:
            if num2 == 0:
                print("Error: Division by zero is not allowed for percentage calculation.")
            else:
                print(f"The result is: {(num1 / num2) * 100}%")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()