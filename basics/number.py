def main():
    x = get_int('Whats x? ')
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #or print('x is not an integer')
            pass

main()