class Book:
    TYPES = ("hardcover", "paperback")

# print(Book.TYPES)

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book {self.name}, {self.book_type}, weighing {self.weight}g"

        # "Book" needs to be in quotation marks " ", if it is under the same class otherwise we don't need to use " " marks.  
        @classmethod
        def hardcover(cls, name: str, page_weight: int) -> "Book":
            return cls(name, cls.TYPES[0], page_weight + 100)
        
        @classmethod
        def paperback(cls):
            return cls(name, cls.TYPES[1], page_weight)
        

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python", 600)

print(book)
print(light)