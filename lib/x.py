import basic

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

#resize window if it is not maximized
def window_resize(width,height,_id=None):
    if not _id:
        basic._exe("xwit -id `xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)'| cut -d '#' -f 2` -resize %s %s"%(width,height))
    else:
        basic._exe("xwit -id %s -resize %s %s"%(_id,width,height))
