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
# 4-10 Slices
print('The first three items in the list are: ' + str(odd_numbers[:3]))
print('The middle three items in the list are: ' + str(odd_numbers[3:6]))
print('The last three items in the list are: ' + str(odd_numbers[-3:]))

# 4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append('veggie')
friend_pizzas.append('hawaiian')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 4-12 More Loops
foods_py_1 = ['pizza', 'falafel', 'carrot cake']
foods_py_2 = ['pizza', 'falafel', 'carrot cake', 'ice cream']

print("The first list of foods.py is:")
for food in foods_py_1:
    print(food)

print("The second list of foods.py is:")
for food in foods_py_2:
    print(food)


# SECTION Tuples TRY IT YOURSELF page 71
# 4-13 Buffet
buffet_foods = ('Sushi', 'Ramen' ,'Teriyaki' ,'BBQ' ,'Rice')
for food in buffet_foods:
    print(food)
# buffet_foods[0] = 'Butter'
buffet_foods = ('Sushi', 'Ramen' ,'Teriyaki' ,'Tempura' ,'Taiyaki')
for food in buffet_foods:
    print(food)