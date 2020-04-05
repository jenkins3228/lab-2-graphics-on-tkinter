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
    def __init__(self,points,speed,color="red"):
        self.points=points
        self.speed=speed
        self.score=0
        self.__count=0
        self.counter=0

        if len(points)==2:
            self.oval=canvas.create_oval(points,fill=color ,outline=color)
 
        else:  
            self.__square=canvas.create_polygon(points,fill=color)

        
    def scalingSquare(self):
        self.score+=self.speed
        canvas.coords(self.__square,self.points[0][0]-self.score,self.points[0][1]-self.score,self.points[1][0]-self.score,self.points[1][1]+self.score,self.points[2][0]+self.score,self.points[2][1]+self.score,self.points[3][0]+self.score,self.points[3][1]-self.score)

    def scalingOval(self):
        self.score+=self.speed
        self.counter+=1
        key=11
        if (self.counter%key)==0:
            self.__count+=1
            self.score=0

        
        if (self.__count%2)!=0:
            self.points[0][0]-=self.score
            self.points[0][1]-=self.score
            self.points[1][0]+=self.score
            self.points[1][1]+=self.score
            canvas.coords(self.oval,self.points[0][0],self.points[0][1],self.points[1][0],self.points[1][1])
            canvas.itemconfig(self.oval, fill='yellow', outline='yellow')
        else:
            self.points[0][0]+=self.score
            self.points[0][1]+=self.score
            self.points[1][0]-=self.score
            self.points[1][1]-=self.score
            canvas.coords(self.oval,self.points[0][0],self.points[0][1],self.points[1][0],self.points[1][1])
            canvas.itemconfig(self.oval, fill='#B0AEA7', outline="#B0AEA7")
