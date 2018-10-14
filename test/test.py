from asyncio import *

from tkinter import *

wn = Tk()
wn.title('KeyDetect')

def down(e):
    print (e.keysym.lower())

wn.bind('<KeyPress>', down)

wn.mainloop()

print("test")
gridx=5
gridy=5
grid=[[None for x in range(gridx)] for y in range(gridy)]
grid[4][0]=-1

def getNeighbors(x,y):
    neighbors=[]
    if(x+1<gridx):
        neighbors.append((x+1,y))
    if(x-1>=0):
        neighbors.append((x-1,y))
    if(y+1<gridy):
        neighbors.append((x,y+1))
    if(y-1>=0):
        neighbors.append((x,y-1))
    return neighbors

def dijkstra(grid,pos):
    frontier = []
    frontier.append(pos)
    distance = {}
    distance[pos] = 0

    while len(frontier)!=0:
       current = frontier.pop(0)
       #print(len(frontier),len(distance))
       print(distance)
       for next in getNeighbors(current[0],current[1]):
          if next not in distance:
             frontier.append(next)
             distance[next] = 1 + distance[current]

    print(distance)

dijkstra(grid,(0,0))
