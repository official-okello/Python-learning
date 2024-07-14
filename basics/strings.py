#capitalizes first letter of name, strips whitespaces
name = input('What is your name? ').strip().title()

#split string
first, last = name.split(' ')

print(f'Hello,  {name}')
print(f'Hey, {last}')