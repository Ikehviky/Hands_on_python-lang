# Problem: will provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important

#Receive the input of age
age = eval(input("Enter your age: "))

if age >= 1 & age <= 18:
    print("You are {} Your birthday is very imprtant".format(age))
elif age == 21 | age == 50:
    print("You are {} Your birthday is Important".format(age))
elif not(age < 65):
    print("Imortant Birthday")
else:
    print("Sorry Not Important")