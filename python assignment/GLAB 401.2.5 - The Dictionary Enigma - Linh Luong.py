# Task 2: Embark on the Dictionary Enigma
# The Magical Library

library = {
    "Harry Potter": "J.K. Rowling",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "To Kill a Mockingbird": "Harper Lee"
}

print("Our magical library contains the following books:")
for book, author in library.items():
    print(f"{book} by {author}")

print("But wait! A new book has appeared!")
library["The Great Gatsby"] = "F. Scott Fitzgerald"

print("Now our library contains the following books:")
for book, author in library.items():
    print(f"{book} by {author}")

# Task 3: Unleash Your Dictionary Powers

# 1. The Quest for Translation: Create a program that acts as a translator. Use a dictionary to store words and their translations. Prompt the user to enter a word and display its translation if it exists in the dictionary.
print() 
def Translate(word):
    dictionary = {"hello": "xin chao", "buy" : "mua", "handsome" : "dep trai", "Today" : "hom nay", "tomorrow" : "ngay mai", "yesterday" : "ngay hom qua", "old" : "gia"} # set up dictionary with key and value words for translation
    
    if word in dictionary: # check if the word is in dictionary
        print(f"{word} means {dictionary[word]} in Vietnamese.") # output the translation
    else:
        print(f"Dictionary doesn't have translation for {word}") # if word not in dictionary output this result
        
#test
word = input("Enter the word for translation: ")
Translate(word)
print()

# 2. The Magic Inventory: Design a game inventory system where each item has a name and quantity. Use a dictionary to store the items and their quantities. Allow the player to add, remove, and view items in their inventory.

def addItem(inventory, item, quantity):
    newItem = {item: quantity} # create new key value variable for item and quantity
    if item in inventory: # check condition if exist in invetory
        inventory[item] += quantity # add item and quantity to existed item 
    else: 
        inventory[item] = quantity # if item not in inventory. add item with quantity
        
    print(f"You add {quantity} {item} to your inventory. ")
    print()
    
    
def viewItem(inventory):
    print("Your inventory (item) : (quantity)")
    print(inventory)
    print()
    
def removeItem(iventory, item): # this code is similar to additem function but delete the whole item instead
    if item in inventory: 
        del(inventory[item])
        print(f"You remove {item} from your inventory")
        print()
    else:
        print("item is not in inventory.")
        print()
    
    
def removeQuantity(inventory, item, quantity): # same as additem function but remove item instead
    if item in inventory:
        inventory[item] -= quantity
        print(f"You took {quantity} of {item} out of your inventory.")
        print()
    else:
        print("item is not in inventory.")
        print()
        
# Test
inventory = {}
addItem(inventory, "potion", 30)
viewItem(inventory)
addItem(inventory, "potion", 20)
viewItem(inventory)
removeQuantity(inventory, "potion", 10)
viewItem(inventory)
addItem(inventory, "antidote", 20)
viewItem(inventory)
removeItem(inventory, "potion")
viewItem(inventory)
removeItem(inventory, "potion")
removeQuantity(inventory, "potion",21)



# 3. The Cryptic Encoder: Write a program that encrypts a message using a simple substitution cipher. Use a dictionary to map each letter to its corresponding encrypted value. Decrypt the message using the reverse mapping.

def encrypt(message):
    cipher_map = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
                  'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
                  'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
                  'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
                  'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b'} # cipher map lower case for each character
    
    cipher_map_upper = {'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G',
                  'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L',
                  'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q',
                  'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V',
                  'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'} # cipher map for upper case
    
    encrypted_message = "" #variable to store encrypted message
    
    for char in message: # loop through each character in the message
        if(char.isupper()): # if upper case then add the correspondent value in cipher map to variable
            encrypted_message += cipher_map_upper.get(char,char)
        else:
            encrypted_message += cipher_map.get(char,char) # if lower case then add from lower cipher map
    
    return encrypted_message

def decrypt(message):
    cipher_map = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
                  'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
                  'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
                  'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
                  'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b',
                  'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G',
                  'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L',
                  'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q',
                  'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V',
                  'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'} # cipher map with all cases
    
    reversedMap = {} # dictionary to reverse cipher map
    
    for key, value in cipher_map.items(): # loop through cipher map to reverse the key and value and add to reversedmap
        reversedMap[value] = key
        
    decryptMessage = "" # variable to store decryption message
    
    for char in message: # loop through the encrypted message and use reverse map to decipher
      decryptMessage += reversedMap.get(char,char)
    return decryptMessage


message = input("Enter your message to encrypt: ")
encryptMessage = encrypt(message)
print(f"Your encrypted message is: {encryptMessage}")
message2 = input("Enter your encrypted message to decrypt: ")
decryptMessage = decrypt(message2)
print(f"Your decrypted message is : {decryptMessage}")