print("Welcome. I'll help you do basic Math!")
print("Type 'exit' to quit")

while True:
    operation = input("Choose +, -, /, *: ")
    if operation.lower() == "exit":
        break
    if operation not in ['+', '-', '*', '/']:
        print("Invalid option. Try again!")
        continue
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Print valid numbers")
        continue

    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Error: A number can't be divided by 0")
            continue
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

