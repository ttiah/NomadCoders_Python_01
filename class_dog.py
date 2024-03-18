class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f"{self.breed} puppy named {self.name}."

    def sleep(self):
        print("zzzzzz.......")


class GuardDog(Dog):

    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggressive = True

    def rrrrr(self):
        print("Stay away!")


class Puppy(Dog):

    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
        self.spoiled = True

    def woof(self):
        print("Woof Woof!")

    def introduce(self):
        self.woof()
        print(f"My name is {self.name} and I am a baby {self.breed}")
        self.woof()


doge = Puppy(name="Doge", breed="Beagle")
bibi = Puppy(name="Bibi", breed="Dalmatian")
oops = GuardDog(name="Oops", breed="Jindo")

print(doge)
print(bibi)
print(oops)
doge.woof()
doge.introduce()
bibi.introduce()
oops.rrrrr()
doge.sleep()
bibi.sleep()
oops.sleep()
