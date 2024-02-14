# Task 1: Enter the Land of Lists
# Task 2: Embark on the List Chronicles
# The Mighty Superheroes

print("The Mighty Superheroes")
heroes = ["Spider-Man", "Iron Man", "Black Panther", "Wonder Woman"]

print("Our mighty superheroes are:")
for hero in heroes:
    print(hero)

print("But wait! There's a new hero in town!")
heroes.append("Superman")

print("Now our superheroes are:")
for hero in heroes:
    print(hero)

print()
# Task 3: Unleash Your List Powers
# 1. The Quest for Sorting: Create a program that takes a list of numbers and sorts them in ascending or descending order. Challenge yourself to implement sorting algorithms like bubble sort or insertion sort.
print("The Quest for Sorting")
def sort_ascend(mylist):
    list_range = len(mylist) 
    
    for i in range(list_range): # loop through each element of the list
        for j in range(0, list_range - i - 1): # loop through the next element of the list to compare
            if mylist[j] > mylist[j+1]: # compare if first element > the next element
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j] # swap their position 
                
def sort_descend(mylist):
    sort_ascend(mylist) # call ascend sorting
    reversedlist = mylist[::-1] # reverse the order
    return reversedlist # return the descended list
    
listsize = 0
while listsize != 0 or listsize !=1:
    listsize = int(input("Enter the size of your list: "))
    if listsize < 2:
        print("List size can't be negative number or 0 or less than 1. Please enter positive number!")
    else:
        break
        
mylist = []
while listsize > 0:
    value = int(input("Enter number for the list: "))
    mylist.append(value)
    listsize -= 1
    
print(f"Your list: {mylist}")
sort_ascend(mylist)
print("Ascended list: {}".format(mylist))
mylist_descent = sort_descend(mylist)
print("Descended list: {}".format(mylist_descent))

print()

# The Battle of Lists: Write a program that compares two lists and finds the common elements between them. Display the matching items and the total count of matches.
print("The Battle of Lists")

def compareList(list1, list2):
    list3 = [] # emtpy list to stored matched element
    count = 0 # count for matched element
    
    list1Len = len(list1)
    list2Len = len(list2)
    
    for i in range(list1Len): # traverse through each element of list 1
        for j in range(list2Len): # nested loop traverse through each element of list 2 
            if list2[j] == list1[i]: # compare each element of list 2 to the element of list 1 
                if list2[j] not in list3: # check if common elements not in list3 yet then add common elements and increase the count
                    list3.append(list2[j])
                    count += 1
    
    print("Matched elements: {}".format(list3))
    print("Total count of matches: {}".format(count))

# test
list1 = []
list2 = []
list1size = 0
list2size = 0
while list1size is not None:
    list1size = int(input("Enter the size of your first list: "))
    
    if list1size < 1:
        print("List size can't be negative number or 0 or less than 1. Please enter positive number!")
    else:
        break
    

while list2size is not None:
    list2size = int(input("Enter the size of your second list: "))
    if list2size < 1:
        print("List size can't be negative number or 0 or less than 1. Please enter positive number!")
    else:
        break
    
while list1size > 0:
    value = input("Enter elements for the first list: ")
    list1.append(value)
    list1size -= 1

while list2size > 0:
    value = input("Enter elements for the second list: ")
    list2.append(value)
    list2size -= 1
    
print(f"First list: {list1}")
print(f"Second list: {list2}")
compareList(list1, list2)

print()
# The Legendary Inventory: Design a game inventory system where the player can add or remove items from their inventory. Use lists to store the items and allow the player to perform actions such as viewing, adding, or dropping items.
print("The Legendary Inventory")
def add_item(list, item):
    list.append(item)
    print("You add {} to your inventory".format(item))
    print()

def view(list):
    print("Your inventory:")
    print(list)
    print()
    
def drop_item(list, item):
    list.remove(item)
    print("You dropped {}".format(item))
    print()
    
#Test
print("Player's Inventory created.")
inventory = []
itemList = ["sword", "shield", "potion", "herb", "antidote","helmet","chestplate","boots","wristband","amulet","ring","roasted chicken","shoulderplate", "darkstone"]
order = True
action = 0
add = True
drop = True
while order:
    while action is not None:
        action = int(input("What do you want to do (pick number 1 - 3)? 1.view inventory 2.add item 3.drop item or press 0 to exit "))
        if action == 1:
            view(inventory)
        elif action == 2:
            print("Item List: ")
            print(itemList)
            while add:
                decision = "y"
                item = input("Please choose item from the list to add to your inventory: ")
                if item in itemList:
                    add_item(inventory, item)
                else:
                    print("Item is not in the list, please pick item from the list") 
                while decision != "n":
                    decision = input("Do you want to keep adding item to your inventory? y/n: ")
                    if decision == 'n':
                        add = False
                    elif decision == 'y':
                        break
                    else:
                        print("Please enter y or n")            
        elif action == 3:
            view(inventory)
            while drop:
                decision = "y"
                item = input("Please choose item from your inventory to drop: ")
                if item in itemList:
                    drop_item(inventory, item)
                else:
                    print("You don't have this item, please pick item from your inventory to drop.")
                while decision != "n":
                    decision = input("Do you want to keep dropping item from your inventory? y/n: ")
                    if decision == 'n':
                        drop = False
                    elif decision == 'y':
                        break
                    else:
                        print("Please enter y or n")
        else:
            break
    order = False