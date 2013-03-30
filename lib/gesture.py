import cv
import math
from basic import dummy_object

all_gestures={}
#reads gestures from JSON file
def read_gestures():
    fp=open("../gestures.JSON")
    all_gestures=eval(fp.readlines()[0][:-1])
    return all_gestures

#returns states through which the points have passed through
def gesture_extract(points):
    lines=extract_lines(points)
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
        elif line.slope<0:
            # inclined left(IL)
            # .
            #  .
            #   .
            if line.start_point[0]<line.end_point[0]:#left ->right
                gesture.append("ILLR")
            else: #right -> left
                gesture.append("ILRL")
        else: #inclined right(IR)
            if line.start_point[0]<line.end_point[0]:#left ->right
                gesture.append("IRLR")
            else: #right -> left
                gesture.append("IRRL")

    return gesture

def extract_lines(points):
    #TODO
    pass
#gets the best fit line, returns line with slope,start_point,end_point
def best_fit_line(line_points):
    x0,y0,vx,vy=cv.FitLine(line_points,cv.CV_DIST_L2,0,0.01,0.01)
    line=dummy_object()
    try:#handle infinite slope
        line.slope=vy/vx
    except:
        line.slope=slope(90)
    line.start_point=line_points[0]
    line.end_point=line_points[-1]
    return line

#finds tan of angle in degrees
def slope(angle):
    return math.tan((angle*math.pi)/180)

def search_gesture(points):
    gestureEXTRACT=gesture_extract(points)
    for gesture in all_gestures.iterkeys():
        if gestureEXTRACT==all_gestures[gesture]:
            return gesture

