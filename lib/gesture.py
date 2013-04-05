import cv
from config import GRID_NUM,ALLOWANCE,MIN_GRID_SIZE

all_gestures={}
#reads gestures from JSON file
def read_gestures():
    fp=open("data/gestures.JSON")
    all_gestures=eval(fp.readlines()[0][:-1])
    return all_gestures

#returns states through which the points have passed through
def gesture_extract(points):
    gesture=[]
    X=[ point[0] for point in points ]
    Y=[ point[1] for point in points ]
    #cluster size with allowance
    cluster_size=((max(X)-min(X))/(GRID_NUM-2*ALLOWANCE),(max(Y)-min(Y))/(GRID_NUM-2*ALLOWANCE))

    #If cluster size is too small then straight line
    if cluster_size[0]<MIN_GRID_SIZE:
        if points[0][1]<point[len(point)-1][1]:
            return ["VTB"]
        else:
            return ["VBT"]
    if cluster_size[1]<MIN_GRID_SIZE:
        if points[0][0]<points[len(point)-1][0]:
            return ["SLR"]
        else:
            return ["SRL"]

    params={'offset':(min(X),min(Y)),'size':cluster_size}
    old_cluster=find_cluster(points[0],params)
    for point in points[1:]:
        new_cluster=find_cluster(point,params)
        if old_cluster!=new_cluster:
            trend=find_trend(old_cluster,new_cluster)
            if trend:
                #if there are no gestures add it
                if len(gesture)==0:
                    gesture.append(trend)
                    #Dont add if it is already there
                elif trend != gesture[len(gesture)-1]:
                    gesture.append(trend)
        old_cluster=new_cluster
    return gesture

def find_cluster(point,params):
    relative_point=(point[0]-params['offset'][0],point[1]-params['offset'][1])
    return (int(relative_point[0]/params['size'][0]),int(relative_point[1]/params['size'][1]))

def find_trend(old_cluster,new_cluster):

    if old_cluster[1]==new_cluster[1] and old_cluster[0]<new_cluster[0]:
        return "SLR"

    if old_cluster[1]==new_cluster[1] and old_cluster[0]>new_cluster[0]:
        return "SRL"

    if old_cluster[0]==new_cluster[0] and old_cluster[1]<new_cluster[1]:
        return "VTB"

    if old_cluster[0]==new_cluster[0] and old_cluster[1]>new_cluster[1]:
        return "VBT"

    return None

def search_gesture(points):
    gestureEXTRACT=gesture_extract(points)
    for gesture in all_gestures.iterkeys():
        if gestureEXTRACT==all_gestures[gesture]:
            return gesture

#Returns an image after analysis
def analyzer(points):
    j=points
    X=[ x[0] for x in j ]
    Y=[ x[1] for x in j ]
    maxX,maxY,minX,minY=max(X),max(Y),min(X),min(Y)
    img=cv.CreateImage((640,480),8,3)
    old=j[0]
    for point in j:
        cv.Line(img,old,point,(255,0,0),2)
        old=point

    for point in j:
        cv.Line(img,point,point,(0,100,255),5)

    cluster_size=((max(X)-min(X))/(GRID_NUM-2*ALLOWANCE),(max(Y)-min(Y))/(GRID_NUM-2*ALLOWANCE))

    gridX=minX-ALLOWANCE*cluster_size[0]
    while gridX<=minX+GRID_NUM*cluster_size[0]:
        cv.Line(img,(int(gridX),int(minY-(ALLOWANCE*cluster_size[1]))),(int(gridX),int(maxY+(ALLOWANCE*cluster_size[1]))),(0,255,0),1)
        gridX+=cluster_size[0]

    gridY=minY-(ALLOWANCE*cluster_size[1])
    while gridY<=minY+GRID_NUM*cluster_size[1]:
        cv.Line(img,(int(minX-ALLOWANCE*cluster_size[0]),int(gridY)),(int(maxX+ALLOWANCE*cluster_size[0]),int(gridY)),(0,255,0),1)
        gridY+=cluster_size[1]

    return img,gesture_extract(points)
