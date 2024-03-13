# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate is
# Print out the earnings after a 10 year period

money = input("Enter your investment amount: ")
interest_rate = input("Enter your interest rate: ")

money = float(money)

interest_rate = float(interest_rate) * .01

for _i in range(10):
    money = money + (money * interest_rate)

print("Investment after 10 years : {:.2f}".format(money))