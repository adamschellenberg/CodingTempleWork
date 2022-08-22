# Python Crash Course, Chapter 2
# Aug, 22, 2022 

# SECTION: Variables TRY IT YOURSELF, page 23
# 2-1 Simple Message:
message = "Hello"
print (message)

# 2-2 Simple Messages:
message_1 = "Hello"
print (message_1)
message_1 = message_1 + " World"
print (message_1)

####################

# SECTION: Strings TRY IT YOURSELF, page 29
# 2-3 Personal Message
name = "Adam"
print ("Hello " + name + ", would you like to play a game?")

# 2-4 Name Cases
name_1 = "Adam Schellenberg"
print (name_1.lower())
print (name_1.upper())
print (name_1.title())

# 2-5 Famous Quote + 2-6 Famous Quote 2
quote = "Simplicity is the ultimate sophistication."
famous_person = "LeOnArDo Da ViNcI"
quote_message = famous_person.title() + ' once said, "' + quote + '"'
print (quote_message)

# 2-7 Stripping Names
name_2 = "    I am\tAdam\n\tSchellenberg. Nice to meet you.   "
print (name_2)
print (name_2.lstrip())
print (name_2.rstrip())
print (name_2.strip())

####################

# SECTION: Numbers TRY IT YOURSELF, page 33
# 2-8 Number Eight

print (4 + 4)
print (10 - 2)
print (4 * 2)
print (int(16 / 2))

# 2-11 Zen of Python
import this