"""
    functions implemented in this library are:
"""
import basic
import cv
import colorsys

#window id
def window_id():
    basic.pipe("xdotool getactivewindow getwindowfocus")
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
#move mouse
def mousemove(x=0,y=0):
    basic._exe("xdotool mousemove %d %d"%(x,y))

#resize window if it is not maximized
def window_resize(width,height):
    basic._exe("xdotool getactivewindow windowsize %d %d"%(width,height))
    #if not _id:
        #basic._exe("xwit -id `xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)'| cut -d '#' -f 2` -resize %s %s"%(width,height))
    #else:
        #basic._exe("xwit -id %s -resize %s %s"%(_id,width,height))
def test():
    print "alse"

#click to obtain color of any object
def get_clicked_color(event,x,y,flags,param):
    if event==cv.CV_EVENT_LBUTTONDOWN:
        color=cv.Get2D(param,y,x)
        #print color[::-1]
        print colorsys.rgb_to_hsv(color[2],color[1],color[0])# Convert RGB to HSV
