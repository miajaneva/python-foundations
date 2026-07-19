class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

book1 = Book("A Tale of Two Cities", "Charles Dickens", 1859)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)


print(book1)
print(book2.year)


def display_book_info(book):
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.year}")

display_book_info(book1)


def borrow_book(book):
    if book.available:
        book.available = False
        print(f"You have borrowed '{book.title}'.")
    else:
        print(f"Sorry, '{book.title}' is currently unavailable.")


def return_book(book):
    if not book.available:
        book.available = True
        print(f"You have returned '{book.title}'.")
    else:
        print(f"'{book.title}' was not borrowed.")


