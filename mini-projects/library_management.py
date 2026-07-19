class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Available: {self.available}")
        print("-" * 30)

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'"{self.title}" borrowed successfully.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'"{self.title}" returned successfully.')
        else:
            print(f'"{self.title}" is already available.')


book1 = Book("Atomic Habits", "James Clear", 2018)
book2 = Book("Clean Code", "Robert C. Martin", 2008)
book3 = Book("Deep Learning", "Ian Goodfellow", 2016)


library = [book1, book2, book3]



print("===== LIBRARY =====")

for book in library:
    book.display_info()


book2.borrow_book()


print("\n===== UPDATED LIBRARY =====")

for book in library:
    book.display_info()



book2.borrow_book()
book2.borrow_book()