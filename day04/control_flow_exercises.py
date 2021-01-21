import random
import re


# exercise 1
def guessing_game():
	user_input = int(input("Guess a number between 1 and 9 "))
	random_number = random.randint(1,9)
	if user_input == random_number:
		print("You guessed right!")
		print(f"The random number was {random_number}")
	else:
		print("Try again!")
		print(f"The random number was {random_number}")
		guessing_game()


#exercise 2
def password_checker():
	print("Please create a password \n\
	Password must contain \n\
	*At least 1 letter \n\
	*At least 1 number between 0 and 9 \n\
	*At least 1 special character ($#@) \n\
	*Have a minimum length of 6 characters, and max of 16 characters\n")

	password = input("Please create a password...  ")
	flag_check = 0

	if not len(password) >= 6 and len(password) <= 16: 
		print("Your password must be between 6 and 16 characters")
		flag_check = 1
	if not re.search(r"[a-zA-Z]", password):
		print("Password must contain atleast 1 letter")	
		flag_check = 1
	if not re.search(r"[0-9]", password):
		print("Password must contain atleast 1 number")
		flag_check = 1
	if not re.search(r"[$#@]", password):
		print("Password must contain atleast one of the following characters: $, #, and/or @")
		flag_check = 1
	else:
		print("Password valid!")

	if flag_check == 1:
		print("Create a password matching all parameters, try again.")
		print("\n")
		password_checker()

#exercise 3
def whois_oldest():
	age_dict = {"person1": 0, "person2": 0, "person3": 0}
	person1 = int(input("Person one, how old are you? "))
	age_dict.update({"person1": person1})
	print(age_dict)
	person2 = int(input("Person two, how old are you? "))
	age_dict.update({"person2": person2})
	print(age_dict)
	person3 = int(input("Person three, how old are you? "))
	age_dict.update({"person3": person3})
	print(age_dict)

	age_max = max(age_dict, key=age_dict.get)
	age_min = min(age_dict, key=age_dict.get)

	print(f"{age_max} is the oldest")
	print(f"{age_min} is the youngest")

	if age_max == age_min:
		print("Everyone is the same age, how about that")


#exercise 4
def exam_attendance():
	total_num_classes = int(input("How many classes were held? "))
	num_classes_attended = int(input("How many classes have you attended? Be honest! "))

	attendance = (num_classes_attended / total_num_classes) * 100
	print(f"Your were in class {round(attendance)}% of the time")

	if round(attendance) >= 75:
		print("Congratulations, you are eligible take the exam!")
	else:
		print("You should shape up and go to class, unless you want to end up like me...")
 

#exercise 5
def integer_n():
	user_number = int(input("Pick a number "))
	if user_number % 2 != 0:
		print("Weird.")
	elif user_number % 2 == 0 and range(2,5):
		print("Not Weird.")
	elif user_number % 2 == 0 and range(6,20):
		print("Weird.")
	elif user_number % 2 == 0 and user_number > 20:
		print("Not Weird.")


def function_selector():
	user_input = input("Type: \n 1 for exercise 1 \n 2 for exercise 2 \n 3 for exercise 3 \n 4 for exercise 4 \n 5 for exercise 5 \n ")
	if user_input == "1":
		guessing_game()
	elif user_input == "2":
		password_checker()
	elif user_input == "3":
		whois_oldest()
	elif user_input == "4":
		exam_attendance()
	elif user_input == "5":
		integer_n()
	
		
function_selector()