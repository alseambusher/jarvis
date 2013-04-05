import gtk
from lib import gesture
k=[
(136, 165),
(138, 166),
(141, 166),
(145, 167),
(153, 166),
(165, 166),
(180, 166),
(201, 165),
(221, 162),
(242, 160),
(261, 156),
(284, 154),
(302, 152),
(321, 148),
(341, 145),
(360, 144),
(378, 141),
(394, 141),
(409, 141),
(425, 139),
(439, 139),
(447, 140),
(451, 144),
(451, 151),
(453, 162),
(456, 175),
(460, 188),
(465, 202),
(465, 216),
(467, 231),
(468, 246),
(468, 262),
(472, 280),
(474, 295),
(476, 308),
(476, 321),
(476, 331),
(478, 338),
(478, 342),
(476, 340),
(472, 339),
(465, 335),
(455, 333),
(447, 332),
(438, 331),
(427, 329),
(413, 328),
(393, 326),
(373, 325),
(346, 322),
(322, 322),
(301, 325),
(280, 331),
(260, 336),
(241, 342),
(219, 348),
(200, 352),
(179, 354),
(159, 355),
(152, 354),
(149, 353),
(151, 353),
(148, 353),
(144, 353),
(139, 347),
(135, 340),
(136, 328),
(135, 315),
(135, 304),
(135, 294),
(136, 285),
(134, 274),
(135, 262),
(135, 249),
(132, 242),
(134, 234),
(135, 229),
(139, 225),
(140, 222),
(142, 222),
(144, 221),
(146, 220),
(146, 219),
(149, 216),
(152, 214),
(151, 214),
(151, 213),
(153, 216)
]

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Jarvis Gesture Analyzer")
        self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color("#eee"))

        table = gtk.Table(8, 4, False)
        table.set_col_spacings(3)
        #TODO Take points from JSON
        img,sequence=gesture.analyzer(k)

        self.sequence = gtk.Label("Gesture State Transition: "+"->".join(sequence))

        halign = gtk.Alignment(0, 0, 0, 0)
        halign.add(self.sequence)

        table.attach(halign, 0, 1, 0, 1, gtk.FILL,
            gtk.FILL, 0, 0);

        self.analyzer=gtk.Image()
        self.img_pixbuf=gtk.gdk.pixbuf_new_from_data(img.tostring(),
                                    gtk.gdk.COLORSPACE_RGB,
                                    False,
                                    img.depth,
                                    img.width,
                                    img.height,
                                    img.width*img.nChannels)
        self.analyzer.set_from_pixbuf(self.img_pixbuf)

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

