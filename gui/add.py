import gtk
class Add(gtk.Window):
    def __init__(self):
        super(Add, self).__init__()

        self.set_title("Add Gesture")
        self.set_size_request(350,250)
        self.set_position(gtk.WIN_POS_CENTER)

        mb = gtk.MenuBar()

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.show_all()

if __name__=="__main__":
    Add()
    gtk.main()
