import gtk
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
        filemenu.append(add)

        #EDIT GESTURE
        edit_menu = gtk.Menu()

        edit=gtk.MenuItem("Edit Gesture")
        edit.set_submenu(edit_menu)


        inews = gtk.MenuItem("Click")
        ibookmarks = gtk.MenuItem("Double Click")
        imail = gtk.MenuItem("Close Window")

        edit_menu.append(inews)
        edit_menu.append(ibookmarks)
        edit_menu.append(imail)

        filemenu.append(edit)

        #DELETE GESTURE
        delete_menu = gtk.Menu()
        delete=gtk.MenuItem("Delete Gesture")
        delete.set_submenu(delete_menu)


        inews = gtk.MenuItem("Click")
        ibookmarks = gtk.MenuItem("Double Click")
        imail = gtk.MenuItem("Close Window")

        delete_menu.append(inews)
        delete_menu.append(ibookmarks)
        delete_menu.append(imail)

        filemenu.append(delete)

        #EXIT
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()


Settings()
gtk.main()
