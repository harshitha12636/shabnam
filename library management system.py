class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently not available.")
                    return
        print(f"Sorry, we don't have a book titled '{title}'.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"You have returned '{book.title}'.")
                return
        print(f"Sorry, we don't have a record of '{title}' being borrowed.")

    def view_books(self):
        print("Available books:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"- {book.title} by {book.author} ({status})")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Lend Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == '2':
            title = input("Enter book title to lend: ")
            library.lend_book(title)
        elif choice == '3':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '4':
            library.view_books()
        elif choice == '5':
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
