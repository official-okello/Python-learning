import datetime as dt

class Diary:
    def add_entry(self):
        time = dt.datetime.now()
        diary = 'diary.txt'
        entry = input('Entry: ')
        
        with open(diary, 'a') as file:
            file.write(str(time) + ': ' + entry + '\r')

    def view_entry(self, file):
        pass
    def edit_entry(self):
        pass
    def delete_entry(self):
        pass
    def display_entries(self):
        diary = 'diary.txt'
        with open(diary,'r') as file:
            for line in file:
                print(file.read())

welcome_message = '''----------------------------My Diary--------------------------------
Welcome to my diary...

1. Add entry
2. View entries
3. Delete entries
4. Exit
'''

while True:
    print(welcome_message)
    option = input('What do you want to do?(1, 2, 3 or 4): ')

    if option == '1':
        add_new = Diary()
        add_new.add_entry()
    elif option == '2':
        view_entries = Diary()
        view_entries.display_entries()
    elif option == '3':
        pass
    elif option == '4':
        exit()
    else:
        print('Please choose from option 1, 2, 3, 4')