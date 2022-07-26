import time

import readchar
import BooksList
import User


class UserInterface:

    __choice: int

    @staticmethod
    def wait(seconds=1.2):
        time.sleep(seconds)

    def create_user(self):
        global user
        print("\nPodaj swoje dane: ")
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone number: ")
        address = input("Address: ")
        user = User.User(name, surname, address, phone)

    def menu(self):
        print("\n\nWhat do you want to do?")
        print()
        print("1. Show available books.")
        print("2. Add book.")
        print("3. Delete book.")
        print("4. Buy book.")
        print("5. Show User info.")
        print("6. Exit program.")
        self.__choice = int(input("\nInput here your choice and press enter.\n--> "))
        # self.__choice = readchar.readkey()

    def select_choise(self):
        books_list = BooksList.BooksList()
        if self.__choice == 1:
            books_list.print_list()
        elif self.__choice == 2:
            books_list.add_book()
        elif self.__choice == 3:
            books_list.remove_book()
        elif self.__choice == 4:
            user.buy_book()
        elif self.__choice == 5:
            user.show_user_data()
        elif self.__choice == 6:
            print("\nThanks for testing app :)")
            UserInterface.wait()
            exit()
        else:
            print("Incorrect number of choices.\n")


