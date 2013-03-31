"""
    functions implemented in this library are:
"""
import basic
import cv
import config

#window id
def window_id():
    return basic.pipe("xdotool getactivewindow getwindowfocus")

#minimize window
def window_minimize():
    basic._exe("xdotool getactivewindow windowminimize")

#window move
def window_move(x,y):
    basic._exe("xdotool getactivewindow windowmove %d %d"%(x,y))

#switch desktop workspace
def switch_desktop_workspace(pointer):
    if pointer=="next":
        basic._exe("xdotool set_desktop $((`xdotool get_desktop`+1))")
    else:
        basic._exe("xdotool set_desktop $((`xdotool get_desktop`-1))")

#close the current window
def window_close():
    basic._exe("xdotool getactivewindow windowkill")

#resize window if it is not maximized
def window_resize(width,height):
    basic._exe("xdotool getactivewindow windowsize %d %d"%(width,height))

#move mouse
def mouse_move(x=0,y=0):
    basic._exe("xdotool mousemove %d %d"%(x,y))

def mouse_click(button,repeat=1):
    """
        1=left
        2=mid
        3-right
    """
    basic._exe("xdotool  click --repeat %d %d"%(repeat,button))

def mouse_scroll(action,repeat=1):
    button=4 if action=="up" else 5
    basic._exe("xdotool  click --repeat %d %d"%(repeat,button))

#click to obtain color of any object
def get_clicked_color(event,x,y,flags,frame):
    if event==cv.CV_EVENT_LBUTTONDBLCLK:
        hsv=cv.CreateImage(cv.GetSize(frame),8,3)
        cv.CvtColor(frame,hsv,cv.CV_BGR2HSV)
        (h,s,v,i)=cv.Get2D(hsv,y,x)
        config.TRACKER_COLOR={'MIN':[h,100,10],'MAX':[h+10,255,255]}
        print "Tracker color set to: ",config.TRACKER_COLOR
        #stop configuration rocess if enabled
        config.MANUAL_CONFIGURATION=False

#keyboard_callback
def keyboard_callback(key):
    if key==27:
        config.TRACK=True
        print "started tracking"
        #cv.DestroyWindow("jarvis")
        #print "Cya bye!!"
        #exit()
