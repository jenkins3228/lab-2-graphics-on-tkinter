from tkinter import *
from random import randint
import math
root = Tk()

root.title('LABA 2')
root.minsize(width=1080, height=720)
root.maxsize(width=1080, height=720)
canvas=Canvas(root,width=1080, height=720)
canvas.pack()

canvas.create_rectangle(0,612,1080,720, fill="#5f5f5f",outline="#484848")#асфальт
canvas.create_rectangle(0,655,1080,670, fill="white", outline="white")#линия на асфальте

class Rectangle:

    def __init__(self,points):
        self.rectangle=canvas.create_polygon(points)#right

    def rotate(self,points, angle, center):
        angle = math.radians(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * math.cos(angle) - y_old *  math.sin(angle)
            y_new = x_old *  math.sin(angle) + y_old * math.cos(angle)
            new_points.append([x_new + cx, y_new + cy])
        return new_points


    def draw_rectangle(self,points,i):
        canvas.coords(self.rectangle,points[0][0]+i,points[0][1],points[1][0]+i,points[1][1],points[2][0]+i,points[2][1],points[3][0]+i,points[3][1])


class Car:
    carImage=PhotoImage(file ="images/car.png")
    __car=0

    def __init__(self, points):
        self.__points = points
        self.createCar()

    def createCar(self):
        Car.__car=canvas.create_image(self.__points ,image=self.carImage, anchor=NW)


    def Move(self,speed):
        canvas.move(self.__car,speed,0)




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

LeftrectangleCenter = (leftVertices[3][0]-((leftVertices[3][0]-leftVertices[0][0])/2),leftVertices[2][1]- ((leftVertices[2][1]-leftVertices[0][1])/2))
RightrectangleCenter = (rightVertices[3][0]-((rightVertices[3][0]-rightVertices[0][0])/2),rightVertices[2][1]- ((rightVertices[2][1]-rightVertices[0][1])/2))

new_square=leftVertices
new_square1=rightVertices


car=Car([29,407])

leftRectangle=Rectangle(leftVertices)
rightRectangle=Rectangle(rightVertices)

Speed=30
i=0
def main():
    global new_square,new_square1,i
    i+=Speed

    new_square = leftRectangle.rotate(new_square,20, LeftrectangleCenter)
    new_square1 = rightRectangle.rotate(new_square1,20, RightrectangleCenter)

    car.Move(Speed)
    leftRectangle.draw_rectangle(new_square,i)
    rightRectangle.draw_rectangle(new_square1,i)
    root.after(100,main)
    
main()

root.mainloop()