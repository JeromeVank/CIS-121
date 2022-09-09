#Jerome Vankpana Lab 3
# 9/9/22


earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")

while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")

if maritalStatus == "s":
    if earnedIncome < 0:
        print("You made less than $0. Contact an accountant")
    elif earnedIncome < 9950:
        Remains1 = earnedIncome - 9950
        taxowed = .10*earnedIncome 
        print("taxed owed is","$", taxowed)
    elif earnedIncome <= 40525:
            Remains1 = earnedIncome - 9950
            taxowed1 = .12 * Remains1 + (9950 * .1) #To find out how much each bracket is taxed you must subract a bracket and calculate how much remains.
            print("taxed owed is","$", taxowed1)
    elif earnedIncome <= 86375:
            Remains1 = earnedIncome - 9950
            Remains2 = Remains1 - 30575
            taxowed2 = .22 * Remains2 + (9950 * .1) + (30575 * .12)
            print("taxed owed is","$", taxowed2)
    elif earnedIncome > 86375:
        print("Hurray you made too much for this calculator")


if maritalStatus == "m":
    if earnedIncome < 0:
            print("You made less than $0. Contact an accountant")
    elif earnedIncome < 19900:
            taxowed = .10*earnedIncome
            print("taxed owed is","$", taxowed) #My code was correct and would not run until I have corrected how the if and elif statements lined up.
    elif earnedIncome <= 81050:
            Remains1 = earnedIncome - 19900
            taxowed = .12 * Remains1 + (19900 * .1)
            print("taxed owed is","$", taxowed)
    elif earnedIncome <= 172750:
     Remains1 = earnedIncome - 19900 #I wasn't aware that to find the correct answer for the third bracket you should subtract the second value from the first.
     Remains2 = Remains1 - 61150
     taxowed = (.22 * Remains2) + (19900 * .1) + (61150 * .12)
     print("taxed owed is","$", taxowed)
    elif earnedIncome > 172750:
        print("Hurray you earned to much for this calculator")
