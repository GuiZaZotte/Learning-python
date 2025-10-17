print("Hello, please give two integers numbers :")
number1 = input()
number2 = input()
if not number1.isnumeric() or not number2.isnumeric() :
    print("Choose integers numbers")
    raise SystemExit("End of the program")
number1 = int(number1)
number2 = int(number2)
operation = input("What operation do you want + ; - ; * ; / ?\n")
if operation not in ["+", "-","*","/"]:
    print("Choose an existant operation.")
    raise SystemExit("End of the program")
if operation == "+":
    result = number1+number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 == 0:
        print("Number 2 can't be equal to 0.")
        raise SystemExit("End of the program")
    result = round(number1 / number2)
print(f"The result of the operation is {result}")