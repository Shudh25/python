import pandas as pd

employee_data = pd.read_csv('employee_data.csv')

manager_data = pd.read_csv('manager_data.csv')

# print(data)
# print(data.to_string())

# print(manager_data.loc[[0,1]])

# print(manager_data.head(10))
# print(manager_data.tail())

# print(manager_data.info())

merged_df = pd.merge(employee_data, manager_data, on='employee_name')

print(merged_df)



