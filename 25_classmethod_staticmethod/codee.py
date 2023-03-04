class Book:
    TYPES = ("hardcover", "paperback")

# print(Book.TYPES)

def __init__(self, name, book_type, weight):
    self.name = name
    self.book_type = book_type
    self.weight = weight

def __repr__(self):
    return f"Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls):
        return cls(name, cls.TYPES[1], page_weight)
    

    book = Book.hardcover("Harry Potter", 1500)
    light = Book.paperback("Python", 600)

    print(book)
    print(light)