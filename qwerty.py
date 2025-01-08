# class Library:
#     def __init__(self):
#         self.books = []  # Список книг в библиотеке

#     def add_book(self, title, author):
#         """Добавление книги в библиотеку."""
#         book = {
#             "title": title,
#             "author": author,
#             "available": True
#         }
#         self.books.append(book)
#         print(f'Книга "{title}" добавлена в библиотеку.')

#     def remove_book(self, title):
#         """Удаление книги из библиотеки."""
#         for book in self.books:
#             if book["title"] == title:
#                 self.books.remove(book)
#                 print(f'Книга "{title}" удалена из библиотеки.')
#                 return
#         print(f'Книга "{title}" не найдена в библиотеке.')

#     def lend_book(self, title):
#         """Выдача книги из библиотеки."""
#         for book in self.books:
#             if book["title"] == title:
#                 if book["available"]:
#                     book["available"] = False
#                     print(f'Книга "{title}" выдана читателю.')
#                 else:
#                     print(f'Книга "{title}" уже выдана.')
#                 return
#         print(f'Книга "{title}" не найдена в библиотеке.')

#     def return_book(self, title):
#         """Возврат книги в библиотеку."""
#         for book in self.books:
#             if book["title"] == title:
#                 if not book["available"]:
#                     book["available"] = True
#                     print(f'Книга "{title}" возвращена в библиотеку.')
#                 else:
#                     print(f'Книга "{title}" не была выдана.')
#                 return
#         print(f'Книга "{title}" не найдена в библиотеке.')

#     def list_books(self):
#         """Вывод списка всех книг в библиотеке."""
#         if not self.books:
#             print("Библиотека пуста.")
#             return
#         print("Книги в библиотеке:")
#         for book in self.books:
#             status = "доступна" if book["available"] else "выдана"
#             print(f'- {book["title"]} by {book["author"]} ({status})')


# # Пример использования
# library = Library()
# library.add_book("Война и мир", "Лев Толстой")
# library.add_book("Преступление и наказание", "Фёдор Достоевский")
# library.list_books()
# library.lend_book("Война и мир")
# library.list_books()
# library.return_book("Война и мир")
# library.list_books()
# library.remove_book("Преступление и наказание")
# library.list_books()








qwer = ["qw",'qw','qwer',12,1,2,23]

for i in qwer(1,6,2):
    print(i)   



















































# students = ['Айданек', 'Бекболот', 'Хасанбай', 'Шахрух', 'Акбар  ', 'Мундуз']
# for student in students:
#     print(f"){student} " ) 