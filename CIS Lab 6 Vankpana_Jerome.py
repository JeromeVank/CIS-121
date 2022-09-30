import Jerome_Vankpana_Stats
#Open files 
file = open("500dayFruitData.txt", "r")
#extract the data from the files 
data = file.read().splitlines()
#Removing the title line
data.pop(0)
apples = []
bananas = []
strawberries = []
#Loop to go through the list 
for day in data:

    temp = day.split()

    if temp[1] == "apple":
        apples.append(int(temp[2]))
    elif temp[1] == "banana":
        bananas.append(int(temp[2]))
    else: #else finds the strawberry days
        strawberries.append(int(temp[2]))
#print(apples)
#print(bananas)
#print(strawberrys)

mean1 = Jerome_Vankpana_Stats.mean(apples)
median1 = Jerome_Vankpana_Stats.median(apples)
mean2 = Jerome_Vankpana_Stats.mean(bananas)
median2 = Jerome_Vankpana_Stats.median(bananas)
mean3 = Jerome_Vankpana_Stats.mean(strawberries)
median3 = Jerome_Vankpana_Stats.median(strawberries)

with open("Jerome_Vankpana_Output.txt", "w") as f:
    f.write("Apples"+"\n"+"Mean: "+str(mean1)+"\n"+"Median: "+str(median1)+"\n"+"Bananas"+"\n"+"Mean: "+str(mean2)+"\n"+"Median: "+str(median2)+"\n"+"Strawberries"+"\n"+"Mean: "+str(mean3)+"\n"+"Median: "+str(median3))
