x = float(input('What is x? '))
y = float(input('What is y? '))

z = round(x + y)

print(f'{z:,}')

z = x/y
#z = round(x/y, 2)

print(f'{z:.2f}')