# QUESTION 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function
def hello_name(user_name):
    print(f"Hello {user_name}!\n")
hello_name("Spider-Man")

# QUESTION 2
# Write a python function, first_odds that prints the
# odd numbers from 1-100 and returns nothing
def first_odds():
    for number in range(1,101):
        if number % 2 == 1:
            print(number)
first_odds()

# QUESTION 3
# Please write a Python function, max_num_in_list to return the max
# number of a given list.
def max_num_in_list(a_list):
    print(f'\n{max(a_list)}')
list = [1,2,3,4,10,0]
max_num_in_list(list)

# QUESTION 4
# Write a function to return if the given year is a leap year.
# A leap year is divisble by 4, but not divisible by 100, unless
# it is also divisible by 400. The return should be a bool
def is_leap_year(a_year):
    leap_year = False
    if a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
    elif a_year % 4 == 0 and a_year % 400 == 0:
        leap_year = True
    return leap_year
print (f'\n{is_leap_year(2000)}')
print (f'{is_leap_year(2100)}')


# QUESTION 5
# Write a function to check to see if all numbers in list are consecutive numbers
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not. The return should be a bool
def is_consecutive(a_list):
    is_consecutive = False
    for number in range(0,len(a_list)-1):
        if a_list[number] + 1 == a_list[number + 1]:
            is_consecutive = True
        else:
            is_consecutive = False
            break
    return is_consecutive
not_consecutive = [1,2,2,6,7]
print(f'\n{is_consecutive(not_consecutive)}')
consecutive = [2,3,4,5,6]
print(is_consecutive(consecutive))