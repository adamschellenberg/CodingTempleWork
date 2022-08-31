# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

from math import pi, floor

def calculateSqft(length, width):
    length = int(length)
    width = int(width)
    sqft = length * width
    print('Square footage is {}'.format(sqft))

def calculateCircum(diameter):
    circumference = int(diameter) * pi
    print('Circumference is {}'.format(floor(circumference)))