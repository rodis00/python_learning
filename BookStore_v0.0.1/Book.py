class Book:
    _id: int
    _author: str
    _title: str
    _price: float

    def __init__(self, id, author, title, price):
        self._id = id
        self._author = author
        self._title = title
        self._price = price

    def show_book_info(self):
        return f"ID = {self._id}\nTitle = {self._title}\nAuthor = {self._author}\nPrice = {self._price}\n"

