# Python Crash Course, Chapter 5
# Aug 23, 2022

# SECTION Conditional Tests TRY IT YOURSELF page 82
# 5-1 Conditional Tests AND 5-2 More Conditional Tests
inventory = ['sword', 'shield', 'key' ,'potion']
item = 'key'
if item in inventory:
    inventory.remove(item)
    print('You managed to unlock the door, but your key broke.')
print(f'Inventory: {inventory}')

# 5-8 Hello Admin
usernames = ['admin', 'client', 'employee']
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f'Hello {user}. Would you like a status report?')
        else:
            print(f'Welcome back {user}!')

# 5-11 Ordinal Numbers
numbers = [value for value in range (1, 10)]
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

number = 8
if True:
    print ("test")