# Task 1: The String Sculptor
'''
Create a Python program that manipulates strings by performing the following tasks:

TO DOs - 1:
Define a string variable with your favorite quote.
Use string concatenation to add a message about Python.
Implement string slicing to extract and print specific portions of the quote.
Utilize string methods to convert the entire quote to uppercase.
Print the results.

'''

print("Task 1: The String Sculptor")
# quote = "You must be the change you wish to see in the world."
quote = input("Enter your quote: ")
print("Your quote: {}".format(quote))

addquote = quote + " " + input("Enter addition message about Python to your quote: ")
print(f"Your addition quote: {addquote}")

## quote += " Python is an interpreted, high-level, general-purpose programming language."

def slice(quote, root, end): # slice function for quote
    subquote = quote[root:end]
    print(subquote)

begin = int(input(f"Enter the number begin portion of the quote you want to slice (0 - {(len(addquote))}): "))
end = int(input(f"Enter the number end portion of the quote you want to slice (0 - {(len(addquote))}): "))
print()
print("slice quote: ")
slice(addquote,begin,end)
print()
print("Upper case for the quote: ")
print(addquote.upper())


# Task 2: The Format Magician
'''
Develop a Python program focusing on string formatting and interpolation. Perform the following actions:

TO DOs - 2:

Define variables for a person's name, age, and profession.
Use string formatting to create a sentence introducing the person.
Print the results.

'''

print()
print("Task 2: The Format Magician")
# ask user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
profession = input("Enter your profession: ")

def introduction(name,age,profession):
    print(f"Hello my name is {name}. I am {age} years old and I am a {profession}. Nice to meet you!")
    
introduction(name,age,profession)
    


# Task 3: The Palindrome Prophet
'''
Craft a Python program that checks whether a given string is a palindrome. Follow these steps:

TO DOs - 3:

Define a function that checks if a given string is a palindrome.
Test the function with various strings, including phrases and sentences.
Handle edge cases, such as ignoring spaces and punctuation.
Print the results.

'''

print()
print("Task 3: The Palindrome Prophet")

def palindrome(text):
    sortText = "".join(text.split()).lower()
    
    return text == sortText[::-1]

text = input("Enter your phrases or sentences to check for palindrome: ")

if palindrome(text):
    print(f"'{text}' is a palindrome!")
else:  
    print(f"'{text}' is not a palindrome!")

# Task 4: The Word Wrangler
'''
Build a Python program that analyzes a given sentence and provides insights into the word composition. Perform the following actions:

TO DOs - 4:

Define a sentence variable with a meaningful sentence.
Use string methods to count the number of words in the sentence.
Identify and print the longest word in the sentence.
Capitalize the first letter of each word in the sentence.

'''
print()
print("Task 4: The Word Wrangler")
sentence = input("Enter your sentence: ")

sentenceList = sentence.split() # plit the sentence into list of each word

longest = [] # make an empty list to store longest words

max_length = max(len(word) for word in sentenceList) # finding the max length of a word in the list
        
for word in sentenceList: # loops through the list and find the word that match with max length and store it into longest list
    if len(word) == max_length:
        longest.append(word)

# output tge result        
print(f"The number of words in sentence is : {len(sentenceList)} words")
print(f"The longest word/s: {longest}")
print("Capitalized first letter of each words: ")
print(sentence.title())
        
# Task 5: The Email Composer

'''
Develop a Python program for composing personalized email messages using string formatting. Perform the following tasks:

TO DOs - 5:

Define variables for recipient name, sender name, and a personalized message.
Use string formatting to compose an email message.
Experiment with including dynamic information, such as the current date.
Print the results.

'''
print()
print("# Task 5: The Email Composer")
import datetime

# ask for input
receiName = input("Enter recipient name: ")
senderName = input("Enter sender name: ")
message = input("Enter your personalized message: ")

print()
def composeEmail(recipient, sender, message): # email pattern
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(current_date)
    print(f"Hello, {recipient}.")
    print(f"My name is {sender}. I want to write you this email because: ")
    print(message)
    print()
    print("Sincerely,")
    print(sender)

# output result    
composeEmail(receiName,senderName,message) 
