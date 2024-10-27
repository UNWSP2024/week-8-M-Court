#3: CAPITALS QUIZ 

#Write a program that creates 
	#a dictionary containing the U.S. states as keys, and their capitals as values.  
#The program should then randomly quiz the user by displaying the name of a state and asking the user to enter the state's capital.  
#The program should count of the number of correct and incorrect responses. 
#(You could alternatively use another country and provinces, or countries of the world and capitals).

#set at 0
correct_answers = 0
incorrect_answers = 0

#create dictionary
states_and_capitals = {"Alabama":"Montgomery", "Florida":"Tallahasse", "Arizona":"Pheonix"}

#see if guess is correct
def correct_or_incorrect(guess, city):
		#create correct answer count
		global correct_answers
		if guess == city:
			print(f"{guess} is correct!")
			correct_answers += 1
		#create false answer count
		global incorrect_answers
		if guess != city:
			print(f"{guess} is incorrect. Next!")
			incorrect_answers += 1

#list total score
def score():
		#correct
		print(f"You got {correct_answers} correct answer(s)!")
		#incorrect
		print(f"You got {incorrect_answers} incorrect answer(s).")		

#get user's guess
for key in states_and_capitals:
		#get user guess
		guess = input(f"What is the capital of {(key)}? (please capitalize) " )
		#correct answer
		city = states_and_capitals.get(key)
		#see if guess is correct
		correct_or_incorrect(guess, city)

#show total score
score()