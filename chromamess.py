
from time import sleep
from ChromaPython import ChromaApp, ChromaAppInfo, ChromaGrid, ChromaColor

info = ChromaAppInfo()

info.DeveloperName = 'Chrigi2486'
info.DeveloperContact = 'Don\'t contact me lol'
info.Category = 'application'
info.SupportedDevices = ['keyboard']
info.Description = 'ChromaMess'
info.Title = 'Mess'

app = ChromaApp(info)

sleep(2)  # initial sleep to let the application load (takes 2 seconds)

keyboard = app.Keyboard

# grid = ChromaGrid('Keyboard')

# grid.set(0, 255, 0)
# keyboard.setCustomGrid(grid)
# keyboard.applyGrid()
keyboard.setStatic(ChromaColor(0, 0, 0))  # sets color to black/off

sleep(2)

for y in range(keyboard.MaxRow-1, -1, -1):  # goes through all keys one at a time and sets the colour
    for x in range(keyboard.MaxColumn):
        keyboard.setPosition(ChromaColor(255, 0, 0), x=x, y=y)
        keyboard.applyGrid()
        sleep(0.01)
for x in range(keyboard.MaxColumn-1, -1, -1):  # same as before but in a different order
    for y in range(keyboard.MaxRow):
        keyboard.setPosition(ChromaColor(0, 255, 0), x=x, y=y)
        keyboard.applyGrid()
        sleep(0.01)

newGrid = ChromaGrid('Keyboard')
newGrid.set(0, 255, 0)  # makes the whole grid (all the keys in the grid) green. Basically cycles through them and makes every individual one green

for x in range(len(newGrid)):  # makes every column red going downwards
    for y in range(len(newGrid[x])):
        newGrid[x][y].set(255, 0, 0)  # this is how you set the color of a key (key.set(r, g, b)) keys are of the ChromaColor class so basically you're changing the color of a ChromaColor object
    keyboard.setCustomGrid(newGrid)  # tells it which grid to use
    keyboard.applyGrid()  # updates the keyboard to use the grid set
    sleep(0.1)

ymax = keyboard.MaxColumn
for y in range(int(ymax/2)):  # this colours the keys blue coming from the sides, approaching the middle and stopping there
    for x in range(len(newGrid)):
        newGrid[x][0+y].set(0, 0, 255)
        newGrid[x][ymax-1-y].set(0, 0, 255)
    keyboard.setCustomGrid(newGrid)
    keyboard.applyGrid()
    sleep(0.03)


ymax = int(keyboard.MaxColumn/2)
for y in range(ymax):  # this then does the opposite and colours the keys white from the middle outwards
    for x in range(len(newGrid)):
        newGrid[x][ymax+y].set(255, 255, 255)
        newGrid[x][ymax-y].set(255, 255, 255)
    keyboard.setCustomGrid(newGrid)
    keyboard.applyGrid()
    sleep(0.03)

for x in range(len(newGrid)):  # turns off all keys per column from top to bottom
    for y in range(len(newGrid[x])):
        newGrid[x][y].set(0, 0, 0)
    keyboard.setCustomGrid(newGrid)
    keyboard.applyGrid()
    sleep(0.05)

# this is then the rainbow yay :D

steps = 63  # vmax divided by amount of rows on the keyboard
vmax = 252  # this is 252 not 255 because 255 isn't a multiple of the amount of rows on the keyboard
r = vmax  # sets the r value to max to begin with
g = 0  # sets the g value to the minimum
b = 0  # same
up = None
down = None
rainbowGrid = ChromaGrid('Keyboard')

# What we want to do to create a rainbow is to start with red, then increase g to the max, then reduce r, then increase b, then reduce g, then increase r, then reduce b
# Basically cycling through all the colors to create a rainbow
# This fist one will only make a still standing rainbow

for y in range(keyboard.MaxColumn):
    for x in range(keyboard.MaxRow):  # sets a whole row with the rgb value then move on to the next
        rainbowGrid[x][y].set(r, g, b)
    if up == 'r':
        r += steps
    elif up == 'g':
        g += steps
    elif up == 'b':
        b += steps
    elif down == 'r':
        r -= steps
    elif down == 'g':
        g -= steps
    elif down == 'b':
        b -= steps
    if g == 0 and b == 0:
        up = 'g'
        down = None
    elif r == 0 and g == 0:
        up = 'r'
        down = None
    elif r == 0 and b == 0:
        up = 'b'
        down = None
    elif r == vmax and g == vmax:
        up = None
        down = 'r'
    elif b == vmax and g == vmax:
        up = None
        down = 'g'
    elif r == vmax and b == vmax:
        up = None
        down = 'b'

    keyboard.setCustomGrid(rainbowGrid)
    keyboard.applyGrid()
    sleep(0.05)

sleep(0.05)

# this is now the moving rainbow

reverse = False  # if you want to go backwards change this to true

while True:  # runs forever cause you won't ever find the end of the rainbow ;)
    for x in range(len(rainbowGrid)):
        for y in range(len(rainbowGrid[x])):  # gets the current rgb value of the key and sets it to the next one
            if reverse:
                r, g, b = rainbowGrid[x][y].getRGB()  # gets the rgb value
            else:
                b, g, r = rainbowGrid[x][y].getRGB()  # does the same but in reverse if you set reverse to False, this one is used
            if r and g == vmax:
                r -= steps
            elif g and b == vmax:
                g -= steps
            elif b and r == vmax:
                b -= steps
            elif not r and b != vmax:
                b += steps
            elif not b and g != vmax:
                g += steps
            elif not g and r != vmax:
                r += steps
            if reverse:
                rainbowGrid[x][y].set(r, g, b)
            else:
                rainbowGrid[x][y].set(b, g, r)
    keyboard.setCustomGrid(rainbowGrid)
    keyboard.applyGrid()
    sleep(0.05)
