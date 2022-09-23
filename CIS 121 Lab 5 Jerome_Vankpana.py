"""



"""





def main():
	
	#encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	#print(DecodeWord(encodedWord))

	DecodeWord()


#Your code goes here.
# First I had to create a new function made to decode the words.
def DecodeWord():
	Newword = "" #I then created a new variable that could store the decoded letters

	encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY" 
	for letter in  encodedWord:
		if letter == "L": #I created If and elif statements that would replace the wrong letters
			Newword += "T" # Then they were stored to the variable
		elif letter == "T":
			Newword += "L"
		elif letter == "8":
			Newword += "A"
		elif letter == "B":
			Newword += "A"
		elif letter == "A":
			Newword += "E"
		elif letter == "E":
			Newword += "B"
		else:
			Newword += letter
	print(Newword) #I then printed the variable with the decoded words.











#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
