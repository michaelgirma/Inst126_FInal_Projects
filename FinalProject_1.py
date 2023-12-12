#THE GROUP OF COMMENTS RIGHT HERE FUFILL ITEM 6.2 OFF THE CHECKLIST
# Script Overview:
# This Python script interacts with text files, processes their content, and performs various operations based on user input.

# Section 1: Input Handling
# The script prompts the user to provide a valid file pathway ending with '.txt'.
# It utilizes a loop to ensure the user enters a correct file path.

# Section 2: File Reading and Processing
# The content of the specified text file is read, converted to uppercase, and printed.
# A list of words is created by splitting the content based on whitespace.

# Section 3: Word Manipulation
# Choice 1:
# - A list of uppercase alphabets is manually created.
# - The user selects between creating a new list of words or removing non-words from the existing list.
# - The script modifies the word list accordingly.

# Choice 2:
# - The user is prompted for another valid file pathway ending with '.txt'.
# - The modified word list and new word list are joined into strings.
# - The script writes the modified word list to the new file and appends the new word list to it.

# Important Note:
# This script assumes that the user provides valid inputs and file pathways for successful execution.
# Proper error handling has been included but to not have to restart make sure you put in what it asks for exactly

# Checklist Items:
# The script addresses various checklist items, as indicated by comments throughout the code.

# End of Documentation


# a conditional to stop the loop
file_condition = False

while file_condition == False:
    #THIS TRY EXCEPT STRUCTURE BELOW HELPED ME ACCOMPLISH ITEMS 4.2 AND 4.9 OF MY CHECKLIST
    try: 
        #provide your file path way
        file_path = input("Please provide a pathway to a file that ends with .txt and actually exists: ")

        #checks if it is a file that ends with txt
        if file_path.endswith(".txt"):
            #checks to see if the txt file can open without a problem so that our except error will run if there are issue 
            with open(file_path, 'r'):
                pass

            print("File has succesfully been stored.")
            file_condition = True
        else:
            #if pathway does not end with a txt file raise this error
            raise ValueError("Please provide a file pathway that ends with a .txt file and actually exists.")
    except FileNotFoundError:
        print("This file could not be opened. Please provide a file that exists")
        file_condition = False

#Now we want to read through that file and store it on a variable 
with open(file_path, 'r') as user_input:

    #reading through the txt file and putting it in a variable 
    file_contents = user_input.read()
    uppercase_file_contents = file_contents.upper()

#should print whatever was on the txt file
#BY MAKING ALL THE LETTERS THAT WERE READ FROM THE FILE UPPERCASE, I WAS ABLE TO COMPLETE ITEM 3.11
print("This is the contents of your file: " , uppercase_file_contents)

#now we will split everything in that string based on whitespace
word_list = uppercase_file_contents.split()
#BY SPLITTING THIS STRING INTO A LIST OF WORDS I ACCOMPLISHED 7.1
print("We have created a list of each thing inbetween a space on your file: ", word_list)

#Marks the start of choice 1
#we will create a list that contains all uppercase alphabets
#THIS COVERS ITEM 5.7 ON MY CHECKLIST BECASUE IT IS A MANUALLY CREATED LIST
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#stores your response, read carefully
user_response = input("Type new if you want to make a new list with only words or type remove to remove non-words from the current list: ")

#checks if user type in the right response if not, they have to respond to the prompt again
if user_response.lower() != 'new' and user_response.lower() != 'remove':
    print("Please provide the right answer")
    user_response = input("Type NEW if you want to make a new list with only words or type REMOVE to remove non-words from the current list: ")

#if the user types in new, it will take only words and append them iteratively in a new list
elif user_response.lower() == 'new':
    new_word_list = []  
    counter = 0
    while counter < len(word_list):
        found = False
        #iterates through alphabet
        for letter in alphabet:
            if letter in word_list[counter]:#if the current letter we are on is in the current word we are on we append it to the new list
                #I AM APPENDING AN ITEM TO A LIST ITERATIVELY THROUGH THIS PIECE OF CODE WHICH CHECKES OF ITEM 5.9 AND TECHNICALLY ALSO CHECKS OF 5.8
                new_word_list.append(word_list[counter])
                found = True
                break
        if not found:
            print("Not a valid word:", word_list[counter])
        counter += 1
    print("Your new list:", new_word_list)
#if the user types in remove, it will remove anything that is not a word in the original list so all that remains is words
elif user_response.lower() == 'remove':
    counter = len(word_list) - 1 #Instead of starting from index 0 we are starting from the last index
    while counter >= 0: #now the its gonna iterate until we get to the first index in word_list
        found = False
        for letter in alphabet:
            if letter in word_list[counter]:
                found = True
                break
        if not found:
            print("Not a valid word:", word_list[counter])
            #I AM REMOVING AN ITEM TO A LIST ITERATIVELY THROUGH THIS PIECE OF CODE WHICH CHECKES OF ITEM 5.11 AND TECHNICALLY 5.10
            del word_list[counter]  
        counter -= 1
# PRINT the modified word_list
    print("Original Modified word_list:", word_list)


#Marks the start of choice 2

while True:
    choiceTwoPathWay = input("Please provide another pathway that leads to a txt file and exists: ")
    
    if choiceTwoPathWay.endswith(".txt"):
        print("New Path way stored!")
        break
    else:
        print('Please provide a pathway to a .txt file that exists.')

def writeAndApprndToFile(provided_file_path,word_list, new_word_list):
    if provided_file_path.endswith('.txt'):
        with open(provided_file_path, 'w') as new_file:
            new_file.write(word_list)
            print("List written to file successfully.")

        with open(provided_file_path, 'a') as new_file:
            new_file.write(new_word_list)
            print("List appended to file successfully.")
    else:
        print("Error: File must be a .txt file.")

string_word_list = ' '.join(word_list)
print(string_word_list)

string_new_word_list = ' '.join(new_word_list)
print(string_new_word_list)

writeAndApprndToFile(choiceTwoPathWay, string_word_list, string_new_word_list)