from Classes import *

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

square = [
    [281, 81],
    [281, 162],
    [375, 161],
    [375, 81],
]


testSquare=Scaling(square)
# testSquare.scalingSquare()

Speed=30
i=0

def main():
    global new_square,new_square1,i
    i+=Speed
    # testSquare.scalingSquare(i)
    
    new_square = leftRectangle.rotate(new_square,20, LeftrectangleCenter)
    new_square1 = rightRectangle.rotate(new_square1,20, RightrectangleCenter)

    car.Move(Speed)
    leftRectangle.draw_rectangle(new_square,i)
    rightRectangle.draw_rectangle(new_square1,i)
    root.after(100,main)
    
main()

root.mainloop()