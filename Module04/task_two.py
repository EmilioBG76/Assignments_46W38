# Task 2: Implement a word counter for text files
# You will write a Python script task_two.py, in which you implement a function 
# called count_words(filename) which takes the name of a text file, and returns 
# the number of words in it. You should do the following:
# 1st.- Write the count_words(filename) in the task_two.py script.
# 2nd.- write also code in the same script that use this function for a text file, 
# for example the file The_Zen_of_Python.txt which you can also download from 
# the course website, i.e., here: 
# #https://learn.inside.dtu.dk/d2l/le/lessons/261112/units/1067114
# 3rd.- print out the file name and number of words in a properly formatted f-string.

# When you implementing the function, you must consider the following:
# you function needs to handle the case when the file (filename) doesn't exist 
# or the user provides the wrong name. Use try and except to catch the possible 
# FileNotFoundError, and if the file can't be found, your function should just return None.
# the punctuations should't be taken into account, thus consider removing the 
# punctuations first. You can easily find out how to do this from the internet, 
# for example here:
# https://www.geeksforgeeks.org/python/python-remove-punctuation-from-string/

#the built-in function split() for strings will be useful, 
# you can find its usage here:
# https://docs.python.org/3/library/stdtypes.html#str.split

import string

# Defining two nested functions that counts the number of words
# in a text file
def count_words(filename):
        
    def get_words_in_txt(filename):
        """This function counts amount of words included within
        a text file, punctuaction not included."""
        try:
            with open(filename) as f:
                words = f.read().translate(str.maketrans("", "", string.punctuation)).split()
            return words
        except FileNotFoundError:
            print(f'{filename} is not found, please double check it.')

    words_counter = len(get_words_in_txt(filename)) 
    return words_counter

amount_words = count_words("The_Zen_of_Python.txt")
print(f'The amount of words in "The Zen of Python" text is {amount_words} words')
             