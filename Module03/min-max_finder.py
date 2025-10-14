# Assignment module 3 - Task 03
# Write a script to find the minimal and maximal

numbers = [] # Initiating an empty number list where to be stored the numbers the user is going to enter

while True: # Starting a loop that will continue meanwhile user enters valid numbers or decides to end
	number_input = input("Please enter a number or type end to finish):")
	
	if number_input == 'end': #Breaking the loop when user enters end to finish
		    break

	else:
		        current_number = float(number_input)
		        numbers.append(current_number)

if numbers: # Tells how to proceed when the numbers list is not empty 
	minimal = numbers[0] # Initiating minimal to the first number entered in the list
	maximal = numbers[0] # Initiating maximal to the first number entered in the list

	for number in numbers: # Iterating through the number list checking if it is less/greater 
				       # than current minimal/maximal, and then it updates depending on 
				       # the comparison results
		if number < minimal:
			    minimal = number

		elif number > maximal:
			    maximal = number
		
	print(f"The list of numbers is: {numbers}") # Printing the list of numbers
	print(f"The minimal number entered is: {minimal}")
	print(f"The maximal number entered is: {maximal}")

else: # Printing message when there were no numbers entered
    print("No numbers were entered.")
