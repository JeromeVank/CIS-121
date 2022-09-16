x = 1
y = 1
summ = 0
perfect = 0
abundant = 0
deficient = 0
bound = int(input("Enter a upper bound: "))
while x <= bound:
    while y < x:
         if x % y == 0:
            summ += y
         y += 1

    if x == summ:
        perfect += 1
    if x < summ:
        abundant += 1
    if x > summ:
        deficient += 1
    summ = 0
    x += 1   
    y = 1 

print("Between 1 and", bound, "there are" )    
print(deficient,"deficient numbers")
print(perfect,"perfect numbers")         
print (abundant,"abundant numbers")
    
        



