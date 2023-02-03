from main import *

# print(colorama.Fore.BLUE)


# class MEgaHuman:
#     def str(self) -> str:
#         return f'{self.name} {self.age} {self.wings}'
    
# hum3 = MEgaHuman("Islam", 18)
# hum3.flying()
# print(hum3.fly())


class Bank:
    def __init__(self, name, age, balance, key : str) -> None:
        self.name = name
        self.age = age
        self._balance = balance
        self.key = key

    # def __len(self):

    def parol(self):
        if len (self.__key) >= 8:
            return self.__key
        else:
            raise ValueError (f"lenchik больше 8")
        
    def __str__(self) -> str:
        return f'{self.name} {self._balance}'

bank = Bank("Asylbek", 16, 4000, 212123)
# print(bank)
print(bank.parol())