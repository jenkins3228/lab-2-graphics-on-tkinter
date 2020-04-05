# from tkinter import *

from tkinter import PhotoImage,Canvas,Tk,NW
from random import randint
import math
root = Tk()

root.title('LABA 2')
root.minsize(width=1080, height=720)
root.maxsize(width=1080, height=720)
canvas=Canvas(root,width=1080, height=720)
canvas.pack()

canvas.create_rectangle(0,612,1080,720, fill="#484848",outline="#484848")#асфальт
canvas.create_rectangle(0,655,1080,670, fill="white", outline="white")#линия на асфальте

leftVertices = [
    [70, 528],
    [70, 603],
    [151, 603],
    [151, 528],
]
rightVertices = [
    [289, 528],
    [289, 603],
    [368, 603],
    [368, 528],
]

square = [
    [281, 81],
    [281, 162],
    [375, 161],
    [375, 81],
]

oval = [
    [870, 16],
    [1060, 184],
]

triangle = [
    [132, 188],
    [132, 270],
    [220, 228],
]

