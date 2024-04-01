import datetime

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.checked_out = 0
        self.due_date = None

    def checkout(self, user_id):
        if self.quantity > 0:
            self.checked_out += 1
            self.quantity -= 1
            self.due_date = datetime.date.today() + datetime.timedelta(days=14)
            return True
        else:
            return False

    def return_book(self, user_id):
        if self.checked_out > 0:
            self.checked_out -= 1
            self.quantity += 1
            self.due_date = None
            return True
        else:
            return False

    def calculate_fine(self, user_id):
        if self.due_date and self.due_date < datetime.date.today():
            return (datetime.date.today() - self.due_date).days * 1
        else:
            return 0

class Library:
    def __init__(self):
        self.catalog = {}
        self.users = {}

    def add_book(self, book_id, title, author, quantity):
        self.catalog[book_id] = Book(book_id, title, author, quantity)

    def display_catalog(self):
        for book_id, book in self.catalog.items():
            print(f"{book_id}: {book.title} by {book.author} ({book.quantity} available)")

    def register_user(self, user_id, name):
        self.users[user_id] = {"name": name, "checked_out_books": []}

    def checkout_book(self, user_id, book_id):
        book = self.catalog[book_id]
        if book.checkout(user_id):
            self.users[user_id]["checked_out_books"].append(book_id)
            return True
        else:
            return False

    def return_book(self, user_id, book_id):
        book = self.catalog[book_id]
        if book.return_book(user_id):
            self.users[user_id]["checked_out_books"].remove(book_id)
            return True
        else:
            return False

    def calculate_fine(self, user_id, book_id):
        book = self.catalog[book_id]
        return book.calculate_fine(user_id)

    def list_overdue_books(self, user_id):
        overdue_books = []
        for book_id in self.users[user_id]["checked_out_books"]:
            book = self.catalog[book_id]
            if book.due_date and book.due_date < datetime.date.today():
                overdue_books.append((book_id, book.title, book.author, book.calculate_fine(user_id)))
        return overdue_books

library = Library()
library.add_book(1, "The Catcher in the Rye", "J.D. Salinger", 5)
library.add_book(2, "To Kill a Mockingbird", "Harper Lee", 3)
library.add_book(3, "1984", "George Orwell", 2)
library.register_user(1, "John Doe")
library.register_user(2, "Jane Smith")
library.checkout_book(1, 1)
library.checkout_book(1, 2)
library.checkout_book(1, 3)
library.display_catalog()
library.return_book(1, 1)
library.checkout_book(1, 2)
library.checkout_book(1, 3)
library.display_catalog()
print(library.list_overdue_books(1))
