import gtk
import json
import cv
from lib import gesture
class Analyzer(gtk.Window):

    def __init__(self,generate=False):
        super(Analyzer, self).__init__()
        self.analyzer_data=eval(json.load(open("data/analyzer.JSON"))["points"])
        self.analyzer_index=0
        if generate:
            self.analyze_all()

        self.set_title("Jarvis Gesture Analyzer")
        self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)

        table = gtk.Table(8, 4, False)
        table.set_col_spacings(3)

        img,sequence=gesture.analyzer(self.analyzer_data[self.analyzer_index])

        self.sequence = gtk.Label("Gesture State Transition: "+"->".join(sequence))

        halign = gtk.Alignment(0, 0, 0, 0)
        halign.add(self.sequence)

        table.attach(halign, 0, 1, 0, 1, gtk.FILL,
            gtk.FILL, 0, 0);

        self.analyzer=gtk.Image()
        self.analyzer.set_from_file("res/analyzer_0.bmp")

        table.attach(self.analyzer, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND,
            gtk.FILL | gtk.EXPAND, 1, 1)

        next_btn = gtk.Button("Next >>")
        next_btn.connect("clicked",self.next_)
        next_btn.set_size_request(50, 30)
        table.attach(next_btn, 3, 4, 1, 2, gtk.FILL,
            gtk.SHRINK, 1, 1)

        valign = gtk.Alignment(0, 0, 0, 0)
        previous_btn = gtk.Button("<< Prev")
        previous_btn.connect("clicked",self.previous)
        previous_btn.set_size_request(70, 30)
        valign.add(previous_btn)
        table.set_row_spacing(1, 3)
        table.attach(valign, 3, 4, 2, 3, gtk.FILL,
            gtk.FILL | gtk.EXPAND, 1, 1)

        self.add(table)

        #self.connect("destroy", gtk.main_quit)
        self.show_all()

    def next_(self,dummy):
        self.analyzer_index=(self.analyzer_index+1)%len(self.analyzer_data)
        self.update_analyzer()

    def previous(self,dummy):
        self.analyzer_index=(self.analyzer_index-1)%len(self.analyzer_data)
        self.update_analyzer()

    def update_analyzer(self):
        img,sequence=gesture.analyzer(self.analyzer_data[self.analyzer_index])

        self.sequence.set_text("Gesture State Transition: "+"->".join(sequence))
        self.analyzer.set_from_file("res/analyzer_"+str(self.analyzer_index)+".bmp")

    def analyze_all(self):
        for i in range(len(self.analyzer_data)):
            img,sequence=gesture.analyzer(self.analyzer_data[i])
            cv.SaveImage("res/analyzer_"+str(i)+".bmp",img)


if __name__=="__main__":
    Analyzer()
    gtk.main()

