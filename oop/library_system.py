

class Book:
    
    def __init__(self,title,author):
        self.title = title
        self.author = author 
    def display_book(self):
        print(f'Book: {self.title} by {self.author}')

    def __str__(self):
        return f'This is a book, Title -> {self.title}, Author -> {self.Author}'
    
class EBook(Book):
    
    def __init__(self,title,author,file_size):
        self.file_size = file_size
        super().__init__(title,author)

    def display_book(self):
        print(f'EBook: {self.title} by {self.author}, File Size: {self.file_size}KB')
    
class PrintBook(Book):
    def __init__(self,title,author,page_count):
        self.page_count = page_count
        super().__init__(title,author)

    def display_book(self):
        print(f'PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}')
    
class Library():
    
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        
        for book in self.books:
            book.display_book()
        
      
        
        
    
    
