import tkinter as tk
import random

def move():
    global x
    global y
    global pasX
    global pasY

    canvas1.move(circle, pasX, pasY)
    coordinates = canvas1.coords(circle)

    x = coordinates[0]
    y = coordinates[1]

    # if outside screen move to start position
    if y <= 1:
        pasY = 10        
        canvas1.coords(circle, x, y, x+width, y+height)
    if x <= 1:
        pasX = 10
        canvas1.coords(circle, x, y ,x+width, y+height)
    if x >= g_width-width:
        pasX = -10
        canvas1.coords(circle, x, y ,x+width, y+height)
    if y >= g_height-height:
        pasY = -10
        canvas1.coords(circle, x, y ,x+width, y+height)

    window.after(333, move)

# --- main ---

start_x = 1
start_y = 1

x = start_x
y = start_y

g_height=1001
g_width=1001

width  = 10
height = 10

pasX = 10
pasY = -10

window = tk.Tk()
window.geometry("1000x1000")

canvas1 = tk.Canvas(window, height=g_height, width=g_width)
canvas1.grid(row=0, column=0, sticky='w')
coord = [x, y, x+width, y+height]
for x in range(1,g_width+1, 10):
    canvas1.create_line(x, 1, x, g_height)
    canvas1.create_line(1, x, g_width, x)


circle = canvas1.create_oval(coord, outline="red", fill="red")


move()

window.mainloop ()

