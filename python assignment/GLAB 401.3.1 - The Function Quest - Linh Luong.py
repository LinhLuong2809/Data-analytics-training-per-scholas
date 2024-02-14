# Task 1: Enter the Realm of Functions
# Task 2: Embark on the Function Quest
# The Mighty Calculator
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

result = add_numbers(5, 3)
print("The sum is:", result)

result = subtract_numbers(10, 4)
print("The difference is:", result)

result = multiply_numbers(6, 2)
print("The product is:", result)

result = divide_numbers(15, 0)
print("The quotient is:", result)

# Task 3: Conquer Coding Challenges
print()
print("Task 3: Conquer Coding Challenges")

'''
The Quest for Fibonacci: Write a recursive function to calculate the Fibonacci sequence. Prompt the user to enter a number and display the corresponding Fibonacci number.

'''

print("The Quest for Fibonacci")
def fibonacci(n):
    if n <=0: # case 0 or negative
        return "Input should be a positive integer."
    elif n ==1: # case = 1 
        return [0]
    elif n == 2: # case = 2
        return [0,1]
    else: 
        fib = fibonacci(n-1) # recursive call function with value -1
        fib.append(fib[-1] + fib[-2]) # add fiboncacci number to the list fib by sum the two precending number
        return fib

# test output
number = int(input("Please enter the Fibonacci sequence number: "))
fib = fibonacci(number)
print("Fibonacci sequence: ")
print(fib)



'''
The Cryptic Decoder: Design a function that decodes a message encrypted using a simple substitution cipher. Use a dictionary to map each encrypted letter to its corresponding plaintext value.

'''

print()
print("The Cryptic Decoder")
def encrypt(message):
    #cipher dictionary to store pair of characters and their cipher
    cipher_map = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
                  'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
                  'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
                  'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
                  'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b',
                  'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G',
                  'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L',
                  'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q',
                  'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V',
                  'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'}
    
    encrypted_message = "" # variable to store encrypted message
    
    for char in message: # loop through each character in the message
        encrypted_message += cipher_map.get(char,char) # use cipher map to encryp message with correspondence letter
    
    return encrypted_message

message = input("Enter your message to encrypt: ")
encryptMessage = encrypt(message)
print(f"Your encrypted message is: {encryptMessage}")



'''
The Magical Validator: Create a function to validate email addresses. Prompt the user to enter an email address and determine if it is valid based on specific criteria.

'''
print()
print("The Magical Validator")

def checkEmail(email):
    atIndex = email.find('@') # check if there is @ index in email
    comIndex = email.find('.com') # check if there .com index in email
    
    if atIndex !=-1 and comIndex !=-1 and atIndex < comIndex -1: # condition index of @ and .com can't be at the begining, and make sure there is text between @ and .com
        return print("Your email is valid.")
    else:
        return print("Your email is invalid.")
    
# test output
email = input("Please enter your email: ")
checkEmail(email)

