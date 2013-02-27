import cv
import lib.track,lib.x
def main():
    capture=cv.CaptureFromCAM(0)
    cv.NamedWindow("jarvis")
    while(1):
        color_image,data=lib.track.track_data(cv.QueryFrame(capture))
        if(data.center):
            #lib.x.mousemove((data.center['x']*1366)/640,(data.center['y']*760)/480)
            lib.x.mousemove(data.center['x'],data.center['y'])
        #cv.Add(test,imdraw,test)
        cv.ShowImage("jarvis",color_image)
        #cv.ShowImage("Threshold",test)
        if cv.WaitKey(33)==1048603:
            cv.DestroyWindow("jarvis")
            #cv.DestroyWindow("Threshold")
            exit()

if __name__=='__main__':
    main()
