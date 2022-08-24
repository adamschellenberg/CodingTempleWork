# Python Crash Course, Chapter 3
# Aug 22, 2022

# SECTION: What Is a List? TRY IT YOURSELF, page 40
# 3-1 Names
names = ['Adam', 'Jenifer', 'Levi', 'Annabelle', 'Easton']
for index, x in enumerate(names):
    print(x)

# 3-2 Greetings
message = 'Whaddup'
for index, x in enumerate(names):
    print(message + ' ' + x + '?')

# 3-3 Your Own List
favorite_pokemon = ['Bulbasaur', 'Leafeaon', 'Chikorita', 'Hoothoot', 'Corviknight']
for index, x in enumerate(favorite_pokemon):
    print('I would like to catch a ' + x + '.')

# SECTION Removing Elements from a List TRY IT YOURSELF, page 46
# 3-4 Guest List
people_to_invite = ['Ash Ketchum', 'Tracey Sketchit', 'Todd Snap']
def PrintInvitations():
    for index, x in enumerate(people_to_invite):
        print("Dear " + x + ", \n Please come over for dinner! I'll keep asking until you do!")

PrintInvitations()

# 3-5 Changing Guest List
print ("... I guess " + people_to_invite[2] + " can't make it...")
people_to_invite[2] = "Samuel Oak"
PrintInvitations()

# 3-6 More Guests
print ("Good news, everyone! I found a bigger table!")
people_to_invite.insert(0, "Bender B Rodriguez")
people_to_invite.insert(2, "Philip J Fry")
people_to_invite.append("Turanga Leela")
PrintInvitations()

# 3-7 Shrinking Guest List
print ("Well this is awkward. The idiots at the dmv messed up our reservation. Now I can only invite two of you!")
while len(people_to_invite) > 2 :
    popped_name = people_to_invite.pop()
    print("Sorry, " + popped_name + ", you are the weakest link.")
for index, x in enumerate(people_to_invite):
    print("Don't worry, " + x + ", you're still invited!")
while len(people_to_invite) > 0:
    del people_to_invite[0]
print(people_to_invite)

# SECTION Organizing a List TRY IT YOURSELF page 50
# 3-8 Seeing the World
places_to_visit = ["Japan", "Canada", "Xbox HQ", "New York", "Nintendo HQ"]
print (places_to_visit)
print (sorted(places_to_visit))
print (places_to_visit)
print (sorted(places_to_visit, reverse=True))
print (places_to_visit)
places_to_visit.reverse()
print (places_to_visit)
places_to_visit.reverse()
print (places_to_visit)
places_to_visit.sort()
print (places_to_visit)
places_to_visit.sort(reverse=True)
print (places_to_visit)

# 3-9 Dinner Guests
people_to_invite_1 = ['Ash Ketchum', 'Tracey Sketchit', 'Todd Snap']
print (len(people_to_invite_1))

# 3-10 Every Function (append, insert, del, pop, remove, sort, sort reverse, sorted, reverse, len)
languages = ["German", "Spanish"]
languages.append("English")
languages.insert(0, "Japanese")
del languages[1]
popped_language = languages.pop()
languages.remove ("Spanish")
sorted_languages = sorted(languages)
languages.reverse()
languages.sort()
languages.sort(reverse=True)
len(languages)

# 3-11 Intentional Error
# del languages[20]