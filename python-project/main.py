from calculator import add, subtract, multiply, divide

print("Welcome to My Calculator!")

try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Answer:", add(number1, number2))
    elif choice == "2":
        print("Answer:", subtract(number1, number2))
    elif choice == "3":
        print("Answer:", multiply(number1, number2))
    elif choice == "4":
        print("Answer:", divide(number1, number2))
    else:
        print("Invalid choice!")

except ValueError:
    print("Error: Please enter numbers only!")
