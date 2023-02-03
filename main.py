# import colorama 
# print(colorama.Back.RED)
# print(colorama.Back.BLACK)

#mro порядок разршение методов 

class Human:
    head = 1
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


hum = Human("beka", 19)
hum.name = "beks" 


class SuperHero(Human):
    def __init__(self, name, age, wings = True) -> None:
        super().__init__(name, age,)
        self.wings = wings

    def flying(self):
        if self.wings == True:
            return f"{self.name} in Fly"

    def fly(self):
        if self.wings != False:
           self.flying()
        else:
            return f"{self.name} in flying"
        


hum2 = SuperHero("Николай", 20, )

print (hum2.fly())
print(hum2.flying())