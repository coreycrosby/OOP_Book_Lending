from datetime import datetime
import random

class Book:

    on_shelf = []
    on_loan = []
    overdue_books = []

    """This instance method makes a new book object. It should initialize a book's title, author, and ISBN."""
    def __init__(self, book_title, author, ISBN):
        self.book_title = book_title
        self.author = author
        self.ISBN = ISBN
        self.due_date = None

    """This class method is how new books are added to the library."""
    @classmethod
    def create(cls, book_title, author, ISBN):
        book = Book(book_title, author, ISBN)
        cls.on_shelf.append(book)
        return book

        """This class method returns the due date for books taken out today."""
    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    """This class method should return a list of books whose due dates are in the past"""
    @classmethod
    def overdue_books(cls):
        for book in cls.on_loan:
            if Book.current_due_date() < datetime.now():
                cls.overdue_books.append(book)


    """This class method should return a random book from on_shelf"""
    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)

    """This instance method is how a book is taken out of the library. 
    use lent_out to check if the book is already on loan, 
        and if it is this method should return False to indicate that the attempt to borrow the book failed. 
    Otherwise,
        use current_due_date to set the due_date of the book 
        and move it from the collection of available books to the collection of books on loan,then return True."""
    def borrow(self):
        if self.lent_out():
            return False
        else:
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            self.due_date = Book.current_due_date()
            return True
        
    """This instance method is how a book gets returned to the library. 
    call lent_out to verify that the book was actually on loan. 
    If it wasn't on loan in the first place, return False. 
    Otherwise, move the book from the collection of books on loan to the collection of books on the library shelves, 
    set the book's due date to None before returning True."""
    def return_to_library(self):
        if self.lent_out():
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due_date = None
            return True
        else:
            return False
        

    """This instance method should return true if a book has already been borrowed and false otherwise."""
    def lent_out(self):
        for book in Book.on_loan:
            if book == self:
                return True
            return False

    

sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sister_outsider.lent_out())
print(sister_outsider.borrow())
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sister_outsider.lent_out())
print(sister_outsider.borrow())
print(sister_outsider.due_date)
print(len(Book.overdue_books)
print(sister_outsider.return_to_library())
print(sister_outsider.lent_out())
print(len(Book.on_shelf))
print(len(Book.on_loan))