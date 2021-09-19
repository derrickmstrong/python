# Class

class PartyAninal:
    # Data
    x = 0 # self.x
    name = "" # self.name
    # Initialize constructor (optional)
    def __init__(self, name):
        self.name = name
        print('I am constructed')
        print(self.name, "constructed")
    # Method - self is sorta like this in JS
    def party(self):
        self.x += 1
        print("So far", self.x)
    # Delete or Destructor (optional)
    def __del__(self):
        print(self.name, 'has been destructed and last x was', self.x)


# Instance of a class PartyAnimal ie. object
dog = PartyAninal("Ruff")  # Parameter represents name in __init__ method
dog.party() # Run party method on this object
dog.party() # Run party method on this object
dog.party() # Run party method on this object
print(dog.x)

# Instance of a class PartyAnimal ie. object
cat = PartyAninal("Kitty")  # Parameter represents name in __init__ method
cat.party() # Run party method on this object
cat.party() # Run party method on this object
print(cat.x)

# Instance of a class PartyAnimal ie. object
fish = PartyAninal('Bubbles')  # Parameter represents name in __init__ method
fish.party()  # Run party method on this object
fish.party()  # Run party method on this object
print(fish.x)
