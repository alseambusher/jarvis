import math
from basic import dummy_object
#gets the best fit line
def best_fit_line(points):
    #TODO Fix this
    lines=[]
    line=dummy_object()
    #TODO put try catch block while finding slope
    line.slope=0
    line.start_point=[0,0]
    line.end_point=[0,0]
    lines.append(line)
    return lines
def gesture_extract(points):
    lines=best_fit_line(points)
    gesture=[]
    for line in lines:
        if abs(line.slope)<slope(10):#straight line
            if line.start_point[0]<line.end_point[0]:#left ->right
                gesture.append("SLR")
            else: #right -> left
                gesture.append("SRL")
        elif abs(line.slope)<=slope(90) and abs(line.slope)>=slope(80):#vertical line
            if line.start_point[1]<line.end_point[1]:#bottom ->top
                gesture.append("VBT")
            else: #top ->bottom
                gesture.append("VTB")
    return gesture
#finds tan of angle in degrees
def slope(angle):
    return math.tan((angle*math.pi)/180)
