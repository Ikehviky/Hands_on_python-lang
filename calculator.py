#Store the user input of 2 number and the operator
print("=== Make sure to give space after each operator and operand ===")
num1, operand, num2 = input("Enter Calculation: ").split()

#Conver the strings into integers
num1 = int(num1)
num2 = int(num2)

#if + then we provide output based on addition

print("okay you want to perform a {} operation".format(operand))

if operand == '+':
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operand == '-':
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operand == '*':
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operand == '/':
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operand == '%':
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else: 
    print("Use either + - * / or % next time.")