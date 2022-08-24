# Python Crash Course, Chapter 7
# Aug 23, 2022

# SECTION How the input() Function Works TRY IT YOURSELF page 121
# 7-1 Rental Car
#car = input("What kind of car would you like to rent? ")
#print(f"Ah yes, the {car}. Very popular. Let me see if I can find you one.")

# 7-2 Restaurant Seating
#people = input ("How many will be in your group tonight? ")
#if int(people) > 8:
#    print ("Wow, popular are we? You'll have to wait for a table.")
#else:
#    print ("Oh, I see. Not too social, are we? Right this way.")

# 7-3 Multiples of Ten
#multiple_of_ten = input ("Tell me a number. Hurry! ")
#if int(multiple_of_ten) % 10 == 0:
#    print ("You know, that's a multiple of ten ( ͡~ ͜ʖ ͡°)")
#else:
#    print ("HA! That's not even a multiple of ten, noob! ")

# SECITION Introducing while Loops TRY IT YOURSELF pages 127-128
# 7-4 Pizza Toppings
# prompt = "Give me toppings one at a time, please."
# prompt += "Also, enter quit when you're done: "

# active = True
# while active:
#     topping = input(prompt)
#     if topping == "quit":
#         break
#     else:
#         print (f"Added {topping} to your pizza!\n")


# 7-5 Movie Tickets
# prompt = "Welcome to the movies. How old are you?\n"
# prompt += "Tell me 'stop' if I've asked you too many times: "
# active = True
# while active:
#     age = input(prompt)
#     cost = 0
#     if age.lower() == "stop":
#         break
#     elif int(age) < 3:
#         cost = 0
#     elif 3 <= int(age) <= 12:
#         cost = 10
#     elif int(age) > 12:
#         cost = 15
#     print (f"Your ticket will be ${cost}, please.\n")

# 7-6 Three Exits


# 7-7 Infinity



# SECTION Using a while Loop with Lists and Dictionaries TRY IT YOURSELF page 131
# 7-8 Deli
# sandwich_orders = ['pastrami', 'blt', 'spicy italian']
# completed_orders = []
# while sandwich_orders:
#     completed_sandwich = sandwich_orders.pop()
#     print (f"I made your {completed_sandwich}")
#     completed_orders.append(completed_sandwich)
# sandwiches = ""
# for sandwich in completed_orders:
#     sandwiches += sandwich + " "

# print (f"Bro, I just made these sandwiches: {sandwiches}")

# 7-9 No Pastrami
# sandwich_orders = ['pastrami', 'blt', 'pastrami', 'spicy italian', 'pastrami']

# print ("Sorry bro, no more pastrami.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print (sandwich_orders)

# 7-10 Dream Vacation
# active = True

# books = {}
# while active:
#     book = input("\nWhat book is that? ")
#     genre = input("What genre is that? ")
#     books[book] = genre

#     repeat = input("Got another book? (yes/no) ")
#     if repeat == "no":
#         active = False

# print ("\n--- Your books ---")
# for book, genre in books.items():
#     print(f"{book} is a {genre} book.")