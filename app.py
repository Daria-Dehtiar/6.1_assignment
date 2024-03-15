num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Which operation would you like to be executed + or - ? ")

def calculation(num1: float, num2: float, operation: str):
    result = 0

    if operation == "+":
        result = num1 + num2
    if operation == "-":
        result = num1 - num2
    return result

print(calculation(num1, num2, operation))


