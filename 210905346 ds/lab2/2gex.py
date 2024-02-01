import pandas as pd

# 11. While Loop with Else
counter = 0
while counter < 5:
    print(f'Inside the loop: Counter = {counter}')
    counter += 1
else:
    print('Exited the loop.')

# 12. Print Negative Numbers in a List using While Loop
numbers_list = [11, -21, 0, 45, 66, -93]
index = 0

print('Negative Numbers:')
while index < len(numbers_list):
    if numbers_list[index] < 0:
        print(numbers_list[index])
    index += 1

# 13. Convert Dictionary to DataFrame and Add a New Column
students_data = {'Name': ['Alice', 'Bob', 'Charlie'],
                 'Height': [160, 175, 162],
                 'Qualification': ['Bachelor', 'Master', 'PhD']}

# a) Convert Dictionary to DataFrame
df_students = pd.DataFrame(students_data)

# b) Declare a list for the new column 'Address'
address_list = ['123 Main St', '456 Oak Ave', '789 Pine Rd']

# c) Add 'Address' column to DataFrame
df_students['Address'] = address_list

# Display the DataFrame
print("\nDataFrame with 'Address' Column:")
print(df_students)
