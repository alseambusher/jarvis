import cv
import lib.track,lib.x
def main():
    old_center=None
    capture=cv.CaptureFromCAM(0)
    cv.NamedWindow("jarvis")
    while(1):
        color_image,data=lib.track.track_data(cv.QueryFrame(capture))
        if(data.center and (data.center!=old_center)):
            lib.x.mousemove((data.center['x']*1380)/640,(data.center['y']*800)/480)
            old_center=data.center
            #try:
                #if((data.center['x'] not in range(old_center['x']-5,old_center['x']+5)) and (data.center['x'] not in range(old_center['x']-5,old_center['x']+5))):
                    #lib.x.mousemove((data.center['x']*1380)/640,(data.center['y']*800)/480)
                    #old_center=data.center
            #except:
                #old_center=data.center
        cv.ShowImage("jarvis",color_image)
        if cv.WaitKey(33)==1048603:
            cv.DestroyWindow("jarvis")
            exit()

if __name__=='__main__':
    main()
