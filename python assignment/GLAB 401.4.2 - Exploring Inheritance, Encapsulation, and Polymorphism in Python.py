

# Task 4: OOP in Action - Simulation of a Zoo
'''
1. Define Base Class - Animal:
Create a base class, Animal, with attributes like name, species, and age.
Implement a method, make_sound, which will be overridden by subclasses.

'''

class Animal:
    def __init__(self, name, species, age) :
        self.name = name
        self.species = species
        self.age = age
    
    def make_sound(self):
        pass

'''
2. Create Subclasses - Mammal and Bird:
Create two subclasses, Mammal and Bird, that inherit from the Animal class.
Extend each subclass with attributes specific to mammals and birds, such as fur_color for mammals and feather_color for birds.

3. Implement Polymorphic Behavior:
Override the make_sound method in both the Mammal and Bird subclasses to provide distinct sounds.
Create instances of both mammal and bird types, and use polymorphism to make them 'speak' using the make_sound method.

'''

class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age,)
        self.fur_color = fur_color
        
    def make_sound(self):
        return "GRrrrrrr!"

class Bird(Animal):
    def __init__(self, name, species, age, feather_color):
        super().__init__(name, species, age)
        self.feather_color = feather_color
        
    def make_sound(self):
        return "Chirp chirp!"
    
'''
4. Encapsulation - Zookeeper's Log:
Define a class, Zookeeper, with a log attribute to keep track of animal activities.
Encapsulate the log to ensure controlled access.
Implement methods to add entries to the log, capturing actions like feeding, cleaning, or observing animals.

'''

class Zookeeper():
    def __init__(self) :
        self.__log = []
        
    def add_entries(self, action, animal):
        entry = f"{self._get_timestamp()} : {action.capitalize()} {animal.capitalize()}"
        self.__log.append(entry)
        
    def get_log(self):
        return self.__log.copy()
    
    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
'''
5. Simulate Zoo Activities:
Instantiate various animal objects, including both mammals and birds, within the zoo.
Simulate zoo activities by having the zookeeper log entries for each activity.
Utilize the polymorphic behavior of animals to make them 'speak' and showcase their unique sounds.

'''
mammal = []
mammalName = []
birdName = []
bird = []
zookeeper = Zookeeper()
while True:
    mInput = input("Add mammal to the zoo (y/n)? ")
    if mInput == "y":
        name = input("What's the mammal's name? ")
        specie = input("What's the species? ")
        age = input("how old is it? ")
        color = input("what's the fur color? ")
        mammal.append(Mammal(name,specie, age, color))
        continue
    else:
        break

while True:
    mInput = input("Add bird to the zoo (y/n)? ")
    if mInput == "y":
        name = input("What's the bird's name? ")
        specie = input("What's the species? ")
        age = input("how old is it? ")
        color = input("what's the feather color? ")
        bird.append(Bird(name,specie, age, color))
        continue
    else:
        break
 
while True:
    action = input("type the action for zookeper (ex: clean, observe, feed, etc.): ")
    pick = input("Pick the mammal or bird: ")
    if pick == "mammal":
        index = int(input(f"Pick mammal from the zoo (0 - {len(mammal) - 1} ): "))
        if index >= 0 and index < len(mammal):
            zookeeper.add_entries(action, mammal[index].name)
        else:
            print("animal's index not in the list")
                
                
    elif pick == "bird":
        index = int(input(f"Pick bird from the zoo (0 - {len(bird) - 1} ): "))
        if index >= 0 and index < len(bird):
            zookeeper.add_entries(action, bird[index].name)
        else:
            print("animal's name not in the list")
                
    else:
        print("wrong choice please pick mammal or bird.") 
        continue
    
    choice = input("Do you want to keep logging action for zookeper (y/n)? ")
    if choice == "y":
        continue
    else:
        break
    
while True:
    speak = input("Do you want to make animal speak (y/n)? ")
    if speak == "y":
        pick = input("Pick the mammal or bird: ")
        if pick == "mammal":
            index = int(input(f"Pick mammal from the zoo (0 - {len(mammal) - 1} ): "))
            if index >= 0 and index < len(mammal):
                print(f"{mammal[index].name} : {mammal[index].make_sound()}")
            else:
                print("animal's index not in the list")
                
        elif pick == "bird":
            index = int(input(f"Pick bird from the zoo (0 - {len(bird) - 1} ): "))
            if index >= 0 and index < len(bird):
                print(f"{bird[index].name} : {bird[index].make_sound()}")    
            else:
                print("animal's index not in the list")
        
        else:
            print("pick mammal or bird")
            continue
        continue
    else:
        break

print("Zookeper logs: ")
print(zookeeper.get_log())
               
                                 