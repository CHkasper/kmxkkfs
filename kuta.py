# class Student():
#     def __init__(self,name,username,bilet,kurs):
#         self.name = name 
#         self.username = username
#         self.bilet = bilet 
#         self.kurs = kurs 

#     def Info(self):
#         print(f"{self.name} {self.username} студенческий билет {self.bilet} учиться на курсе {self.kurs}") 

#     def Kurs(self):
#         self.kurs = input("Введите курс на который вы ходите: ")
#         print(f"учиться на курсе {self.kurs}")

# student = Student('bayel',"anashov",1234,"Geeks")
# # student.Info()  
# # student.Kurs()



# class Library():
#     def __init__(self):
#         self.books = []

#     def add_book(self,name,auther):
#         book =  {"name": name,"auther": auther,"available": True}
#         self.books.append(book)
#         print(f'Книга "{name}" добавлена в библиотеку. Писатель {auther}')

#     def remove_book(self,name):
#         for book in self.books:
#             if book['name'] == name:
#                 self.books.remove(book)
#                 print(f"книга {name} удалена из библеотеки")
#                 return True
#         print(f'книга {book} нету в библеотеки')
#         return False
    
#     def borrow_book(self,name):
#         for book in self.books:
#             if book['name'] == name:
#                 self.books.append(book)
#                 print(f"книга {name} добавлена в библеотеки")
#                 return True
#         print(f"книга {book} нету в библеотеки")
#         return False
                
#     def lend_book(self,name):
#         for book in self.books:
#             if book['name'] == name:
#                 if book["available"]:
#                     print(f"книга {name} выдана читателю")
#                 else:
#                     print(f"книги {name} нету в библеотеки")
#                 return True
#         print(f"книга {name} нету в библеотеки")
#         return False
    
#     def return_book(self,name):
#         for book in self.books:
#             if book["name"] == name:
#                 if book["available"]:
#                     print(f"Книга {name} возврашена в библеотеку")
#                 else:
#                     print(f"Книга {name} уже в библеотеке")
#                 return True
#             print(f"Такой книги как {name} нету в библеотеке")
#             return False 

#     def list_books(self):
#         if not self.books:
#             print("Библеотека пуста")
#             return
#         print("Книги В библеотеке:")
#         for book in self.books:
#             status = "Доступно" if book["available"] else "Выдана"
#             print(f"- {book['name']} {book['auther']} ({status}) ")
             

# library = Library()
# library.add_book('Война и Мир',"Лев Толстой")
# library.add_book('Чыпалак',"Лев Толстой")
# library.add_book('Война и Мир',"Лев Толстой")

class Person:
    def __init__(self,name,age,is_married):
        self.name = name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Имя - {self.name}, возраст - {self.age}, женат - {self.is_married}")

person = Person("bayel",12,True)
# person.introduce_myself()

class Student(Person):
    def __init__(self, name, age, is_married):
        super().__init__(name, age, is_married) 

    def average_value(self):
        urok = {"англиский":100 ,"руский":100,"история":100}
        dostup = input("Введите словарь: ")
        # print(f"среднее бал по ЭНТ {sum(urok) / len(urok)}")
        print(urok(dostup))

student = Student("kuta",16,False)
student.average_value()
        

        