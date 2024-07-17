# Day 2 Project: Tip Calculator done on June 27, 2024
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give; 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_for_each_person = "{:.2f}".format(((total_bill*(tip/100)) + total_bill)/people) # the "{:.2f}".format(what_you_want_round_up) is used to round it to the 2 decimal places
print(f"Each person should pay: ${bill_for_each_person}")