import xml.etree.ElementTree as ET  
import os  # dosya kontrolü için  

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

    def find_book_by_author(self, author_name):  
        return [book for book in self.books if book.author.name == author_name]  

    def display_books(self):  
        if not self.books:  
            print("Kitap yok!")  
        for book in self.books:  
            print(f"Kitap: {book.title}, Yazar: {book.author.name}")  

    def load_from_xml(self, xml_file):  
        # XML dosyasının var olduğunu kontrol et  
        if not os.path.exists(xml_file):  
            print(f"Hata: {xml_file} dosyası bulunamadı.")  
            return  

        try:  
            tree = ET.parse(xml_file)  
            root = tree.getroot()  
        except ET.ParseError:  
            print("Hata: XML dosyası geçersiz bir yapıya sahip.")  
            return  

        authors = {}  
        # Yazarları okuma  
        for author_elem in root.find('authors').findall('author'):  
            author_name = author_elem.find('name').text  
            authors[author_name] = Author(author_name)  

        # Kitapları okuma  
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

        # Yazarları ekleme  
        authors = {book.author.name: book.author for book in self.books}  
        for author in authors.values():  
            author_elem = ET.SubElement(authors_elem, "author")  
            name_elem = ET.SubElement(author_elem, "name")  
            name_elem.text = author.name  
        
        # Kitapları ekleme  
        for book in self.books:  
            book_elem = ET.SubElement(books_elem, "book")  
            title_elem = ET.SubElement(book_elem, "title")  
            title_elem.text = book.title  
            author_elem = ET.SubElement(book_elem, "author")  
            author_elem.text = book.author.name  

        tree = ET.ElementTree(root)  
        tree.write(xml_file)  

    def add_new_book(self, title, author_name):  
        author = Author(author_name)  
        book = Book(title, author)  
        self.add_book(book)  

# Kütüphane nesnesi oluşturma ve kitapları yükleme  
library = Library()  
library.load_from_xml('C:\\Users\\d-e-m\\Desktop\\python2\\dbooks.xml')  
library.display_books()  

# Kullanıcıdan yeni kitap bilgisi alma ve ekleme  
new_title = input("Yeni kitap başlığını girin: ")  
new_author = input("Yeni yazar adını girin: ")  
library.add_new_book(new_title, new_author)  

# Güncellenmiş kütüphaneyi XML dosyasına kaydetme  
library.save_to_xml('C:\\Users\\d-e-m\\Desktop\\python2\\dbooks.xml')  
library.display_books()  