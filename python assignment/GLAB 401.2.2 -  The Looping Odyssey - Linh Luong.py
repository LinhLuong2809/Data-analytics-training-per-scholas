# Task 1: Set Foot in the Land of Loops
# Task 2: Embark on the Looping Journey
# The Enchanted Countdown
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!")
print()

# Task 3: Conquer Loopy Challenges
'''
1. The Treasure Hunt: Write a program that prompts the user to guess a number between 1 and 100. Use a while loop to keep the user guessing until they find the correct number. Provide hints along the way to guide their quest for the hidden treasure.

'''
print("The Treasure Hunt")
count = 0
while count < 1 or count > 100:
    if count < 1 or count > 100:
        print("Please enter a number between 1 and 100")
    count = int(input("How many steps to walk to the treasure (1 - 100)? "))
    
    
    while count >= 1 and count <= 100:
        if count == 50:
            print("You found the treasure!")
            break
        
    
        if count > 50 and count < 60:
            print("You walk a little too far away.")
            count = int(input("How many steps to walk to the treasure (1 - 100)? "))
        
        if count >= 60:
            print("You walk too far away.")
            count = int(input("How many steps to walk to the treasure (1 - 100)? "))
        
        if count < 50 and count > 40:
            print("You are almost there! need more steps")
            count = int(input("How many steps to walk to the treasure (1 - 100)? "))
        
        if count <= 40 :
            print("You are so far away! need many more steps")
            count = int(input("How many steps to walk to the treasure (1 - 100)? "))
    
    

    

'''

2. The Magical Pattern: Use nested loops to create a mesmerizing pattern of stars, triangles, or any other shape your heart desires. Let your artistic spirit roam free as you generate beautiful patterns on the canvas of your Python terminal.

'''
print()
print("The Magical Pattern")
for i in range(6):
    for j in range(6-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
        
    print()

'''
The Infinite Laughter: Design a joke generator that displays a series of jokes using a while loop. Keep the laughter going until the user decides to exit the program. Spread joy and giggles with your infinite humor machine.

'''

import pyjokes
print()
print("The Infinite Laughter")
answer = "yes"
while answer != "no":
    answer = input("Do you want to hear a joke? yes/no : ")
    if answer == "no":
        break
    if answer == "yes":
        joke = pyjokes.get_joke()
        print(joke)
    else:
        print("please type yes or no.")
