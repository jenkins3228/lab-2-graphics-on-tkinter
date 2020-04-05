from configuration import *

class Rectangle:

    def __init__(self,points):
        self.rectangle=canvas.create_polygon(points)

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

class Scaling:
    i=0
    def __init__(self,points,color="red"):
        if len(points)==2:
            self.__oval=canvas.create_oval(points,fill=color)
        else:
            self.points=points
            self.__square=canvas.create_polygon(points,fill=color)


    def scalingSquare(self,i):
        canvas.coords(self.__square,self.points[0][0]-i,self.points[0][1]-i,self.points[1][0]-i,self.points[1][1]+i,self.points[2][0]+i,self.points[2][1]+i,self.points[3][0]+i,self.points[3][1]-i)
