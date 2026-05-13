import json
import os
import uuid
from datetime import datetime


class LibraryItem:
    def __init__(self, filename):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self._filename = f"{filename}.json"

    def save(self):
        if os.path.exists(self._filename):
            with open(self._filename) as f:
                old = json.load(f)
            self.id = old["id"]
            self.created_at = old["created_at"]
            self.updated_at = datetime.now().isoformat()

        data = {k: v for k, v in self.__dict__.items() if k != "_filename"}
        with open(self._filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Saved {self._filename}")


class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_borrowed = False


class User(LibraryItem):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")


bookOne = Book("The Alchemist", "Paulo Coelho", 1988, "Fiction")
bookTwo = Book("Brave New World", "Aldous Huxley", 1932, "Dystopian")
bookThree = Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Classic")

userOne = User("Alice")

userOne.borrow_book(bookOne)
userOne.borrow_book(bookTwo)

bookOne.save()
bookTwo.save()
bookThree.save()
userOne.save()

print(bookOne.is_borrowed)   # True
print(bookTwo.is_borrowed)   # True
print(bookThree.is_borrowed) # False