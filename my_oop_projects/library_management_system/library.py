class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title} has been added to library.")
    
    def remove_book(self, title):
        for book in self.books:
            if self.title == title:
                self.books.remove(book)
                print(f"The book '{title}' has been removed from library.")
                return
        print(f"The book '{title}' not fond in the library.")
    
    def display_books(self):
        if not self.books:
            print("The library is emoty!")
        else:
            print("Books in library are: ")
            for book in self.books:
                print(book)