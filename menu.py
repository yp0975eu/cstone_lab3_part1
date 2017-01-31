class Menu:

    menu_options = ['create', 'find', 'update', 'delete', 'quit']
    find_options = ['find by name', 'find by country', 'find by catches']

    def __init__(self):
        pass

    @staticmethod
    def display(options):
        #empty newline
        print()
        menu_num = 1
        for value in options:
            print(menu_num, value)
            menu_num += 1

    @staticmethod
    def get_user_input(options):
        while True:
            try:
                selection = int(input('\n'))
                if selection not in range(len(options) + 1):
                    print("\nWas that a valid menu option?")
                    pass
                else:
                    return selection

            except ValueError as ve:
                print("\nWas that a number?")

            except KeyboardInterrupt as ki:

                exit('Goodbye')


    @staticmethod
    def print_results(data):
        if len(data) == 0:
            print('We got nothing. Sorry.')
        else:
            print(data)


class Dialogs:

    @staticmethod
    def show_create():

        name = input('Enter name\n')

        country = input('Enter country\n')

        catches = Dialogs.get_int_input('Enter number of catches\n')

        return name, country, catches

    @staticmethod
    def get_string_input(message):
        while True:
            try:
                search_string = input(message)
                return search_string
            except ValueError as ve:
                print('Find by name error')

    @staticmethod
    def get_int_input(message):
        while True:
            try:
                number_input = int(input(message))
                return number_input

            except ValueError as ve:
                print("\nWas that a number?\n")

