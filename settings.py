import gtk
from gui import analyzer
from gui import add as add_gesture_dialog
class Settings(gtk.Window):
    def __init__(self):
        super(Settings, self).__init__()

        self.set_title("Jarvis Settings")
        self.set_size_request(500,500)
        self.set_position(gtk.WIN_POS_CENTER)

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        mb.append(filem)

        #ADD GESTURE
        add=gtk.MenuItem("Add Gesture")
        add.connect("activate",lambda w:add_gesture_dialog.Add())
        filemenu.append(add)

        """
        #EDIT GESTURE
        edit_menu = gtk.Menu()

        edit=gtk.MenuItem("Edit Gesture")
        edit.set_submenu(edit_menu)


        lclick= gtk.MenuItem("Left Click")
        rclick= gtk.MenuItem("Right Click")
        dclick= gtk.MenuItem("Double Click")
        close_window= gtk.MenuItem("Close Window")

        edit_menu.append(lclick)
        edit_menu.append(rclick)
        edit_menu.append(dclick)
        edit_menu.append(close_window)

        filemenu.append(edit)

        #DELETE GESTURE
        delete_menu = gtk.Menu()
        delete=gtk.MenuItem("Delete Gesture")
        delete.set_submenu(delete_menu)


        lclick= gtk.MenuItem("Left Click")
        rclick= gtk.MenuItem("Right Click")
        dclick= gtk.MenuItem("Double Click")
        close_window= gtk.MenuItem("Close Window")

        delete_menu.append(lclick)
        delete_menu.append(rclick)
        delete_menu.append(dclick)
        delete_menu.append(close_window)

        filemenu.append(delete)
        """
        #ANALYZER
        self.analyze_all=True
        analyzer_menu=gtk.MenuItem("Analyzer")
        analyzer_menu.connect("activate",self.start_analyze)
        filemenu.append(analyzer_menu)

        #EXIT
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
    def start_analyze(self,dummy):
        analyzer.Analyzer(self.analyze_all)
        self.analyze_all=False

Settings()
gtk.main()
