from screen import Screen
from Game_GUI import GUI
import mods

width=600
height=600
del_x=700
del_y=300
color="green"

screen=Screen(width,height,del_x,del_y,color)
gui=GUI(screen)

while not gui.quite:
    if gui.mode_1:
        mods.mode_1(screen)
    else:
        mods.mode_2(screen)
    gui.End_Screen()

