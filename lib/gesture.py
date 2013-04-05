GRID_NUM=5
ALLOWANCE=0.05 #5%

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
    cluster_size=((max(X)-min(X)+2*ALLOWANCE)/GRID_NUM,(max(Y)-min(Y)+2*ALLOWANCE)/GRID_NUM)
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

