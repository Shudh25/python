import csv
import json

output =[]

# // open input file
with open("final_corrected_data.csv","r") as f:    
    reader = csv.DictReader(f)
    
# //appending each record in list
    for records in reader:    
        output.append(records)

# // Create JSON file
with open("RecordsJson.json","w")as outfile:    
    json.dump(output,outfile,sort_keys=True, indent=4)


import requests

# // POST API
url ="http://localhost:8080/postData"

# // Reading JSON file
with open("RecordsJson.json","r")as infile:    
    indata = json.load(infile)

output =[]

# //Calling API POST method on requests one by one
for data in indata:    
    r= requests.post(url, data=data)    
    # print(r, r.text)