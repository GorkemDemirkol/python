import xml.etree.ElementTree as ET
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
    
    def load_from_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        authors = {}
        for author_elem in root.find('authors').findall('author'):
            author_name = author_elem.find('name').text
            authors[author_name] = Author(author_name)

        for book_elem in root.find('books').findall('book'):
            title = book_elem.find('title').text
            author_name = book_elem.find('author').text
            author = authors.get(author_name)
            if author:
                book = Book(title, author)
                self.add_book(book)

    def save_to_xml(self, xml_file):
            root = ET.Element("library")
            authors_elem = ET.SubElement(root, "authors")
            books_elem = ET.SubElement(root, "books")
            #yazarları ekleme
            authors={book.author.name:book.author for book in self.books}
            for author in authors.values():
                author_elem = ET.SubElement(authors_elem, "author")
                name_elem = ET.SubElement(author_elem, "name")
def add_new_book(self, title, author_name):
    author = Author(author_name)
    book = Book(title, author)
    self.add_book(book)
    

    authors={}
    for author_elem in root.find('authors').findall('author'):
        author_name=author_elem.find('name').text
        authors[author_name]=Author(author_name)
   
    for book_elen in root.find('books').findall('book'):
        title=book_elen.find('title').text
        author_name=book_elen.find('author').text
        author=authors.get(author_name)
        if author:
            book=Book(title,author)
            self.add_book(book)

library=Library()
library.load_from_xml('C:\\Users\\d-e-m\\Desktop\\python2\\dbooks.xml')  
library.display_books()
new_title=input("Yeni kitap başlığını girin: ")
new_author=input("Yeni yazar adını girin: ")
library.add_new_book(new_title, new_author)
library.save_to_xml('C:\\Users\\d-e-m\\Desktop\\python2\\dbooks.xml')
library.display_books()