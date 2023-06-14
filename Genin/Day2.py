# Tip Calculator
print("Welcome to the tip calculator")

bill = float(input("Please enter your bill:\n$"))

people = int(input("How many people are paying the bill?:\n"))

tip = int(input("Enter your tip Percentage: 10, 12 or 15\n"))

tip_percent = tip / 100

pay = (bill / people) * (tip_percent)

print(f"Each person is to pay ${round(pay, 2)}")
