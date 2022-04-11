#Crack the bouncing egg

import pgzrun # pip install pgzero
#set the size of the screen (window)
WIDTH = 800
HEIGHT = 600

change_x = 2
change_y = 2
halt = False

#define an actor object
golden_egg = Actor('golden_egg', pos = (100,100))

def draw(): #auto invoked by pygame zero to refresh the screen
    #clear the screen and set it to black background
    screen.clear()

    #have a background image applied on the screen
    screen.blit(image = 'farm', pos = (0,0)) #looks for images/farm.png

    #draw the actor
    golden_egg.draw()

#event procedure : a callback function that auto executes on event mouse down
def on_mouse_down(pos, button):
    global halt
    if button == mouse.LEFT and golden_egg.collidepoint(pos):
        golden_egg.image = 'broken-golden'
        #music.play('egg_cracking') #plays in a loop
        music.play_once('egg_cracking')  # plays once
        music.set_volume(1) #full volume
        halt = True

#event procedure : a callback function that auto executes on event mouse up
def on_mouse_up():
    global halt
    golden_egg.image = 'golden_egg'
    halt = False


def update(): #auto invoked by pygame zero per FRAME
    if not halt:
        global change_x, change_y
        if golden_egg.left+ golden_egg.width >= WIDTH   or golden_egg.left <=0:
            change_x = change_x * -1
        if golden_egg.top + golden_egg.height >= HEIGHT   or golden_egg.top <= 0:
            change_y = change_y * -1

        golden_egg.left += change_x
        golden_egg.top += change_y


pgzrun.go() #should be the last line of the application