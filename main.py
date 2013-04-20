import gtk
from gui import settings
class main(gtk.Window):
    def __init__(self):
        super(main, self).__init__()

        self.set_title("Jarvis")
        self.set_size_request(400,250)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(8)

        vbox = gtk.VBox(True, 2)

        #MENU>>>>>>>>>>>
        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        mb.append(filem)

        settings_menu_item=gtk.MenuItem("Settings")
        settings_menu_item.connect("activate",lambda x:settings.Settings())
        filemenu.append(settings_menu_item)

        #EXIT
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)

        #HELP
        helpmenu = gtk.Menu()
        helpm= gtk.MenuItem("Help")
        helpm.set_submenu(helpmenu)

        mb.append(helpm)

        #ABOUT
        about=gtk.MenuItem("About")
        about.connect("activate",self.about)
        helpmenu.append(about)

        vbox.pack_start(mb, False, False, 0)

        #MENU ENDS>>>>>>


        #First Row
        hbox1=gtk.HBox(True,5)
        gesture_box=gtk.TextView()
        self.gesture_box_text=gtk.TextBuffer(table=None)
        gesture_box.set_buffer(self.gesture_box_text)
        #self.gesture_box.get_buffer()
        gesture_box.set_wrap_mode(True)
        gesture_box.set_size_request(400,40)
        hbox1.add(gesture_box)
        halign1=gtk.Alignment(0,0,1,0)
        halign1.add(hbox1)
        vbox.pack_start(halign1, False, False, 10)

        #Second Row
        hbox2=gtk.HBox(True,5)

        slr=gtk.Button("Left->Right")
        srl=gtk.Button("Right->Left")
        vtb=gtk.Button("Top->Bottom")
        vbt=gtk.Button("Bottom->Top")

        #slr.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("SLR->"))
        #srl.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("SRL->"))
        #vtb.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("VTB->"))
        #vbt.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("VBT->"))

        hbox2.add(slr)
        hbox2.add(srl)
        hbox2.add(vtb)
        hbox2.add(vbt)
        halign2=gtk.Alignment(0,0,1,0)
        halign2.add(hbox2)
        vbox.pack_start(halign2, False, False, 10)

        #Third Row

        hbox3=gtk.HBox(False,5)
        gesture_name_label=gtk.Label("Gesture:")
        self.gesture_name=gtk.Entry()
        self.gesture_name.set_size_request(300,self.gesture_name.get_size_request()[1])

        hbox3.add(gesture_name_label)
        hbox3.add(self.gesture_name)

        halign3=gtk.Alignment(0,0,0,0)
        halign3.add(hbox3)
        vbox.pack_start(halign3, False, False, 0)

        self.connect("destroy", gtk.main_quit)
        self.add(vbox)
        self.show_all()

    def about(self,widget):
        about = gtk.AboutDialog()
        about.set_program_name("Jarvis")
        about.set_version("1.0")
        about.set_copyright("(c) Jarvis ")
        about.set_comments("Control your computer using hand motion, gestures to improve Human-Computer Interaction.")
        about.set_website("http://www.lifepluslinux.blogspot.in")
        #about.set_logo(gtk.gdk.pixbuf_new_from_file("battery.png"))
        about.run()
        about.destroy()

main()
gtk.main()
