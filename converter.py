#Ask the user to input 2 values and store them in variables num1 num2:

num1, num2 = input("Enter two numbers: ").split()

#convert the strings into regular number:

num1 = int(num1)
num2 = int(num2)

#Add the values entered and store in sum:

sum = num1 + num2

#Subtract values and store in difference:

sub = num1 - num2

#Multiply the vlues and store in product:

multiply = num1 * num2

#Divide the values and store in quotient

Divide = num1 / num2

#Use modulus in the values to find the remainder:

mod = num1 % num2

#Print the result

print("sum: {}, sub: {}, multiply: {}, divide: {}, mod: {}".format(sum, sub, multiply, Divide, mod))
