#2: WORD SEPARATOR

#Write a program that accepts as input 
	#	a sentence in which all of the words are run together, 
	#	but the first character of each word is uppercase. 
	#Convert the sentence to a string in which 
		#the words are separated by spaces, 
		#and the first word starts with an uppercase.

#For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."


#function
def spacer(closed_sentence):	
		#take first letter
		open_sentence = closed_sentence[0]	
		#find capitals? how to find capitals when whole sentence is not capital 
		for character in closed_sentence[1:]:
			if character.isupper():
					open_sentence += " " + character.lower()
			else:
					open_sentence += character
		return open_sentence

#get first sentence
closed_sentence = input("Enter a sentence with no spaces, capitalizing the first letter of each word: ")
#run spacing function
print(spacer(closed_sentence))