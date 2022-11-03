from pyparsing import col
from pytimedinput import timedInput
import random
import pyfiglet
import os
from colorama import Fore,init
import time
#PRODUCES THE BASIC SETUP AREA
init(autoreset = True)
def print_field():
    for cell in CELLS:
        if cell in Snake_bod:
            print(Fore.LIGHTGREEN_EX + "0", end = "")
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0,FIELD_HEIGHT - 1):
            print("#", end = "")
        elif cell == apple_position:
            print(Fore.RED + "Õ", end = "")
        else:
            print(" ", end = "")
        if cell[0] == FIELD_WIDTH - 1:
            print("")

def update_snake():
    global eaten
    new_head = Snake_bod[0][0] + direction[0], Snake_bod[0][1] + direction[1]
    Snake_bod.insert(0,new_head)
    
    if not eaten:
        Snake_bod.pop(-1) 
    eaten = False

    

def apple_eat():
    global apple_position, eaten
    if apple_position == Snake_bod[0]:
        apple_position = place_apple()
        eaten = True

def place_apple():
    col = random.randint(1, FIELD_WIDTH - 2)
    row = random.randint(1, FIELD_HEIGHT - 2)

    while (col, row) in Snake_bod:
        col = random.randint(1, FIELD_WIDTH - 2)
        row = random.randint(1, FIELD_HEIGHT - 2)
    
    return (col, row)

#Settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range (FIELD_HEIGHT) for col in range(FIELD_WIDTH)]


#Snake
Snake_bod = [(5,FIELD_HEIGHT// 2), (4,FIELD_HEIGHT// 2), (3,FIELD_HEIGHT// 2)]
DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
direction = DIRECTIONS["right"]



eaten = False

#Apple
apple_position = place_apple()

ASCII_title = pyfiglet.figlet_format("WELCOME TO TERMINAL SNAKE!", font='isometric1')
print(ASCII_title)
print("Up = W \nDown = S \nRight = A\n Left = D \n Quit = Q")
time_skip = input("Skip? y- es n- o")


os.system("cls") #clears things

def countdown():
    time.sleep(60)
    t = 60
    while t>=0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    countdown()
while True:
    #clear the field
    os.system("cls") #clears things
    #field drawing 
    print_field()

    txt,_= timedInput("", timeout = 0.2)

    match txt:
        case "w": direction = DIRECTIONS["up"]
        case "a": direction = DIRECTIONS["left"]
        case "s": direction = DIRECTIONS["down"]
        case "d": direction = DIRECTIONS["right"]
        case "q": 
            os.system("cls")
            break
    
    #snake death
    if Snake_bod[0][0] in (0, FIELD_WIDTH - 1) or Snake_bod[0][1] in (0, FIELD_HEIGHT- 1):
        os.system("cls")
        print_field() == False
        print("GAME ENDED : YOU TOUCHED THE BORDER - ROOKIE MISTAKE")
        print("PRESS Q TO QUIT")
    elif Snake_bod[0] in Snake_bod[1:]:
        os.system("cls")
        print_field() == False
        print("GAME ENDED : YOU TOUCHED YOURSELF")
        print("PRESS Q TO QUIT")

    
    update_snake()
    apple_eat()
