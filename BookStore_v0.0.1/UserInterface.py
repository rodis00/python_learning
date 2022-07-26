import time

import readchar
import BooksList


class UserInterface:

    __choice: int

    def menu(self):
        print("\n\nWhat do you want to do?")
        print()
        print("1. Show available books.")
        print("2. Add book.")
        print("3. Delete book.")
        print("4. Exit program.")
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
            print("\nThanks for testing app :)")
            time.sleep(1.5)
            exit()
        else:
            print("Incorrect number of choices.\n")
