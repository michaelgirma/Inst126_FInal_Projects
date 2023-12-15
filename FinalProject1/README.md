#THIS WHOLE FILE COVERS ITEM 6.1 OF MY CHECKLIST
# Word List Processor

#    Description
1. This Python script allows users to read and process a text file containing words. Users can create a new list containing only words or remove non-words from the original list. Then they can choose to push their results to an already exisiting file or create a new file to append their results to. 

# Prerequisites
1. You need Python 3 downloaded on your local device

# Getting Started
A. JUST MENTIONING THAT THIS SECTION HERE COVERS ITEM 6.5 OF MY CHECKLIST
1. create a copy of this file or just save the file somewhere on your computer, I would recommend a folder in your desktop
2. Make sure you have Python installed.
3. Run the script:
    1. Find the pathway to the folder your file is in 
    2. Open you terminal and type cd and paste the pathway right after 
    3. then type this exactly after if there are no errors: python FinalProject_1.py
4. After running the script, you will be prompted to provide the path to a text file (ending with .txt). The script will read the file, convert all letters to uppercase, and split the contents into a list of words.
5. Your first Option:
    1. Create a New List with Only Words:
         Type new when prompted. The script will iterate through the words, creating a new list containing only valid words. The resulting list will be displayed.

    2. Remove Non-Words from the Original List
         Choose option remove when prompted. The script will iteratively remove non-words from the original list. The modified list will be displayed.

6. After that your results will be displayed based on your choice and then you will have the choice after that to write your results to a file or append the results to a file

7. After you make that choice, that would mark the end of this program 

# File Structure
    1. FinalProject_1.py: The main Python script.
    2. sample_text_file.txt: An example text file for testing the script. Just create one and type whatever you want in there and let the script do the rest. 

# Note
    1. Make sure to provide the correct file path and type 'new' or 'remove' when prompted.
    2. The script is case-insensitive when checking user input.

# Contributing
    1. Feel free to contribute by opening issues or submitting pull requests. Your feedback and improvements are welcome!

# License
    1. This project is licensed under the MIT License.