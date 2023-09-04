# Exercise 6 Solution - Library Management Software in Python 
#day 64

class Library:
    def __init__(self):       #THe constructor
            self.nobooks=0
            self.book=[]
    def addbook(self,book):
          self.book.append(book)
          self.nobooks=len(self.book)
        
    def showinfo(self):
          print(f'THe library has {self.nobooks} books')
          
    
 
l1=Library()
l1.addBook('book1')
l1.showinfo()




#CWH code
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
    