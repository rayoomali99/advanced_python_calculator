# ---------- ADVANCED PYTHON CALCULATOR ----------
# Author: Reem (Your future data queen)
# Description: A modular calculator with multiple operations and history tracking.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "❌ Error: Cannot divide by zero"

def power(x, y):
    return x ** y

def history_show(history_list):
    if not history_list:
        print("\nNo history yet.")
    else:
        print("\n---- Calculation History ----")
        for item in history_list:
            print(item)
        print("-----------------------------")

history = []

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Show History")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "7":
        print("\nGoodbye! 👋")
        break

    elif choice == "6":
        history_show(history)
        continue

    elif choice in ("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op = "/"
        elif choice == "5":
            result = power(num1, num2)
            op = "^"

        record = f"{num1} {op} {num2} = {result}"
        history.append(record)
        print("Result:", result)

    else:
        print("❌ Invalid choice, try again.")
