#!/usr/bin/python
import gtk


class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Jarvis Gesture Analyzer")
        #self.set_size_request(300, 250)
        self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
	self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color("#777"))

        table = gtk.Table(8, 4, False)
        table.set_col_spacings(3)

        self.sequence = gtk.Label("Gesture State Transition: SLR->VTB->SRL->VBT")

        halign = gtk.Alignment(0, 0, 0, 0)
        halign.add(self.sequence)

        table.attach(halign, 0, 1, 0, 1, gtk.FILL,
            gtk.FILL, 0, 0);

        self.analyzer=gtk.Image()
        self.analyzer.set_from_file("res/jarvis.jpg")
        table.attach(self.analyzer, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND,
            gtk.FILL | gtk.EXPAND, 1, 1)

        next_btn = gtk.Button("Next >>")
        next_btn.set_size_request(50, 30)
        table.attach(next_btn, 3, 4, 1, 2, gtk.FILL,
            gtk.SHRINK, 1, 1)

        valign = gtk.Alignment(0, 0, 0, 0)
        previous_btn = gtk.Button("<< Prev")
        previous_btn.set_size_request(70, 30)
        valign.add(previous_btn)
        table.set_row_spacing(1, 3)
        table.attach(valign, 3, 4, 2, 3, gtk.FILL,
            gtk.FILL | gtk.EXPAND, 1, 1)

       

        self.add(table)

        self.connect("destroy", gtk.main_quit)
        self.show_all()


PyApp()
gtk.main()

