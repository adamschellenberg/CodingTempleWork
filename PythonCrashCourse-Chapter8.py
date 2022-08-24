# Python Crash Course, Chapter 8
# Aug 23, 2022

# SECTION Defining a Function TRY IT YOURSELF page 135
# 8-1 Message
def display_message():
    print ("This chapter is about functions")
display_message() 

# 8-2 Favorite Book
def favorite_book(title):
    print (f"One of my facorite books is {title}")
favorite_book("Halo: Fall of Reach")


# SECTION Passing Arguments TRY IT YOURSELF page 141
# 8-3 T-Shirt
def make_shirt(size, text):
    print(f"Making a {size} size shirt, and printing '{text}' on it.")
make_shirt("Large", "Hello World")
make_shirt(size="Medium", text="Hello Again")

# 8-4 Large Shirts
def make_large_shirt(size="large", text="I love Python"):
    print(f"Making a {size} size shirt, and printing '{text}' on it.")
make_large_shirt()
make_large_shirt("medium")
make_large_shirt("small", "This is functional")

# 8-5 Cities



# SECTION Return Values TRY IT YOURSELF page 146
# 8-6 City Names
def city_country(city, country):
    return f'"{city}, {country}"'
print (city_country("Salta", "Argentina"))

# 8-7 Album
def make_album(artist, album_title, number_of_tracks=""):
    if number_of_tracks:
        return {'artist': artist, 'album': album_title, 'number of tracks': int(number_of_tracks)}
    else:
        return {'artist': artist, 'album': album_title}
print (make_album("Alesana", "The Emptiness"))
print (make_album("I See Stars", "Digital Renegade", "15"))

# 8-8 User Albums
def user_albums(artist, album_title, number_of_tracks):
    if number_of_tracks:
        return {'artist': artist, 'album': album_title, 'number of tracks': int(number_of_tracks)}
    else:
        return {'artist': artist, 'album': album_title}
adding_albums = True
albums = []
while adding_albums:
    print("\nEnter 'q' to quit at any time")
    print("Enter album information")

    artist = input("Artist name (required): ")
    if artist == 'q':
        break

    album_title = input("Album title (required): ")
    if artist == 'q':
        break

    number_of_tracks = input("Number of tracks (optional): ")
    if artist == 'q':
        break
    albums.append(user_albums(artist, album_title, number_of_tracks))
print(f"Here's a list of all of your albums:\n {albums}")
# SECTION Passing a List TRY IT YOURSELF page 150
# 8-9 Magicians


# 8-10 Great Magicians


# 8-11 Unchanged Magicians



# SECTION Passing an Arbitrary Number of Arguments TRY IT YOURSELF page 154
# 8-12 Sandwiches


# 8-13 User Profile


# 8-14 Cars



# SECTION Styling Functions TRY IT YOURSELF page 159
# 8-15 Printing Models


# 8-16 Imports


# 8-17 Styling Functions