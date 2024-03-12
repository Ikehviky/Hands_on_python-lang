#Problem: Receive miles and convert to kilometers
#kilometers = miles * 1.60934
#Enter Miles 5
#5 miles equals 8.04 kilomiters


#Ask the user to input miles and assign it to the miles variable
miles = input("How many miles form your house to the bus pack: ")

#Convert from string to integer
miles = int(miles)

#convert to kilometers
kilometers = miles * 1.60934

#print out
print("Your house  is {} miles, which is {} kilomiters to the bus pack".format(miles, kilometers))