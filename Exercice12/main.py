class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        elif book not in self.borrow_books:
            self.borrow_books.remove(book)
        else:
            print(f"{book.title} doesn't exist")

    def borrow_book(self, book: Book):
        self.borrow_books.append(book)
        self.books.remove(book)

    def return_books(self, book: Book):
        self.books.append(book)
        self.borrow_books.remove(book)

    def available_books(self):
        for book in self.books:
            print(f"{book.title}")

    def borrowed_books(self):
        for book in self.borrow_books:
            print(f"{book.title}")
