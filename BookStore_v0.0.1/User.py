import BooksList
import UserInterface


class User:
    _name: str
    _surname: str
    __address: str
    __phone_number: str
    __own_books: list

    def __init__(self, name, surname, address, phone_number):
        self._name = name
        self._surname = surname
        self.__address = address
        self.__phone_number = phone_number
        self.__own_books = []

    def show_user_data(self):
        print(f"Name and Surname: {self._name} {self._surname}\nAddress: {self.__address}\nPhone number: {self.__phone_number}\nBooks id:")
        for book in self.__own_books:
            print(book._id)

    def buy_book(self):
        print("Select book's ID to buy book.")
        choice = int(input("--> "))
        for book in BooksList.BooksList._list:
            if book._id == choice:
                self.__own_books.append(book)
                book._quantity -= 1
                print("\nBook added to your list.")
                UserInterface.UserInterface.wait()
