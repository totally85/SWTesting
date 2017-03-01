import math
def distance(x1,x2,y1,y2):
    xValues=(x2-x1)*(x2-x1)
    yValues=(y2-y1)*(y2-y1)
    dist=math.sqrt(xValues+yValues)
    return dist
    print("Distance function")
