name = "Jerome"
last_name = "Vankpana"
age = 20 #Hash tags can be used to leave comments in code
age2 = 20.1
age3 = 20.5
print(name,last_name,age) #Using comas in between commands puts them in the same line.
print("Your age in dog years is", age * 7,"years")
modage2= int(age2)
print("Your age in dog years is", modage2 * 7,"years", int((age2-modage2 )* 12), "months",int(((age2-modage2)-(int(age2-modage2 )))* 30), "days") #My formula takes takes the decimals and turns them to whole number and uses the remainder to find days and months.
print("Your age in dog years is", age3 * 7,"years")
human_age = 45
cat_age = 9
human_age2 = 45.2
print("A 45 year old human is", human_age / cat_age, "in cat years")
print("A 45.2 year old human is", int(human_age2 / cat_age), "years",round(((human_age2 / cat_age)-(int(human_age2 /cat_age)))*12), "months and", round(((((human_age2 / cat_age)-(int(human_age2 /cat_age)))*12)*30)), "days old in cat age")
human_age2 = 10
human_age2 = 12
horse_years = 3 * ((((human_age2**2)-47) /7)+12)
y = int(horse_years)
x = round(12*(horse_years-y))
z = 12*(horse_years-y)
w = (z - int(z))*30
print("An age 12 human is", y , "years", x , "months and", round(w), "days old in horse age") #By the third problem I had a better understanding and was able to make the code less bulky.
Name = input("Please enter your name:")
Last_Name = input("please enter your last name:")
Age = int(input("please enter your age:"))
print("Name:", Name)
print("Last_Name:",Last_Name)
print("Age:", Age * 35)