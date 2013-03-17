import cv
from basic import dummy_object
import config
def getthresholdedimg(im):
    imghsv=cv.CreateImage(cv.GetSize(im),8,3)
    cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)				# Convert image from RGB to HSV
    imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
    cv.InRangeS(imghsv,config.TRACKER_COLOR['MIN'],config.TRACKER_COLOR['MAX'],imgthreshold)	# Select a range of yellow color
    return imgthreshold

def track_data(frame):#this gets all data and the color_image from a given frame
    #posx=0
    #posy=0
    color_image = frame
    #imdraw=cv.CreateImage(cv.GetSize(color_image),8,3)
    cv.Flip(color_image,color_image,1)
    cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)
    imgyellowthresh=getthresholdedimg(color_image)
    cv.Erode(imgyellowthresh,imgyellowthresh,None,3)
    cv.Dilate(imgyellowthresh,imgyellowthresh,None,10)
    storage = cv.CreateMemStorage(0)
    contour = cv.FindContours(imgyellowthresh, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
    points = []
    centers=[]
    areas=[]
    #This is the new part here. ie Use of cv.BoundingRect()
    while contour:
        # Draw bounding rectangles
        bound_rect = cv.BoundingRect(list(contour))
        contour = contour.h_next()
        # for more details about cv.BoundingRect,see documentation
        pt1 = (bound_rect[0], bound_rect[1])
        pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
        points.append(pt1)
        points.append(pt2)
        cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 1)

        #this will have center of each box
        centers.append(
            (cv.Round((pt1[0]+pt2[0])/2),cv.Round((pt1[1]+pt2[1])/2))
        )
        #Compute areas
        areas.append(pow((pt1[0]-pt2[0]),2))

        #lastx=posx
        #lasty=posy
        #posx=cv.Round((pt1[0]+pt2[0])/2)
        #posy=cv.Round((pt1[1]+pt2[1])/2)
        #if lastx!=0 and lasty!=0:
            #cv.Line(imdraw,(posx,posy),(lastx,lasty),(0,255,255))
            #cv.Circle(imdraw,(posx,posy),5,(0,255,255),-1)
    #compute center TODO Find center of left and right hands
    #Computing center
    try:
        center={'x':0,'y':0}
        for c in centers:
            center['x']+=c[0]
            center['y']+=c[1]
        center['x']=center['x']/len(centers)
        center['y']=center['y']/len(centers)
    except:
        center=None
    #Add to data
    data=dummy_object()
    data.center=center
    data.centers=centers
    data.areas=areas
    return color_image,data
