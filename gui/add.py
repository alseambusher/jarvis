import gtk
from lib import gesture
class Add(gtk.Window):
    def __init__(self):
        super(Add, self).__init__()

        self.set_title("Add Gesture")
        self.set_size_request(400,250)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(8)
        self.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color("#ccc"))

        vbox = gtk.VBox(True, 2)

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

        slr.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("SLR->"))
        srl.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("SRL->"))
        vtb.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("VTB->"))
        vbt.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("VBT->"))

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

        #Comment
        hbox5=gtk.HBox(False,5)
        comment_label=gtk.Label("Comment:")
        self.comment=gtk.Entry()
        self.comment.set_size_request(300,self.comment.get_size_request()[1])

        hbox5.add(comment_label)
        hbox5.add(self.comment)

        halign5=gtk.Alignment(0,0,0,0)
        halign5.add(hbox5)
        vbox.pack_start(halign5, False, False, 0)

        #Command
        hbox6=gtk.HBox(False,5)
        command_label=gtk.Label("Command:")
        self.command=gtk.Entry()
        self.command.set_size_request(300,self.command.get_size_request()[1])

        hbox6.add(command_label)
        hbox6.add(self.command)

        halign6=gtk.Alignment(0,0,0,0)
        halign6.add(hbox6)
        vbox.pack_start(halign6, False, False, 0)


        #Fourth Row
        hbox4=gtk.HBox(False,5)

        add=gtk.Button(stock=gtk.STOCK_SAVE)
        close=gtk.Button(stock=gtk.STOCK_CLOSE)
        add.connect("clicked",lambda x:self.add_gesture(self.gesture_name.get_text(),self.comment.get_text(),self.command.get_text(),self.get_text(self.gesture_box_text)))
        close.connect("clicked",lambda x:self.destroy())

        hbox4.add(add)
        hbox4.add(close)

        halign4=gtk.Alignment(0,0,1,0)
        halign4.add(hbox4)
        vbox.pack_start(halign4,False,False,10)


        self.add(vbox)
        self.show_all()

    def add_gesture(self,name,comment,command,sequence):
        if not sequence:
            self.alert("Gesture cant exist without states!!")
            return
        if not name:
            self.alert("Gesture Name must NOT be empty")
            return
        if not command:
            self.alert("Command must NOT be empty")
            return
        if sequence[-2:]=="->":
            sequence=sequence[:-2]
        if gesture.search_gesture_by_field('sequence',sequence):
            self.alert("Gesture sequence already exists!!")
            return
        if gesture.search_gesture_by_field('command',command):
            self.alert("Gesture command already exists!!")
            return
        if gesture.search_gesture_by_field('name',name):
            self.alert("Gesture name already exists!!")
            return

        gesture_list=sequence.split("->")
        for gesture_state in gesture_list:
            if gesture_state not in ['SLR','SRL','VTB','VBT']:
                self.alert("Gesture sequence invalid!")
                return

        gesture.add_gesture(sequence,name,comment,command)
        self.alert("Successfully added gesture!","info")
        self.destroy()

    def alert(self,message,message_type="error"):
        md = gtk.MessageDialog(self,gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR if message_type=="error" else gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, message)
        md.run()
        md.destroy()
    #pass a text buffer and get text
    def get_text(self,TextBuffer):
        startiter, enditer = TextBuffer.get_bounds()
        return startiter.get_text(enditer)
