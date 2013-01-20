import basic

def window_id(window=None):
    if not window:
        return basic.pipe("xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)'| cut -d '#' -f 2")
    else:
        pass

def minimize(_id=None):
    if not _id:
        _id=window_id()
        print "xwit -id %s -iconify"%_id
        basic._exe("xwit -id %s -iconify"%_id)
