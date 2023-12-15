import pandas as pd
import numpy as np

# 5.15: Creating a dictionary manually
my_dict = {'Species': [], 'obs': [], 'flower_part': [], 'Length': [], 'Width': []}

# 8_2: Reading CSV data into a DataFrame using pandas
while True: 
    csv_file_path = input('Please enter a valid pathway to a valid csv file: ')

    try:
        with open(csv_file_path, 'r'):
            pass
    except FileNotFoundError as e:
        print(f"Your csv file does not exist.{e}")

    if csv_file_path.endswith('.csv'):
        df = pd.read_csv(csv_file_path)
        print(df)
        break
    else:
        print("Please provide a valid csv file: ")

# 5.17: Accessing the keys of a dictionary
keys = my_dict.keys()
print(keys)

# 5.19: Updating values in a dictionary programmatically
for index, row in df.iterrows():
    my_dict['Species'].append(row['Species'])
    my_dict['obs'].append(row['obs'])
    my_dict['flower_part'].append(row['flower_part'])
    my_dict['Length'].append(row['Length'])
    my_dict['Width'].append(row['Width'])

# 5.18: Iterating through the items of a dictionary to access both keys and values
for key, value in my_dict.items():
    print(f"HERE ARE YOUR KEY VALUE PAIRS --> Key: {key}, Value: {value}")

user_question = input("Type yes to see the length values square, type no to move on: ")
if user_question == 'yes':
    # 8.1: Using NumPy for vectorized computation
    df['new_lengths'] = np.square(df['Length'])
    print("Heres a list of values below that has the squared values of the original lengths: {}".format(df['new_lengths']))
else:
    print("We will move on :(")


# 8.3: Using pandas to get a subset of a DataFrame using a boolean and 8.4: Writing data to CSV using pandas
subset_df = df[df['flower_part'] == 'Sepal']
print(f"Here is a subset dataframe that shows you all the flower parts that were specifcally sepals {subset_df}.")

while True: 
    output_csv_path = input('Provide a pathway to a csv file to put your new subset dataframe in: ')

    try:
        with open(output_csv_path, 'r'):
            pass
    except FileNotFoundError as e:
        print(f"Your csv file does not exist.{e}")

    if output_csv_path.endswith('.csv'):
        subset_df.to_csv(output_csv_path, index=False)
        # 7.2: Using a backslash to escape a special character
        print("Congradulations, checkout your new dataframe's on the csv file you provided which will also contain those squared length values. : \\)")
        break
    else:
        # 7.3: Using a raw string to avoid needing to use backslashes
        print(r"Please provide a valid csv file: \\")


# 7.4: Using a regular expression to check if a string matches a pattern
import re

while True:
    pattern = r'\d{3}-\d{2}-\d{4}'  
    social_security = input('Please provide a social security number in this format with numbers(abc-ab-abcd). Do not use spaces!: ')
    if re.match(pattern, social_security):
        print("Pattern matched!")
        break
    else:
        print("Please provide a valid social security.")

# 7.5: Using regular expressions with groupings to extract or change parts of a string
while True:
    new_social_security = input("If you want to input a new social security type a new one if not just type no: ")

    if new_social_security == 'no':
        match_result = re.search(r'(\d+)-(\d+)-(\d+)', social_security)
        if match_result:
            groups = match_result.groups()
            modified_string = f"{int(groups[0])+4}-{int(groups[1])+5}-{int(groups[2])+1}"
            print("Heres your original modified social security number: " ,modified_string)
            break
    else:
        new_match_result = re.search(r'(\d+)-(\d+)-(\d+)', new_social_security)
        if new_match_result:
            groups = new_match_result.groups()
            modified_string = f"{int(groups[0])+4}-{int(groups[1])+5}-{int(groups[2])+1}"
            print("Heres your new modified social security number: " ,modified_string)
            break
        else:
            print("Please provide a valid social sceurity number in this exact format: 123-45-4567")

# 6.8: Making appropriate use of another person’s license when incorporating their software
# (Note: Ensure you comply with the license terms of any third-party software you use)

