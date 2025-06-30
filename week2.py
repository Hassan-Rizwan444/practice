class library:
    def __init__(self, num):
        self.num = num
    
    def isEmpty(self):
        if (self.num <= 0):
            return True
        else:
            return False    

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
    