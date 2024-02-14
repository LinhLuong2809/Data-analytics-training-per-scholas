# Task 1: The Factorial Factory
'''
develop a program using a while loop to calculate the factorial of a given number. Ensure the program handles edge cases such as zero and negative numbers gracefully.

'''

print("Task 1: The Factorial Factory")
print()
factorial = 1
while True:
    num = int(input("Enter factorial number: "))
    value = num
    if num < 0:
        print("factorial cannot be negative number. Please choose again.")
    elif num == 0:
        break
    else:
        break

while num > 0:
    factorial *=num
    num -= 1

print(f"factorial number of {value} is {factorial}")


# Task 2: The Fibonacci Alchemist
'''
employing loops to generate Fibonacci sequences. Use both for and while loops to generate the fibonacci series.

'''

print()
print("Task 2: The Fibonacci Alchemist")
while True:
    n = int(input("Please enter fibonacci sequences number: "))
    if n <=0:
        print("Input should be a positive number.")
    else:
        break
    
fib = [0,1] # original fibonacci sequences for number 1

if n > 1 :
    while len(fib) <= n:                # while loop to generate 
        fib.append(fib[-1] + fib[-2])   # add the sum of two precending number to fib list
        
    # for i in range(1, n):             # for loop to generate, want to test then comment out # while loop code and delete # on for loop code    
    #    fib.append(fib[-1] + fib[-2])  

print("Fibonacci sequences: ")
print(fib)



# Task 3: The Prime Hunter
'''
using loops to identify prime numbers within a specified range. Use both for loop and while loop to identify the prime numbers. 

'''

print()
print("Task 3: The Prime Hunter")

def prime(num): # prime function to check if a passing number is prime or not by return a boolean false for not prime and true for prime
    if num <=1:
        return False
    elif num ==2:
        return True
    elif num % 2 == 0:
        return False
    else:
        
        # for loop
        for i in range (3, int(num/2) + 1): #for loop check for the range between 3 and n/2 number if any num divide any number in this range then it's not prime number
            if num % i == 0:
                return False
        return True

'''    
        # while loop
        count = 3
        while count < (num/2) + 1:
            if num % count == 0:
                return False
            count+=1
        return True
'''      
       
def primeRange(start, end):
    primeNumber = []
    for num in range(start, end +1):
        if prime(num):
            primeNumber.append(num)
    
    return primeNumber
    
# Test
start = int(input("Please enter the start of the range: "))
end = int(input("Please enter the end of the range: "))
primeNumber = primeRange(start, end)

if len(primeNumber) >0:
    print(f"List of prime number in range ({start},{end}): {primeNumber}")
else:
    print(f"There's no prime number in range ({start},{end})")
    
          

# Task 4: The Palindrome Detective
'''
Develop a Python program utilizing loops to check whether a given string is a palindrome. Consider edge cases and implement the program to handle various scenarios gracefully.

'''

print()
print("Task 4: The Palindrome Detective")

def palindrome(text):
    arrText = ""
    sortText = "".join(text.split()).lower()
    count = -1
    while count > -len(sortText) - 1:
        arrText += sortText[count]
        count -= 1
    return arrText == text

text = input("Enter your phrases or sentences to check for palindrome: ")

if palindrome(text):
    print(f"'{text}' is a palindrome!")
else:  
    print(f"'{text}' is not a palindrome!")


   
# Task 5: The Multiplication Maestro

print()
print("Task 5: The Multiplication Maestro")


'''
build a program that displays the multiplication table for a given number using loops. Ensure the output is well-formatted and easy to read. 

'''

number = int(input("Enter the number for multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
    
