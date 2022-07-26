import Book


class BooksList:
    list = []

    def __get_id(self):
        if len(self.list) == 0:
            id = 1
        else:
            last_book = len(self.list) - 1
            id = self.list[last_book]._id + 1

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

        price = input("Price for book: ")
        if price == "":
            price = 0
        else:
            price = price.replace(',', '.')
        price = float(price)

        id = self.__get_id()
        book = Book.Book(id, author, title, price)
        self.list.append(book)

    def remove_book(self):
        print("Input 'ID' of book to delete.")
        id = int(input())
        for book in self.list:
            if book._id == id:
                self.list.remove(book)
            else:
                print("Invalid book's ID.")

    def print_list(self):
        if len(self.list) == 0:
            print("\nBook's list is empty.\n")
        else:
            for book in self.list:
                print(f'\n{book.show_book_info()}')
