from turtle import *
import json
import time
import numpy as np

class Cellules():
    def __init__(self, cellule_size=(62, 62), cellules=(10, 10), width=5, tspeed=0):
        self.cs = cellule_size
        self.width = width
        self.cellules = cellules
        self.speed = tspeed

    def start(self):
        dr = Screen()
        self.cellule = [[(int(self.cs[0]*i*-1), int(self.cs[1]*j)) for j in range(int(-1*(self.cellules[1])/2), int((self.cellules[1])/2))] for i in range(int(-1*self.cellules[0]/2), int(self.cellules[0]/2))]
        self.cellule = [i[::-1] for i in self.cellule[::-1]]
        print(self.cellule)
        dr.setup(width=1+self.cs[0]*self.cellules[0], height=1+self.cs[1]*self.cellules[1])
        width(5)
        speed(self.speed)

    def fill(self, go, colour):
        penup()
        goto(self.cellule[go[0]][go[1]][0], self.cellule[go[0]][go[1]][1])
        pendown()
        print(self.cellule[go[0]][go[1]][0], self.cellule[go[0]][go[1]][1])
        begin_fill()
        color(colour)
        width, height = self.cs
        left(180)
        for i in range(2):
            forward(width)
            right(90)
            forward(height)
            right(90)
        end_fill()

    def add(self, x, y):
        self.fill((x - int(self.cellules[0]/2), y - int(self.cellules[1]/2)), "black")

    def rm(self, x, y):
        self.fill((x - int(self.cellules[0]/2), y - int(self.cellules[1]/2)), "white")
    
    def connect(self, ends):
        d0, d1 = np.abs(np.diff(ends, axis=0))[0]
        if d0 > d1: 
            return np.c_[
                np.linspace(ends[0, 0], ends[1, 0], d0+1, dtype=np.int32),
                np.round(np.linspace(ends[0, 1], ends[1, 1], d0+1)).astype(np.int32)
            ] 
        else:
            return np.c_[
                np.round(np.linspace(ends[0, 0], ends[1, 0], d1+1)).astype(np.int32),
                np.linspace(ends[0, 1], ends[1, 1], d1+1, dtype=np.int32)
            ]

cellules = Cellules(cellules=(50, 50), cellule_size=(12.4, 12.4))
e = {"blockname": "glowstone", "coords": []}
tmp = []
cellules.start()

def buttonclick(x,y):
    print("{0}, {1}".format(int(x/cellules.cs[0]), int(y/cellules.cs[1])))
    if len(tmp) == 1:
        tmp.append([int(x/cellules.cs[0]), int(y/cellules.cs[1])])
        print(tmp)
        for coord in cellules.connect(np.array(tmp)):
            cellules.add(int(coord[0]), int(-1*coord[1]))
            e["coords"].append([int(coord[0]), int(-1*coord[1])])
        tmp.clear()

    else:
        tmp.append([int(x/cellules.cs[0]), int(y/cellules.cs[1])])


onscreenclick(buttonclick,1)

done()

print(e)

with open(f"results/{str(int(time.time()))}.json", "w") as s:
    s.write("".join(json.dumps(e, indent=4)))
