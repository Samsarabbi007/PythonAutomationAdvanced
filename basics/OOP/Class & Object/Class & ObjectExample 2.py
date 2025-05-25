class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display__Book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}")

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"Sorry, '{self.title}' is not available for borrowing.")

Book1 = Book("1984", "George Orwell", 0)
Book1.display__Book_info()
Book1.borrow_book()  # Borrowing the book
#Book1.display__Book_info()  # Displaying updated book information after borrowing