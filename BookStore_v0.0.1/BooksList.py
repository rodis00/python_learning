import Book
import UserInterface


class BooksList:
    _list = []

    def __get_id(self):
        if len(self._list) == 0:
            id = 1
        else:
            last_book = len(self._list) - 1
            id = self._list[last_book]._id + 1

        return id

    def add_book(self):
        author = input("Author full name: ")
        if author == "":
            author = "None"
        else:
            author = author.title()

        title = input("Title of book: ")
        if title == "":
            title = "None"
        else:
            title = title.title()
            for book in self._list:
                if book._title == title:
                    print("This book is in the list.")
                    UserInterface.UserInterface.wait()
                    book._quantity += 1
                    print("Quantity has been increased.")

                    return

        price = input("Price for book: ")
        if price == "":
            price = 0
        else:
            price = price.replace(',', '.')
        price = float(price)

        quantity = int(input("Quatity: "))

        id = self.__get_id()

        book = Book.Book(id, author, title, price, quantity)
        self._list.append(book)

    def remove_book(self):
        print("Input 'ID' of book to delete.")
        id = int(input())
        for book in self._list:
            if book._id == id:
                self._list.remove(book)
            else:
                print("Invalid book's ID.")

    def print_list(self):
        if len(self._list) == 0:
            print("\nBook's list is empty.\n")
        else:
            for book in self._list:
                if book._quantity == 0:
                    self._list.remove(book)
                print(f'\n{book.show_book_info()}')
