from tkinter import *
from random import randint
import math
root = Tk()

root.title('ROCK')
root.minsize(width=1080, height=720)
root.maxsize(width=1080, height=720)
canvas=Canvas(root,width=1080, height=720)
canvas.pack()

canvas.create_rectangle(0,612,1080,720, fill="#5f5f5f",outline="#484848")
canvas.create_rectangle(0,655,1080,670, fill="white", outline="white")

class Car:
    carImage=PhotoImage(file ="images/car.png")
    car=0

    def __init__(self, points):
        self.__points = points
        self.createCar()

    def createCar(self):
        Car.car=canvas.create_image(self.__points ,image=self.carImage, anchor=NW)


    def Move(self):
        canvas.move(self.car,50,0)



car=Car([29,407])

def test():

    car.Move()
    root.after(100,test)
    
test()

root.mainloop()