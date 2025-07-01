class library:
    def __init__(self, num):
        self.num = num
    
    def isEmpty(self):
        if (self.num <= 0):
            return True
        else:
            return False  
        
    def add_books(self, number):
        self.num += number
        
    def remove_books(self, number):
        self.num -= number  

class book:
    def __init__(self, name, genre, pages):
        self.name = name
        self.genre = genre
        self.pages = pages
        
    def isPresent(self, name):
        if self.name == name:
            return True
        else:
            return False
        
    def book_info(self):
        return self.name, self.genre, self.pages


lib = library(200)
print(lib.isEmpty())
lib.add_books(50)
print(lib.num)
lib.remove_books(250)
print(lib.isEmpty())

b = book("Thomas Calculus", "Educational", 1450)
print(b.isPresent("Harry Potter"))
print(b.book_info())

b2 = book("The Hobbit", "Fantasy", 1200)
print(b2.isPresent("Thomas Calculus"))
print(b2.book_info())