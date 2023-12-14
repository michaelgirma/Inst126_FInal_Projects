import pandas as pd
import numpy as np
import re

# 5.15: Creating a dictionary manually
my_dict = {'Name': 'John', 'Age': 25, 'City': 'New York'}

# 5.17: Accessing the keys of a dictionary
keys = my_dict.keys()

# 5.18: Iterating through the items of a dictionary to access both keys and values
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# 5.19: Updating values in a dictionary programmatically
for key in my_dict:
    if isinstance(my_dict[key], int):
        my_dict[key] += 1
    elif isinstance(my_dict[key], str):
        my_dict[key] = f"Updated_{my_dict[key]}"

# 8_1: Using NumPy for vectorized computation
my_dict['Age'] = np.square(my_dict['Age'])

# 8_2: Reading CSV data into a DataFrame using pandas
csv_file_path = 'your_data.csv'
df = pd.read_csv(csv_file_path)

# 8_3: Using pandas to get a subset of a DataFrame using a boolean
subset_df = df[df['column_name'] > 30]

# 8_4: Writing data to CSV using pandas
output_csv_path = 'output_data.csv'
subset_df.to_csv(output_csv_path, index=False)

# 7.2: Using a backslash to escape a special character
escaped_string = 'This is a string with a special character: \\'

# 7.3: Using a raw string to avoid needing to use backslashes
raw_string = r'This is a raw string with a special character: \\'

# 7.4: Using a regular expression to check if a string matches a pattern
pattern = r'\d{3}-\d{2}-\d{4}'  # Example pattern for a social security number
text_to_check = '123-45-6789'
if re.match(pattern, text_to_check):
    print("Pattern matched!")

# 7.5: Using regular expressions with groupings to extract or change parts of a string
match_result = re.search(r'(\d+)-(\d+)-(\d+)', text_to_check)
if match_result:
    groups = match_result.groups()
    modified_string = f"{groups[0]}-{groups[1]}-{int(groups[2])+1}"

# 6.8: Making appropriate use of another person’s license when incorporating their software
# (Note: Ensure you comply with the license terms of any third-party software you use)

# Now, my_dict has updated values, and a subset of the DataFrame is written to a new CSV file.
