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
        
        # Sorting the list of numbers entered by the user
        sort_numbers = True  

        # Implementing a sorting algorithm
        n = len(numbers) # Getting the total number of elements within the number list
                         # Storing the total number in the variable n defined   
        for i in range(n): # Iterating n times, placing sorted at least one element for each pass
                           
            for j in range(0, n - i - 1): # Iteraring through the unsorted elements of the list
                if sort_numbers:
                     if numbers[j] > numbers[j + 1]:
                        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        print(f"The sorted list of numbers is: {numbers}")
else: # Printing message when there were no numbers entered
    print("No numbers were entered.")