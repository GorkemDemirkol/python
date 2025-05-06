class Author:
    def __init__(self, name):
        self.name = name
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def find_book_by_author(self,author_name):
        return [book for book in self.books if book.author.name == author_name]
    def display_books(self):
        for book in self.books:
            print(f"Kitap: {book.title}, Yazar: {book.author.name}")
    
library=Library()
author1=Author(" Leo Tolstoy")
author2=Author(" George Orwell")
author3=Author("Harper Lee")
author4=Author("Fyodor Dostoyevski")
author5=Author("Antoine de Saint-Exupéry")
author6=Author("J.K. Rowling")
author7=Author("Charles Dickens")
author8=Author("Gabriel García Márquez")
author9=Author("Ray Bradbury")
author10=Author("Can Yucel")

book1=Book("Savaş ve Barış",author1)
book2=Book("1984",author2)
book3=Book("Bülbülü Öldürmek",author3)
book4=Book("Suç ve Ceza",author4)
book5=Book("Küçük Prens",author5)
book6=Book("Harry Potter ve Felsefe Taşı",author6)
book7=Book("İki Şehrin Hikayesi",author7)
book8=Book("Yüzyıllık Yalnızlık",author8)
book9=Book("Fahrenheit 451",author9)
book10=Book("Yalnızım",author10)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)
library.add_book(book9)
library.add_book(book10)

library.display_books()

J_K_Rowling_books=library.find_book_by_author("J.K. Rowling")
for book in J_K_Rowling_books:
    print(book.title)