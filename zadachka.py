# # class Shape:
# #     def __init__(self,name):
# #         self.name = name 

# #     def draw(self):
# #         print(f"Рисуем фигуру {self.name}")
# # shape = Shape("Ничего")
# # shape.draw()

# # class Rectangle(Shape):
# #     def __init__(self, name):
# #         super().__init__(name)
    
# #     def draw(self):
# #         return super().draw()
    
# # rectangle = Rectangle("Прямоугольник")
# # rectangle.draw()

# # class Circle(Shape):
# #     def __init__(self, name):
# #         super().__init__(name)
    
# #     def draw(self):
# #         return super().draw()
    
# # circle = Circle("Круг")
# # circle.draw()


class Computer:
    def __init__(self,__cpu,__memory):
        self.__cpu = __cpu
        self.__memory = __memory

    def get_item(self):
        return self.__cpu, self.__memory
    
    def  __make_computations(self):
        print(f"{self.__memory} + {self.__cpu} = {self.__memory + self.__cpu}")
        print(f"{self.__memory} - {self.__cpu} = {self.__memory - self.__cpu}")
        print(f"{self.__memory} / {self.__cpu} = {self.__memory / self.__cpu}")
        print(f"{self.__memory} * {self.__cpu} = {self.__memory * self.__cpu}")

    def get_make(self):
        return self.__make_computations()
    
    
# computer = Computer(12,2)
# print(computer.get_item())
# print(computer.get_make())

 
class Phone:
    def __init__(self):
        self._sim_cards_list = []

    def set_sim(self,sim_cards_list):
        if sim_cards_list:
            self._sim_cards_list = sim_cards_list 
            print(self._sim_cards_list)

    def call(self,sim_card_number:str,call_to_number:int):
        if call_to_number == 1:
            call_to_number = "Beeline"
            print(f"Вам звонит абонимент {sim_card_number} - c сим карты {call_to_number}")
        elif call_to_number == 2:
            call_to_number = "Oshka"
            print(f"Вам звонит абонимент {sim_card_number} - c сим карты {call_to_number}")
        else:
            print("Вы велли не правильно выбрали сим карту")

# phone = Phone()
# print(phone.set_sim("+996 559 515 260"))
# phone.call("+996 559 515 260",1 )

class SmartPhone(Computer,Phone):
    def __init__(self, __cpu, __memory):
        super().__init__(__cpu, __memory)

    def use_gps(self,):
        print("Здрасвтуйте, выберите где вы находитесь чтоб добраться до Geeks")
        print("1) Западный \n2) Восток \n3) Келечек \n4) Араванский")
        location = int(input("1,2,3 или 4: "))
        if location == 1:
            print(f"Сядьте на маршутку 146 и вас достовять прям до двери Geeks")
        elif location == 2:
            print("Садьте на маршутку 134 или 138 и вас достовять до дверей Geeks")
        elif location == 3:
            print("Садьте на маршутку 134,138 или 25 и вас достовять до дверей Geeks")
        elif location == 4:
            print("Садьте на маршутку 25,134 или 138 и вас достовять до дверей Geeks")
        else:
            print("Вы не правильно вели локацию")

    def add_memeory_card(self):
        print("Выберите насколько хотите увеличеть память на телефоне \n1)Увеличивает память на 10гб \n2)Увеличевает память на 15гб \n3)Увеличивает память на 20гб")
        add_memeory_card = int(input("1,2 или 3: "))
        if add_memeory_card == 1:
            print("Ваша память увеличена на 10гб ")
        elif add_memeory_card == 2:
            print("Ваша память увеличена на 15гб ")
        elif add_memeory_card == 3:
            print("Ваша память увеличена на 20гб ")
        else:
            print("Вы не правильно вели введите заново")

# user_phone = SmartPhone(13,5)
# user_phone.use_gps()
# user_phone.add_memeory_card()
              
class Lenux(Computer):
    def __init__(self, __cpu, __memory):
        super().__init__(__cpu, __memory)
lenux = Lenux(15,4)
print(lenux.get_item())
print(lenux.get_make())
    
class Apple(Phone):
    def __init__(self):
        super().__init__() 
apple = Apple()
print(apple.set_sim("+996 559 515 260"))
apple.call("+996 559 515 260",2)

class Iphone(SmartPhone):
    def __init__(self, __cpu, __memory):
        super().__init__(__cpu, __memory)
iphone = Iphone(12,3)
iphone.use_gps()
iphone.add_memeory_card()


class Samsung(SmartPhone):
    def __init__(self, __cpu, __memory):
        super().__init__(__cpu, __memory)
samsung = Samsung(15,5)
samsung.use_gps()
samsung.add_memeory_card()



