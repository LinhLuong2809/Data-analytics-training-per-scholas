# Task 1: The Dictionary Creator
'''
Create a Python program that explores the creation and manipulation of dictionaries by performing the following tasks:

TO DOs - 1:
Define an empty dictionary and populate it with at least five key-value pairs.
Use dictionary methods to add, remove, and update key-value pairs.
Print the final state of the dictionary.

'''
print("Task 1: The Dictionary Creator")
print()
# Test fucntion
def test(person):
    print(person)
    print()
    
personInfo = {"name" : "John", "Age" : 24,"Gender" : "Male", "Occupation" : "Teacher", "Status" : "Single"} # Define an empty dictionary and populate it with at least five key-value pairs.
test(personInfo)

# Add new key and value
personInfo["Income"] = 100000
test(personInfo)

# Remove key
del(personInfo["Status"])
test(personInfo)

# update key-value pairs
personInfo.update({"name" : "Linh"})
test(personInfo)

# Task 2: The Dictionary Detective
'''
Build a Python program that analyzes the frequency of words in a given text using a dictionary. Perform the following tasks:

TO DOs - 2:

Define a dictionary representing information about a person (e.g., name, age, profession).
Utilize dictionary methods to retrieve, update, and manipulate the information.

'''

print("Task 2: The Dictionary Detective")
print()
person = {"name" : "Linh", "Gender" : "male", "age" : 33, "Occupation" : "Chef"}
print("Person's info: {}".format(person))
print()
# print out person name
print(f"this person name is: {person.get("name")}")

# print out person gender
print(f"this person's gender is: {person.get("Gender")}")
print()
# update adding income for this person
person["Income"] = 125000
# update change person's age
person["age"] = 20
# update change person's Gender
person.update({"Gender" : "Female"})
# Check person full info
test(person)

# Task 3: The Word Frequency Analyzer
'''
Build a Python program that analyzes the frequency of words in a given text using a dictionary. Perform the following tasks:

TO DOs - 3:
Define a text variable containing a paragraph or sentence.
Use a dictionary to count the frequency of each word in the text.
Print the word frequencies in a readable format.

'''
print("Task 3: The Word Frequency Analyzer")
print()

para = "The bush began to shake. Brad couldn't see what was causing it to shake, but he didn't care. he had a pretty good idea about what was going on and what was happening. He was so confident that he approached the bush carefree and with a smile on his face. That all changed the instant he realized what was actually behind the bush."
print("Paragraph: ")
print(para)
print()
para_list = para.lower().split()

my_dict = {}

for word in para_list:
    if word not in my_dict:
        my_dict[word] = 1
    else:
        my_dict[word] +=1

print("The word and its frequencies: ")
for word, count in my_dict.items():
    if(my_dict.get(word) == 1):
        print(f"'{word}' appears 1 time.")
    else:
         print(f"'{word}' appears {my_dict.get(word)} times.")


# Task 4: The Phone Book Manager
'''
Develop a Python program that simulates a phone book using a dictionary. Perform the following actions:

TO DOs - 4:
Define a dictionary representing a phone book with names and phone numbers.
Implement functions to add, remove, and lookup entries in the phone book.

'''
phoneBook = {'Jasmin Schwartz': '(805)991-6231', 'Patricia Baker': '(359)562-9380', 'Sheila Bean': '(551)500-9123', 'Andrew Martinez': '(852)384-7493', 'Jessica Mills': '(413)462-1435', 'Ashley Miller': '(918)240-9255', 'Jessica Brown': '(666)954-3553', 'Mark Phillips': '(850)862-9885', 'Kristen Anthony': '(242)424-3463', 'Jamie Martin': '(975)757-3815', 'Monica Anderson': '(571)933-5936', 'Michael Mccann': '(365)632-6030'}

def add(phonebook, name, phone):
    if name not in phonebook:
        phonebook[name] = phone
        print("new info added to phonebook")
        print()
    else:
        print("Can't add existed name please use update.")
        
def view(phonebook):
    print("Phone Book: ")
    for k,v in phonebook.items():
        print(f"{k} : {v}")
    print()

def remove(phonebook, name):
    del(phonebook[name])
    print(f"Remove {name} from phonebook.")
    print()
    
def lookup(phonebook, name):
    print(f"Phone number for {name} is: {phonebook.get(name)}")
    
# Test

add(phoneBook, "Linh Luong", "(337)342-3123")
view(phoneBook)

remove(phoneBook, "Jasmin Schwartz")
view(phoneBook)

lookup(phoneBook, "Linh Luong")