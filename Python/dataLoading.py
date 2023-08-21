import pandas as pd
from datetime import datetime
from datetime import timedelta

employee_data = pd.read_csv('employee_data.csv')
# print(employee_data)

manager_data = pd.read_csv('manager_data.csv')
# print(manager_data)

merged_data = pd.merge(employee_data, manager_data, on='employee_name')
# print(manager_data)

# CONVERTING DATA FOR DATABASE

#increment variable
i = 0

while i < len(merged_data):

    toDate = merged_data.loc[i,"leave_dates"]
    duration = merged_data.loc[i,"leave_duration"]

    # taking input as the date
    Begindatestring = toDate
    
    # carry out conversion between string 
    # to datetime object
    Begindate = datetime.strptime(Begindatestring, "%m/%d/%Y")
    
    # print begin date
    # print("Beginning date")
    # print(Begindate)
    
    # calculating end date by adding 10 days
    Enddate = Begindate + timedelta(days=duration)
    
    # Formating date
    formatedStartdate = Begindate.strftime("%Y-%m-%d")
    formatedEnddate = Enddate.strftime("%Y-%m-%d")
    # print("date :",formatedEnddate)	

    merged_data.loc[i,"leave_dates"] = formatedStartdate
    merged_data.loc[i,"leave_duration"] = formatedEnddate

    i += 1
#END WHILE

# Correcting headers of Data
correct_headers = merged_data.copy()
correct_headers.rename(columns={'leave_dates': 'start_leave_date','leave_duration': 'to_leave_date'}, inplace=True)

# EXPORT FINAL DATA CSV
# merged_data.to_csv('final_data.csv', index=False)
correct_headers.to_csv(r'final_corrected_data.csv', index=False,header=True)


