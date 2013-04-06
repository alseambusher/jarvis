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

        #ANALYZER
        self.analyze_all=True
        analyzer_menu=gtk.MenuItem("Analyzer")
        analyzer_menu.connect("activate",self.start_analyze)
        filemenu.append(analyzer_menu)

        #EXIT
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)

        #HELP
        helpmenu = gtk.Menu()
        helpm= gtk.MenuItem("Help")
        helpm.set_submenu(helpmenu)

        mb.append(helpm)

        #RESET
        contents= gtk.MenuItem("Reset Jarvis")
        helpmenu.append(contents)
        #CONTENTS
        contents= gtk.MenuItem("Contents")
        helpmenu.append(contents)

        #ABOUT
        about=gtk.MenuItem("About")
        helpmenu.append(about)

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
