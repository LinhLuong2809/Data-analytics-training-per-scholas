# Task 1: Explore the Arithmetic Realm
'''
In the mystical land of arithmetic operators, you will perform magical calculations. Open your favorite Python IDE or text editor, create a new Python file, and dive into the world of arithmetic operators. Use operators like `+`, `-`, `*`, `/`, `%`, and `**` to perform basic arithmetic operations. Experiment with various expressions and print the results.

To Dos - 1

Choose or declare two variables, let's call them num1 and num2, and assign them numerical values (e.g., num1 = 8 and num2 = 3).
Experiment with the following expressions using the provided arithmetic operators:
Addition, Subtraction, Multiplication, Division, Modulo, Exponentiation. 
Print the results of each operation using print() statements.
Run your Python file and observe the output to understand the effects of each arithmetic operator.

'''
    
num1 = 34
num2 = 21
# Addition, Subtraction, Multiplication, Division, Modulo, Exponentiation. 

print(f"num1 = {num1}")
print(f"num2 = {num2}")
x = num1 + num2
print(f"num1 + num 2 = {x}")

x = num1 - num2
print(f"num1 - num 2 = {x}")

x = num1 * num2
print(f"num1 * num 2 = {x}")

x = num1 / num2
print(f"num1 / num 2 = {x}")

x = num1 % num2
print(f"num1 % num 2 = {x}")

x = num1 ** num2
print(f"num1 ** num 2 = {x}")

print()
# Task 2: Navigate the Comparison Seas
'''
Sail through the comparison seas using comparison operators. Create a program that compares different values using operators like `==`, `!=`, `<`, `>`, `<=`, and `>=`. Print the results of these comparisons to understand how these operators work.

To Dos - 2
Create or choose two variables, e.g., value1 and value2, and assign them numerical values.
Use comparison operators (==, !=, <, >, <=, >=) to compare the values of value1 and value2.
Print the results of each comparison using print() statements.

'''

num1 = 12
num2 = 5

x = num1 == num2
print(f"num1 == num2 is {x}")

x = num1 != num2
print(f"num1 != num2 is {x}")

x = num1 > num2
print(f"num1 > num2 is {x}")

x = num1 < num2
print(f"num1 < num2 is {x}")

x = num1 <= num2
print(f"num1 <= num2 is {x}")

x = num1 >= num2
print(f"num1 >= num2 is {x}")

# Task 3: Conquer the Logical Galaxy
print()
'''
In the logical galaxy, create a program that demonstrates the power of logical operators. Use `and`, `or`, and `not` to combine and manipulate boolean values. Print the results to unveil the truth behind logical operations.

To Dos - 3:
Declare two boolean variables, e.g., is_sunny and is_warm, and assign them True or False values.
Use logical operators (and, or, not) to combine and manipulate boolean values.
Print the results of each logical operation.

'''
is_sunny = True
is_warm = False

x = is_sunny and is_warm
print(f"is_sunny and is_warm is {x}")

x = is_sunny or is_warm
print(f"is_sunny or is_warm is {x}")

x = is_sunny is not is_warm
print(f"is_sunny not is_warm is {x}")

# Task 4: Harness the Assignment Powers
print()
'''
Explore the world of assignment operators to manipulate variables. Create a program that uses operators like `=`, `+=`, `-=`, `*=`, `/=`, and `**=` to modify variable values. Print the updated values to witness the impact of assignment operators.
To Dos - 4:

Declare variables, e.g., x and y, and assign them numerical values.
Use assignment operators (=, +=, -=, *=, /=, **=) to modify the values of x and y.
Print the updated values of x and y to observe the impact of assignment operators.

'''
x = 10
y = 20
print(f"x = {x} ; y = {y}")
print()

x+= 21
y+= 2
print(f"x = {x} ; y = {y}")
print()

x-= 5
y-= 12
print(f"x = {x} ; y = {y}")
print()

x*= 3
y*= 4
print(f"x = {x} ; y = {y}")
print()

x/= 5
y/= 2
print(f"x = {x} ; y = {y}")
print()

x**= 2
y**= 3
print(f"x = {x} ; y = {y}")
print()

# Task 5: Uncover the Identity Mysteries
'''
In the realm of identity, create a program that explores identity operators `is` and `is not`. Compare variables and objects to understand when these operators yield `True` or `False`.

To Dos - 5:
Declare variables, e.g., a, b, c, and d, and assign them values.
Use identity operators (is and is not) to compare the identity of variables and objects.
Print the results of each identity comparison.

'''
a = 3
b = "dad"
c = "mom"
d = 10
e = 3
f = "dad"

print(a is b)
print(a is c)
print(a is d)
print(a is e)
print(b is f)
print(b is not e)
print(f is not a)
print(c is d)
print(c is not e)
print()

# Task 6: Embrace the Membership Adventure
print("Task 6: Embrace the Membership Adventure")

'''
Embark on a membership adventure by using `in` and `not in` operators. Create a program that checks whether elements exist in a sequence (list). Print the results to uncover the membership mysteries.

To Dos - 6:
Declare a list, e.g., fruits, and populate it with some elements (strings).
Use membership operators (in and not in) to check if certain elements exist in the list.
Print the results of each membership check.

'''
basket = ["apple", "banana", "lemon", "tomato","grapes","pineaples","watermelon"]

print("apple" in basket)
print("banana" not in basket)
print("onion" in basket)
print("lettuce" not in basket)

# Task 7: Ascend the Precedence Summit
'''
Climb the precedence summit by understanding the precedence of operators. Create expressions that involve multiple operators and observe how Python follows the rules of precedence. Print the results to unravel the secrets of operator precedence.
To Dos - 7:

Create expressions involving multiple operators to observe the precedence.
Use arithmetic, comparison, and logical operators in the expressions.
Print the results of each expression to understand the precedence of operators.

'''
print()
print("# Task 7: Ascend the Precedence Summit")

x = 33 + 2 -3*2- 10 + 3**4 / 2
y = 33 + 2 -3*2- 10 + 3**4 / 2 > 23
z = 33 + 2 -3*2- 10 + 3**4 / 2 > 23 and False
print(x)
print(y)
print(z)