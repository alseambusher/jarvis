import basic
import cv
import colorsys

#returns window id
def window_id(window=None):
    if not window:
        return basic.pipe("xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)'| cut -d '#' -f 2")
    else:
        pass

#minimize window
def minimize(_id=None):
    if not _id:
        basic._exe("xwit -id `xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)'| cut -d '#' -f 2` -iconify")
    else:
        basic._exe("xwit -id %s -iconify"%_id)

def mousemove(x=0,y=0):
    basic._exe("xdotool mousemove %d %d"%(x,y))

#resize window if it is not maximized
def window_resize(width,height,_id=None):
    if not _id:
        basic._exe("xwit -id `xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)'| cut -d '#' -f 2` -resize %s %s"%(width,height))
    else:
        basic._exe("xwit -id %s -resize %s %s"%(_id,width,height))
def test():
    print "alse"

#click to obtain color of any object
def get_clicked_color(event,x,y,flags,param):
    if event==cv.CV_EVENT_LBUTTONDOWN:
        color=cv.Get2D(param,y,x)
        #print color[::-1]
        print colorsys.rgb_to_hsv(color[2],color[1],color[0])# Convert RGB to HSV
