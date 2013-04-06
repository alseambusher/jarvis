import cv
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

    while(1):
        color_image,data=track.track_data(cv.QueryFrame(capture))
        data=track.filter_fingers(data)
        #Optimize mouse center based on previous data before moving mouse
        optimized_centerX,optimized_centerY=track.optimize_mouse_center(old_center,data.center)
        #TODO delete this
        z=[optimized_centerX,optimized_centerY]
        if config.TRACK:
            try:
                print (cv.Round((z[0]*640)/(1366*1.02)),cv.Round((z[1]*480)/(768*1.02)))
            except:
                pass

        if(optimized_centerX and optimized_centerY):
            x.mouse_move(optimized_centerX,optimized_centerY)
            old_center=data.center
        #cv.ShowImage("jarvis",color_image)
        x.keyboard_callback(cv.WaitKey(10))
if __name__=='__main__':
    main()
