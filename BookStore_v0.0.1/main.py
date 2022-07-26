import UserInterface

if __name__ == '__main__':
    run = UserInterface.UserInterface()
    run.create_user()
    while True:
        run.menu()
        run.select_choise()




