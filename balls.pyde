xCoordinate =20
yCoordinate
speed= 10
ellipseSize= 35
def setup():
    size(400, 400)

    
def draw():
    background (0)
    global xCoordinate, yCoordinate, yspeed, speed, ellipseSize
    leftBoundary= ellipseSize/ 2
    rightBoundary= 400- ellipseSize/ 2
    if xCoordinate >=rightBoundary or xCoordinate <=leftBoundary:
        speed= -speed
    xCoordinate +=speed
    fill (255, 255, 0)
    ellipse (xCoordinate, 40, ellipseSize, ellipseSize)
    ellipse (xCoordinate, 80, ellipseSize, ellipseSize)
    ellipse (xCoordinate, 200, ellipseSize, ellipseSize)
