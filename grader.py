#if age is 5 Go to kindergarten
#Ages 6 through 17 goes to grade 1 through 12
#if age is greater than 17 say go to college
# Try to complete with 10 less lines

age = eval(input("Enter your age: "))

if age < 5:
    print("Too Young for school")
elif age == 5:
    print("Go to kindergarten")
elif age <= 17:
    print("Go to High school")
else:
    print("Go to college")