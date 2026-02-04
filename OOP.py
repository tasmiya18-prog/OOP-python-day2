# Parent class
class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

# Child class inheriting from Book
class IssuedBook(Book):
    def _init_(self, title, author, issued_to, issued_date):
        super()._init_(title, author)  # Calling parent class constructor
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        print("Book Details:")
        super().display_book_details()  # Calling parent class method
        print(f"Issued To: {self.issued_to}")
        print(f"Issued Date: {self.issued_date}")

    def display_book_details(self):
        # Overriding parent class method
        print(f"Title: {self.title}, Author: {self.author}")

# Create an object of IssuedBook
issued_book = IssuedBook("Python Programming", "John Smith", "Jane Doe", "2022-01-01")

# Display issued book details
issued_book.display_issued_book_details()
print("\nDisplaying book details using overridden method:")
issued_book.display_book_details()
