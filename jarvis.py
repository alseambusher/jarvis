import cv
import lib.track,lib.x
def main():
    capture=cv.CaptureFromCAM(0)
    cv.NamedWindow("Real")
    while(1):
        color_image,data=lib.track.track_data(cv.QueryFrame(capture))
        #cv.Add(test,imdraw,test)
        cv.ShowImage("Real",color_image)
        #cv.ShowImage("Threshold",test)
        if cv.WaitKey(33)==1048603:
            cv.DestroyWindow("Real")
            #cv.DestroyWindow("Threshold")
            exit()

if __name__=='__main__':
    main()
