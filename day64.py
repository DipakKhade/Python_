# Exercise 6 - Library Management System in Python


class library:
    def __init__(self):
        total_books:books
        no_of_books:int()

        def no(self):
            print('The number of books are :',len(no_of_books))

a=library()




#
class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)


l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()
    
