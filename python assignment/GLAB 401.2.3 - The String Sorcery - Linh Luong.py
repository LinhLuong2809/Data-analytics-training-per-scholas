# task 1: Enter the realm of strings
# The Magical Reversal

# Task 2: Embrace the String Sorcery
# TO DO 1
print(f"Task 2: Embrace the String Sorcery")
text = input("Enter a word or phrase: ")
reversed_text = text[::-1]
print("The reversed version is:", reversed_text)

print()

# Task 3: Unleash Your String Sorcery
# TO DO 2
# 1 The Word Alchemist: Create a program that counts the number of occurrences of each word in a given text. Use string manipulation techniques to split the text into words and update a dictionary with the word counts.
print("Task 3: Unleash Your String Sorcery")
print()
print("The World Alchemist")

def WordAlchemist(word):
    word_counts = {} # create dictionary to store word : count
    word_lower = word.lower() # tranforms the text message to lower case for case sensitive when counting the repeating word
    words = word_lower.split() # split each word in the string in to an array of each seperated word
    
    for word in  words: # for loop to iterate through the words and update dictionary
        word = word.strip(".,!?()[]{}\"'") # remove punctuation if existed in each word
        
        if word in word_counts: # if the word existed in dictionary already increase count by 1
            word_counts[word] +=1
        else:
            word_counts[word] = 1 # if the word not exist in dictionary, put it in and give count by 1
        
    print(word_counts) # out put the results
    
# testing 
text = input("Enter your message: ")
WordAlchemist(text)

# 2. The Cipher Master: Implement a simple Caesar cipher encryption and decryption program. Prompt the user to enter a message and a shift value. Apply the shift to each character in the message to create an encrypted version, and vice-versa for decryption.
print()
print("The Cipher Master")
def CipherMaster(text, shift):
    alpha = "A B D E F G H I J K L M N O P Q R S T U V W X Y Z" # create a list of alphabet
    alph_lower = alpha.lower().split() # split alphabet to a another list with lower case
    alph_upper = alpha.split() # split alphabet to a list with upper case
    text_list = text.split() # split the input message into a list of words
    newtext = "" # create new varibale with empty string to store decipher message
    
    for word in text_list: # loop to traverse the message list 
        for char in word: # loop to traverse each word in the message list
            if char in alph_lower: # condition if character in the word is lower case
                index = alph_lower.index(char) + shift # calculate index of that word in the list then add shift value to the index
                if index < len(alph_lower): # condition if index is smaller than the list length
                    newtext += alph_lower[index] # add the character into newtext message
                else: # condition if index is larger than the list length
                    index -= len(alph_lower) # substract the index length to get the correct index
                    newtext += alph_lower[index]
                    
            if char in alph_upper: # same code as above but check for upper case
                index = alph_upper.index(char) + shift
                if index < len(alph_upper):
                    newtext += alph_upper[index]
                else:
                    index -= len(alph_upper)
                    newtext += alph_upper[index]
        newtext += " " # add space after each word
    return newtext # return the value to the function

def decryptCipherMaster(text, shift): # decrypt encryption message with shift value.
    return CipherMaster(text, -shift)   # call encryption fucnction but reverse the shift value


# testing code        
text = input("Enter your message to encrypt: ")
shift = input("Enter your shift value: ")
cipher = CipherMaster(text,shift)
print("Encryption message : {}".format(cipher))
text = input("Enter your encrypted message:")
decipher = decryptCipherMaster(text, shift)
print("Real message : {}".format(decipher))


# 3. The Anagram Conjurer: Write a program that prompts the user to enter two words or phrases. Determine if they are anagrams (contain the same characters in different orders) and reveal the secret connection between them.
print()
print("The Anagram Conjurer")
def anagrams(word1, word2):
    # delete space and change all words to lower case for comparision.
    word1_sort = ''.join(word1.split()).lower()
    word2_sort = ''.join(word2.split()).lower()
    
    return sorted(word1_sort) == sorted(word2_sort) # return boolean true or false after comparing two words to the function

def revealConnection(word1, word2):
    if anagrams(word1,word2):
        print(f"{word1} and {word2} are anagrams!")
    else:
        print(f"{word1} and {word2} are not anagrams!")

# Testing 
word1 = input("Enter your first word or phrase: ")
word2 = input("Enter your second word or phrase: ")
anagrams(word1,word2)
revealConnection(word1, word2)