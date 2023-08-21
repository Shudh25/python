import pandas as pd

employee_data = pd.read_csv('employee_data.csv')

manager_data = pd.read_csv('manager_data.csv')

merged_df = pd.merge(employee_data, manager_data, on='employee_name')

print(merged_df)

# merged_df.to_csv(r'export.csv', index=False)



