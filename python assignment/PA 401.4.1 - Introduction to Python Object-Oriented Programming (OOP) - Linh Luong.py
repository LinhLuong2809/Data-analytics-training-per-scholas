'''
Task 1: Creating a Simple Class

Open a new Python script file.
Define a class named Person with a constructor method (__init__) taking name and age parameters.
Inside the constructor, initialize attributes name and age with the provided parameters.
Print a message inside the constructor to indicate the creation of a person object.

'''

class Person:
    def __init__(self, name, age, secret):
        self.name = name
        self.age = age
        self.__secret = secret
        print("Person info created")
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
    def reveal_secret(self):
        return self.__secret
    
'''
Task 2: Inheritance - Extending the Class

Below the Person class, define a subclass named Student.
In the Student class, create a constructor method (__init__) with additional parameter student_id.
Use super().__init__(name, age) inside the Student constructor to call the constructor of the parent class.
Initialize the student_id attribute with the provided parameter.
Print a message inside the Student constructor to indicate the creation of a student object.


'''
'''
Task 3: Polymorphism - Adding Methods

In both the Person and Student classes, create a method named display_info.
In the Person class method, print the person's name and age.
In the Student class method, override the display_info method to include the student ID and call the parent class method using super().display_info().

'''
'''
Task 4: Encapsulation - Private Attribute

Inside the Person class, add a private attribute named __secret with an initial value.
Create a method named reveal_secret inside the Person class that prints the value of __secret.
Outside the class, attempt to access the private attribute directly.

'''
class Student(Person):
    def __init__(self, name, age, secret, student_id):
        super().__init__(name, age, secret)
        self.student_id = student_id
        print("Student info added")
        
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        super().display_info()
        
    def reveal_secret(self):
        return self.__secret

person1 = Person("Tony", 23, "like banana")
student1 = Student("Linh", 33, "Like video game", 1234)
