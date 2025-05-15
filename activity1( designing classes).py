# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I can {self.power}!")

    def fight_crime(self):
        print(f"{self.name} is fighting crime with {self.power}!")

# Subclass using inheritance
class Supervillain(Superhero):
    def __init__(self, name, power, origin, evil_plan):
        super().__init__(name, power, origin)
        self.evil_plan = evil_plan

    def introduce(self):
        print(f"I am {self.name}, and I'm planning to {self.evil_plan}!")

    def fight_crime(self):
        print(f"{self.name} is causing chaos instead of stopping it!")

# Create objects
hero = Superhero("ThunderGirl", "control lightning", "Zeus City")
villain = Supervillain("DarkMind", "mind control", "Shadow Realm", "take over minds of world leaders")

# Use methods
hero.introduce()
hero.fight_crime()

print("---")

villain.introduce()
villain.fight_crime()
