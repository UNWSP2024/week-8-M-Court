#1: Initials

#gets a string containing
	# a person's first, middle, and last names, 
#displays 
	#their first, middle, and last initials.  

#For example, if the user enters John William Smith, the program should display J. W. S.

#get first sentence
full_name = input("Enter a full name (please capitalize): ")
initial = ("")
all_initials = ("")
#find first letter
for character in full_name:
	if character.isupper():
		initial = character + ". "
		all_initials += initial

#show initials
print(all_initials)