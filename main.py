class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0 - ситий, 100 - голодний
        self.energy = 50  # 0 - втомлений, 100 - бадьорий

    def __str__(self):
        return f"{self.name}: Голод={self.hunger}%, Енергія={self.energy}%"

    def eat(self):
        print(f"🍽{self.name} поїв.")
        self.hunger = max(0, self.hunger - 30)

    def sleep(self):
        print(f"{self.name} поспав.")
        self.energy = min(100, self.energy + 40)

    def play(self):
        print(f"{self.name} погрався (ТИГИДИК!).")
        self.energy = max(0, self.energy - 30)
        self.hunger = min(100, self.hunger + 20)

# Приклад використання:
barsik = Cat("Барсик")
barsik.play()
barsik.eat()
barsik.sleep()
print(barsik)

