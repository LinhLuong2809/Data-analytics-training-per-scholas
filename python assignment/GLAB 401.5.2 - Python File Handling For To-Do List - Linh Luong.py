# Task 1: Reading and Displaying To-Do List

'''
To Dos - 1: 
Write a Python program that reads and displays the contents of a to-do list stored in a text file.
Use the "with" statement for file handling to ensure proper resource management.
Allow the user to input the filename they want to read for the to-do list.
Display a user-friendly message if the file doesn't exist.

'''    
with open("to_do_list.txt", 'r') as file:        
    try: 
        found = False  
        with open("to_do_list.txt", "r") as file:
            file_content = file.read()
            while True:
                filename = input("What do you want to read from the to do list? ")
                    
                for line in file_content.splitlines():
                    if filename in line:
                        print(line.strip())
                        found = True
                
                con= input("Do you want read more (y/n): ")
                if con == 'y':
                    continue
                elif con == 'n':
                    break
                else:
                    print("wrong choice, pls type y or n")
                    continue
        
        if not found:
            print("File name not in to-do list")

    except Exception as e:
        print("file not exist")
        
# 2 Task 2: Creating and Modifying To-Do List
'''
To Dos - 2: 
Create a function to receive user input for adding tasks to the to-do list.
Validate the input to ensure the task description is not empty.
Implement user-friendly messages to provide feedback on successful task additions and error conditions.
Write the to-do list tasks to a text file in append mode ("a").
Allow the user to choose whether to add another task or exit the program.

'''

with open("to_do_list.txt", 'w') as file:
    while True:
        to_do = input("What do you want to do? ")
        if not to_do.isalpha():
            print("to do can't be empty")
            continue
        
        con= input("Do you want write more (y/n): ")
        if con == 'y':
            file.write(to_do + "\n")
            continue
        elif con == 'n':
            break
        else:
            print("wrong choice, pls type y or n")
            continue
