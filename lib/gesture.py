import cv
import math
from basic import dummy_object
GRID_NUM=5

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
    cluster_size=((max(X)-min(X))/GRID_NUM,(max(Y)-min(Y))/GRID_NUM)
    params={'offset':(min(X),min(Y)),'size':cluster_size}
    old_cluster=find_cluster(points[0],params)
    for point in points[1:]:
    	new_cluster=find_cluster(point,params)
	#TODO do something here
	old_cluster=new_cluster
    return gesture
#TODO
def find_cluster(point,params):
	pass
def search_gesture(points):
    gestureEXTRACT=gesture_extract(points)
    for gesture in all_gestures.iterkeys():
        if gestureEXTRACT==all_gestures[gesture]:
            return gesture

