import Jerome_Vankpana_Stats
#open files
file = open("50DayFruitData.txt","r")
#extract data from the files
data = file.read().splitlines()
#Removing the title line
data.pop(0)
#create empty list
apples = []
mod = []
#loop to examine the function
for day in data:
    
    temp = day.split()

    if temp[1] == "apple":
        apples.append(int(temp[2]))
        if temp[2] != 5:
            mod.append(int(temp[2]))
        

mean = Jerome_Vankpana_Stats.mean(apples)
median = Jerome_Vankpana_Stats.median(apples)
mode = Jerome_Vankpana_Stats.mode(apples)
mode2 = Jerome_Vankpana_Stats.mode(mod)

#print(apples)
with open("Jerome_Vankpana_Out.txt", "w") as f:
    f.write("Apples"+"\n"+"Mean :"+str(mean)+"\n"+"Median: "+str(median)+"\n"+"Mode: "+str(mode)+","+str(mode2))