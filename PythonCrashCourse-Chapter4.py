# Python Crash Course, Chapter 4
# Aug 23, 2022

# SECTION Avoiding Indentation Errors TRY IT YOURSELF page 60
# 4-1 Pizzas
from audioop import mul


pizzas = ['pepperoni', 'cheese', 'combo']
for pizza in pizzas:
    print (pizza.title() + ' is one of my favorite kinds of pizza.')
print ('Clearly, I like pizza.')

# 4-2 Animals
animals = ['zebra', 'turtle', 'squirrel']
for animal in animals:
    print('A ' + animal + ' would make an okay pet, I guess...')
print ("Honestly, I don't really like pets. You do you, though.")

# SECTION Making Numerical Lists TRY IT YOURSELF page 64
# 4-3 Counting to Twenty
numbers = [number for number in range(1,21)]
print (numbers)

# 4-4 One Million
millions = [number for number in range(1,1000001)]
#for number in millions:
#    print (number)

# 4-5 Summing a Million
print(min(millions))
print(max(millions))
print(sum(millions))

# 4-6 Odd Numbers
odd_numbers = [number for number in range(1, 21, 2)]
print (odd_numbers)

# 4-7 Threes
multiples_of_three = [multiple for multiple in range (3,31, 3)]
for multiple in multiples_of_three:
    print(multiple)

# 4-8 Cubes AND 4-9 Cube Comprehension
cubes = [cube**3 for cube in range (1, 11)]
for cube in cubes:
    print(cube)

# SECTION Working with Part of a List TRY IT YOURSELF page 69
