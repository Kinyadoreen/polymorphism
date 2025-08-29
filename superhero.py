### Activity 1: Design Your Own Class
class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city
    def save_the_world(self):
        print(f"{self.name} is saving the world using {self.superpower}!")
    def introduce(self):
        print(f"Hello, I'm {self.name} from {self.city}. My superpower is {self.superpower}.")
class Superstar(Superhero):
    def __init__(self, name, superpower, city, weakness):
        super().__init__(name, superpower, city)
        self.weakness = weakness
    def cause_trouble(self):
        print(f"{self.name} is causing trouble in {self.city}!")
    def reveal_weakness(self):
        print(f"{self.name}'s weakness is {self.weakness}!")
# Creating instances of Superhero and Superstar
hero = Superhero("Captain Shine", "Super Strength", "Denmark")
Superstar = Superstar("Prof Kendy", "Mind Control", "Casablanca", "Love")
# Using methods
hero.introduce()
hero.save_the_world()
Superstar.introduce()
Superstar.cause_trouble()
Superstar.reveal_weakness()

### Activity 2: Polymorphism Challenge

# Parent class: Animal
class Animal:
    def move(self):
        pass
# Child classes
class Dog(Animal):
    def move(self):
        print("The dog is running!")
class Fish(Animal):
    def move(self):
        print("The fish is swimming!")
class Bird(Animal):
    def move(self):
        print("The bird is flying!")
# Create objects
dog = Dog()
fish = Fish()
bird = Bird()
# Use the move() method
dog.move()
fish.move()
bird.move()

