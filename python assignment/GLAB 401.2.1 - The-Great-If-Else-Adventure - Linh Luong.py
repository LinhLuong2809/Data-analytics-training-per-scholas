# Task 1: Enter the Land of If-Else
# Task 2: Run the Magical Code
# The Enchanted Door
password = input("Enter the secret password: ")

if password == "Open Sesame":
    print("The door opens wide. Welcome!")
else:
    print("The door remains closed. Access denied!")

# Task 3: Take a Leap of Faith
'''
1. The Potion Conundrum: Write a program that asks the user for their age. If they are under 18, display a message saying that they cannot drink the magic potion. Otherwise, grant them access to the secret, magic potion recipe.

'''
print()
print("The Potion Conundrum")
age = int(input("How old are you? "))

if age > 18 :
    print("You are old enought to have this magic potion recipe. Take it!")    
else:
    print("You are under 18, you are not old enough to drink this magic potion")

print()

'''
2. The Riddle of the Sphinx: Create a riddle game where the user has to guess the correct answer. If they guess correctly, congratulate them on their wisdom. Otherwise, bewilder them with a clever hint.

'''
print("The Riddle of the Sphinx")

answer = input("Mary's mom has 4 kids. Their names are Spring, Summer, Fall. What is the name of the 4th kid? ")
if answer == "Mary":
    print("Congratulation, your answer is right!")
else:
    print("Wrong answer. The answer is in the question.")
    
'''
3. The Tricky Troll: Imagine a troll guarding a bridge. Prompt the user to answer a riddle. If they answer correctly, they may pass unharmed. Otherwise, well... let's just say that they will have a bumpy journey.

'''
print()
print("The Tricky Troll")

answer = input("I am easy to lift, but hard to throw. What am I? ")
if answer == "feather":
    print("Your answer is right. You may pass.")
else:
    print("Wrong answer!!!! Your journey ends here.")