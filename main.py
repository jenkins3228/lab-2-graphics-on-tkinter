from Classes import *
from configuration import *

LeftrectangleCenter = (leftVertices[3][0]-((leftVertices[3][0]-leftVertices[0][0])/2),leftVertices[2][1]- ((leftVertices[2][1]-leftVertices[0][1])/2))
RightrectangleCenter = (rightVertices[3][0]-((rightVertices[3][0]-rightVertices[0][0])/2),rightVertices[2][1]- ((rightVertices[2][1]-rightVertices[0][1])/2))

car=Car([29,407])

leftRectangle=Rectangle(leftVertices)
rightRectangle=Rectangle(rightVertices)

mirror=Mirror(triangle)

testSquare=Scaling(oval,1,"yellow")

Speed=15
i=0

def main():
    global leftVertices,rightVertices,i
    i+=Speed
    # testSquare.scalingSquare()
    testSquare.scalingOval()

    mirror.startMirroring()

    leftVertices = leftRectangle.rotate(leftVertices,20, LeftrectangleCenter)
    rightVertices = rightRectangle.rotate(rightVertices,20, RightrectangleCenter)

    car.Move(Speed)
    leftRectangle.draw_rectangle(leftVertices,i)
    rightRectangle.draw_rectangle(rightVertices,i)
    root.after(100,main)
    
main()

root.mainloop()