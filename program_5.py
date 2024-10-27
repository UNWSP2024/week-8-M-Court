 #5: Course Info

#Write a program that has the user input a bunch of course ID, course name pairs.  

#For example a course ID could be "COS 2005" and the course name could be "Python Programming."  

#Then ask the user for a subject (like "COS"). #Finally, the program will display the ID and name of all the courses having that subject.

#create dictionary
user_dictionary = {}

#function to find course using ID
def find_course(user_dictionary, subject_to_find):
	while True:	
		#find subject with ID
		for courseID, course_name in user_dictionary.items():
			#show relevant courses
			if subject_to_find in courseID:
				print(f"{course_name} has {subject_to_find} ID.")
		
		#repeat?
		repeat = input("To continue, type 'y': ")		
		#don't repeat
		if repeat != "y":
			break

while True:
	#get a code
	code = input("Enter a course ID with 3 letters and 4 numbers (example: ABC 1234): ")
	#get a class_name
	class_name = input("Enter a class: ")
	#add the new code and class to dictionary
	user_dictionary[code] = class_name
	#repeat
	repeat = input("Would you like to search, type 'y': ")		
	#don't repeat
	if repeat != "y":
		break

#get ID from user
subject = input("To find a course, enter an ID with 3 letters: (example: ABC)")
#search for user ID
find_course(user_dictionary, subject)