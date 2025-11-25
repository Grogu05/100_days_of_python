print("Welcome to the bill calculator")
total = float(input("What is the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
pay = (total + (total / 100 * tip)) / people

print(f"each person should pay: {round(pay, 2)}")