from book import Book
from library import Library

library = Library()

while True:
    print("Library Menu")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Book")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice in ["1","Add Book"]: # same as if choice == "1" or if choice == "Add Book"
        title = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        book = Book(author, title)
        library.add_book(book)
    elif choice in ["2","Remove Book"]:
        title = input("Enter the name of the book: ")
        library.remove_book(title)
    elif choice in ["3","Display Book"]:
        library.display_books()
    elif choice in ["4","Exit"]:
        print("Exiting the library. Bye!")
        break