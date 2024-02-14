# Task 1: Encoding a Python Dictionary into JSON

'''
To Dos - 1:
Write a Python program to encode the following Python dictionary into JSON and save it to an external JSON file (encoded_data.json):

'''
import json
from jsonschema import validate

print("Task 1: Encoding a Python Dictionary into JSON")

# create python dictionary
person_hobby = {"John": "eat", "Mary" : "sleep", "Daniel" : "Play", "Tony" : "sing", "Martha":"cook",
                "Barney" : "read", "Timmy" : "shower", "Nathan" : "workout"}

# write to json file
with open("encoded_data.json", 'w') as file:
    json.dump(person_hobby, file)
    
print("Json file created.")

# Task 2: Decoding a JSON String into a Python Dictionary
'''
To Dos - 2:
Write a Python program to decode the JSON data from the external JSON file (encoded_data.json) into a Python dictionary:

'''
print()
print("Task 2: Decoding a JSON String into a Python Dictionary")

# open json file in python
with open("encoded_data.json", 'r') as file:
    data = json.load(file)
    
# print out json file in python    
print("Loaded data from encoded_data.jason file: ")
print(data)

# Task 3: Validate JSON Against a Schema (Using encoded_data.json)
'''
To Dos - 3:
1. Given the encoded_data.json file, write a Python program to validate the encoded JSON data. Print a success message if the validation is successful; otherwise, catch and print the validation error.

2. Create a Python dictionary (invalid_data) representing an invalid JSON instance that does not conform to the simplified schema. Save this dictionary to a file named invalid_data.json.

3. Using the newly created invalid_data.json and the same simplified schema, write a Python program to validate the invalid JSON instance against the schema. Print a success message if the validation is successful; otherwise, catch and print the validation error.


'''
print()
print("Task 3: Validate JSON Against a Schema (Using encoded_data.json)")
# 1.
# function to check if json file is valid by loading to python, return boolean value
def  jsonCheck(jsonfile):
    try:
        json.load(jsonfile)
        return True # true if json file can load
    except Exception as e:
        return False # false if json file not load
    
# open json

with open(r"C:\Users\luong\OneDrive\Desktop\json example\schema.json", 'r') as file:
    
    check = jsonCheck(file)
    
    if check:
        print("Json file encoded_data is valid.")
    else:
        print("Json file encoded_data is invalid.")
    
# 2.

invalid_data = ["Name", "Lana", "age", "23", "status" , True, "data" , None]

with open("invalid_data.json", 'w') as file:
    json.dumps(invalid_data)

# 3. 

with open("invalid_data.json", 'r') as file:
    
    check = jsonCheck(file)
    
    if check:
        print("Json file invalid_data is valid.")
    else:
        print("Json file invalid_data is invalid.")
        
# Task 4: Extracting Information from JSON Data
'''
To Dos - 4:
Write a Python program to extract and print the "name" and "age" from the decoded JSON data:

'''

print()
print("# Task 4: Extracting Information from JSON Data")

# i use user_100.json file for this example. change the path in your computer approriately
with open(r"C:\Users\luong\OneDrive\Desktop\json example\users_100.json", 'r') as file:
    data = json.load(file)
    
    # for loop to extract name and age
    for person in data:
        for key, value in person.items():
            if key == "name":
                print(value, end = " is ")
                
            if key == "age":
                print(value, end=" years old \n")


        