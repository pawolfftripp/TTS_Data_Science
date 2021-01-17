attempt = 0
answer = []
quiz_end = 0

def question_one():
	user_input1 = input("What does the following code evaluate to? \n float(10) ")
	if user_input1 == "10.0":
		print("That is correct!")
		global answer
		answer.append(user_input1)
		print(answer)
		global question_flag
		question_flag = 1
		global score
		score = 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_one()
		else:
			attempt = 0
			question_two()


 
def question_two():
	user_input2 = input("What does the following code evaluate to? \n int(50.3) ")
	if user_input2 == "50":
		print("That is correct!")
		global answer
		answer.append(user_input2)
		print(answer)
		global question_flag
		question_flag = 2
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_two()
		else:
			attempt = 0
			question_three()

def question_three():
	user_input3 = input("What python method allows for removal of an item in a list? ")
	if user_input3 == "pop()":
		print("That is correct!")
		global answer
		answer.append(user_input3)
		print(answer)
		global question_flag
		question_flag = 3
		global score
		score += 1	
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_three()
		else:
			attempt = 0
			question_four()	

def question_four():
	user_input4 = input("Is a tuple immutable? y/n ")
	if user_input4 == "y":
		print("That is correct!")
		global answer
		answer.append(user_input4)
		print(answer)
		global question_flag
		question_flag = 4
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_four()
		else:
			attempt = 0
			question_five()

def question_five():
	user_input5 = input("Is the following line of code valid? y/n \n x, y, z = 2, 12, '8' ")
	if user_input5 == "y":
		print("That is correct!")
		global answer
		answer.append(user_input5)
		print(answer) 
		global question_flag
		question_flag = 5
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_five()
		else:
			attempt = 0
			question_six()

def question_six():
	user_input6 = input("With regard question 5, what will z * x return? \n x, y, z = 2, 12, '8'")
	if user_input6 == "88":
		print("That is correct!")
		global answer
		answer.append(user_input6)
		print(answer)
		global question_flag
		question_flag = 6
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_six()
		else:
			attempt = 0
			question_seven()

def question_seven():
	user_input7 = input("'//' , '*', '|' , and '%' are all examples of ____________ ")
	if user_input7 == "operators" or user_input7 == "Operators" or user_input7 == "operator" or user_input7 == "Operator":
		print("That is correct!")
		global answer
		answer.append(user_input7)
		print(answer)
		global question_flag
		question_flag = 7
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_seven()
		else:
			attempt = 0
			question_eight()

def question_eight():
	user_input8 = input("Consider this code: \n number_list = [10, 11, 12, 13, 14, 15] \n What number will be replaced if the following code is run? number_list[3] = 7 ")
	if user_input8 == "13":
		print("That is correct!")
		global answer
		answer.append(user_input8)
		print(answer)
		global question_flag
		question_flag = 8
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_eight()
		else:
			attempt = 0
			question_nine()

def question_nine():
	user_input9 = input("What is the following code an example of? \n employees = {'emp_a': 'IT', 'emp_b': 'Finance', 'emp_c': 'advertising'} \n ")
	if user_input9 == "dictionary" or user_input9 == "Dictionary":
		print("That is correct!")
		global answer
		answer.append(user_input9)
		print(answer)
		global question_flag
		question_flag = 9
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_nine()
		else:
			attempt = 0
			question_ten()

def question_ten():
	user_input10 = input("What method is used to remove the leading and trailing whitespace in a string? \n x = '     test     ' ")
	if user_input10 == "strip()":
		print("That is correct!")
		global answer
		answer.append(user_input10)
		print(answer)
		global question_flag
		question_flag = 10
		global score
		score += 1
	else:
		print("Try again!")
		question_flag = 0
		global attempt
		attempt += 1
		if attempt <= 3:
			question_ten()
		else:
			question_flag = 10


def start_quiz():
	start = input("Are you ready to start the quiz? y/n ")
	if start == "y":
		global question_flag
		question_flag = 0
		question_stepper()
	else:
		print("give it a shot.")

def your_score():
	global score
	print(f" You scored {score} out of 10!")
	if score == 10:
		print("Great job, you got them all right!")
	elif score >= 7:
		print("Good job, review a bit more and take the quiz again!")
	elif score <= 6:
		print("Review and try again!")

def reset_attempt():
	global attempt
	attempt = 0

def question_stepper():
	question_one()
	reset_attempt()
	if question_flag == 1:
		question_two()
		reset_attempt()
	if question_flag == 2:
		question_three()
		reset_attempt()
	if question_flag == 3:
		question_four()
		reset_attempt()
	if question_flag == 4:
		question_five()
		reset_attempt()
	if question_flag == 5:
		question_six()
		reset_attempt()
	if question_flag == 6:
		question_seven()
		reset_attempt()
	if question_flag == 7:
		question_eight()
		reset_attempt()
	if question_flag == 8:
		question_nine()
		reset_attempt()
	if question_flag == 9:
		question_ten()
	if question_flag == 10:
		quiz_end = 1
		your_score()






