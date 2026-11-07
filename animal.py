# Parent class (superclass)
class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age          # Age in years
        self.weight = weight    # Weight in kilograms

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def get_description(self):
        return f"Animal: {self.name}, Age: {self.age} yo, Weight: {self.weight} kg."


# Subclass "Dog"
class Dog(Animal):
    def __init__(self, name, age, weight, breed):
        # Call the parent constructor using super()
        super().__init__(name, age, weight)
        self.breed = breed

    # Method overriding (polymorphism)
    def eat(self):
        return f"{self.name} the dog is chewing a bone."

    # Unique method for Dog
    def bark(self):
        return f"{self.name} says: Woof woof!"


# Subclass "Cat"
class Cat(Animal):
    def __init__(self, name, age, weight, fur_color):
        super().__init__(name, age, weight)
        self.fur_color = fur_color

    # Method overriding (polymorphism)
    def eat(self):
        return f"{self.name} the cat is eating fish."

    # Unique method for Cat
    def purr(self):
        return f"{self.name} says: Purr-purr..."


# Example usage:

dog = Dog(name="Buddy", age=3, weight=12.5, breed="Dachshund")
cat = Cat(name="Whiskers", age=2, weight=4.0, fur_color="Ginger")

# Call methods and inspect properties
print(dog.get_description())
print(f"Breed: {dog.breed}")
print(dog.eat())
print(dog.bark())
print(dog.sleep())

print("-" * 30)

print(cat.get_description())
print(f"Fur Color: {cat.fur_color}")
print(cat.eat())
print(cat.purr())
print(cat.sleep())