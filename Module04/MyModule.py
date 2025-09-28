# Assignment module 4 - Task 01
# Revise the script you wrote for Task 3: Write a script to find the minimal 
# and maximal in the Assignment of Module 03, transform it into three functions
# get_a_list_of_numbers(),find_min(list_of_numbers) & find_max(list_of_numbers)

# This python file includes a function which get a list a list of numbers
# returning min/max with two more min/max functions

def get_a_list_of_numbers():
    """Asking the user to input a list of numbers, process is ended when input=end"""
    numbers = [] # Initiating an empty numbers list where to be stored the numbers
                 # the user is going to enter

    while True: # Starting a loop that will continue meanwhile user enters valid numbers
                # or decides to end
            number_input = input("Please enter a number or type 'end' to finish:")

            if number_input == 'end': # Breaking the loop when user enters end to finish
                    print(f"The list of numbers is: {numbers}")
                    return numbers
            else:
                try:
                    numbers.append(float(number_input))
                except ValueError:
                    print(f"The input entered {number_input} wasn't valid, it has been jumped")
    return numbers

def find_min(numbers):
    """Defining function for finding the minimun from the list of numbers"""
    if len(numbers) > 0: # Tells how to proceed when the numbers list is not empty
        minimal = numbers[0]
        # Initiating minimal to the first number entered in the list
        for number in numbers:
        # Iterating through the number list checking if it is less/greater
                # than current minimal/maximal, and then it updates depending on
                # the comparison results
            if number < minimal:
                minimal = number
        print(f"The minimal number is: {minimal}")        
        return minimal
    else:
        print(f"The list is empty.")
        return None

def find_max(numbers):
    """Defining function for finding the maximun from the list of numbers"""
    if len(numbers) > 0:
        maximal = numbers[0] # Initiating maximal to the first number entered
                             # in the list
        for number in numbers: # Iterating through the number list checking if it
                           # is less/greater
                       # than current minimal/maximal, and then it updates depending on
                       # the comparison results
            if number > maximal:
                maximal = number
        print(f"The maximal number is: {maximal}") 
        return maximal
    else:
        print(f"The list is empty.")
        return None

## Here below is the sorting code part from Module 3, not required in this Task 1
## from Module 04
		
#	print(f"The list of numbers is: {numbers}") # Printing the list of numbers
#	print(f"The minimal number entered is: {minimal}")
#	print(f"The maximal number entered is: {maximal}")
        
#def sor# Sorting the list of numbers entered by the user
#        sort_numbers = True  

        # Implementing a sorting algorithm
#        n = len(numbers) # Getting the total number of elements within the number list
        # Storing the total number in the variable n defined   
#        for i in range(n): # Iterating n times, placing sorted at least one element for each pass             
#        for j in range(0, n - i - 1): # Iteraring through the unsorted elements of the list
#                if sort_numbers:
#                    if numbers[j] > numbers[j + 1]:
#                        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

#        print(f"The sorted list of numbers is: {numbers}")
#else: # Printing message when there were no numbers entered
#    print("No numbers were entered.")