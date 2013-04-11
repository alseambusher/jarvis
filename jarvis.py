import cv
import os
from lib import track,x,gesture
import config
def main():
    old_center=None
    capture=cv.CaptureFromCAM(0)
    cv.NamedWindow("jarvis")
    #Click on named window and obtain its color using this callback
    cv.SetMouseCallback("jarvis",x.get_clicked_color,cv.QueryFrame(capture))

    #If manual configuration is enabled
    while config.MANUAL_CONFIGURATION:
        configuration=cv.QueryFrame(capture)
        cv.Flip(configuration,configuration,1)
        cv.ShowImage("jarvis",configuration)
        x.keyboard_callback(cv.WaitKey(10))
    cv.DestroyWindow("jarvis")

    gesture_tolerance=0 # holds number of continuous null returned
    gesture_started=False
    gesture_points=[]
    while(1):
        color_image,data=track.track_data(cv.QueryFrame(capture),config.TRACKER_COLOR)
        gesture_image,gesture_data=track.track_data(cv.QueryFrame(capture),config.GESTURE_COLOR)

        data=track.filter_contour(data)
        gesture_data=track.filter_contour(gesture_data)

        #10% tolerance
        if data.areas:
            if  not gesture_started and gesture_data.areas and max(gesture_data.areas)>0.8*max(data.areas) and max(gesture_data.areas)<1.2*max(data.areas):
                gesture_tolerance=0
                gesture_started=True
                gesture_points=[]
                print "gesture started!!"

            elif not gesture_data.areas and gesture_started:
                if gesture_tolerance>3:
                    gesture_tolerance=0
                    gesture_started=False
                    print gesture_points
                    try:
                        print gesture.gesture_extract(gesture_points)
                        print gesture.search_gesture(gesture_points)
                        os.system(str(gesture.search_gesture(gesture_points)[0][2]))
                    except:
                        print "No match!"
                    gesture_points=[]
                    print "gesture stopped!"
                else:
                    gesture_tolerance+=1
            else:
                #keep adding to gesture queue
                gesture_points.append((data.center['x'],data.center['y']))

        #Optimize mouse center based on previous data before moving mouse
        optimized_centerX,optimized_centerY=track.optimize_mouse_center(old_center,data.center)

        if(optimized_centerX and optimized_centerY):
            x.mouse_move(optimized_centerX,optimized_centerY)
            old_center=data.center
        cv.ShowImage("jarvis",color_image)
        x.keyboard_callback(cv.WaitKey(10))
if __name__=='__main__':
    main()
