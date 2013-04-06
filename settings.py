import gtk
import os
from gui import analyzer
from gui import add as add_gesture_dialog
from gui import edit as edit_gesture_dialog
from lib import gesture
class Settings(gtk.Window):
    def __init__(self):
        super(Settings, self).__init__()

        self.set_title("Jarvis Settings")
        self.set_size_request(500,500)
        self.set_position(gtk.WIN_POS_CENTER)

        self.update_list()

        self.connect("destroy", gtk.main_quit)

    def start_analyze(self,widget):
        analyzer.Analyzer(self.analyze_all)
        self.analyze_all=False

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

    def prompt(self,message,target):
        dialog = gtk.MessageDialog(self,gtk.DIALOG_DESTROY_WITH_PARENT,gtk.MESSAGE_QUESTION,gtk.BUTTONS_OK_CANCEL,message)
        self.dialog_response=dialog.run()
        dialog.connect("destroy",target)
        dialog.destroy()

    def reset_jarvis(self,widget):
        if self.dialog_response is -5:
            if not os.system("cp data/gestures_master.db data/gestures.db"):
                print "Jarvis reset success"
                self.refresh_list()
            else:
                print "Jarvis reset failed"

    def edit(self,widget):
        gesture_name=" ".join(widget.get_label().split(" ")[1:])
        gest=gesture.search_gesture_by_field('name',gesture_name)[0]
        dialog=edit_gesture_dialog.Edit(str(gest[0]),str(gest[1]),str(gest[2]),str(gest[3]))
        dialog.connect("destroy",lambda x:self.refresh_list())

    def delete_prompt(self,widget):
        gesture_name=" ".join(widget.get_label().split(" ")[1:])
        dialog = gtk.MessageDialog(self,gtk.DIALOG_DESTROY_WITH_PARENT,gtk.MESSAGE_QUESTION,gtk.BUTTONS_OK_CANCEL,"Do you want to delete '%s'?"%gesture_name)
        dialog_response=dialog.run()
        dialog.connect("destroy",lambda x:self.delete(dialog_response,gesture_name))
        dialog.destroy()

    def delete(self,response,gesture_name):
        if response is -5:
            gesture.delete_gesture("name",gesture_name)
            self.refresh_list()

    def add_new(self,widget):
        dialog=add_gesture_dialog.Add()
        dialog.connect("destroy",lambda x:self.refresh_list())

    def update_list(self):

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        mb.append(filem)

        #ADD GESTURE
        add=gtk.MenuItem("Add Gesture")
        add.connect("activate",self.add_new)
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
        reset= gtk.MenuItem("Reset Jarvis")
        reset.connect("activate",lambda x:self.prompt("Click OK to reset Jarvis. Note that this process is Irreversible!",self.reset_jarvis))

        #ABOUT
        about=gtk.MenuItem("About")
        about.connect("activate",self.about)
        #about.connect("activate",lambda x:edit_gesture_dialog.Edit('1','2','3','4'))
        helpmenu.append(reset)
        helpmenu.append(about)

        self.sv=gtk.ScrolledWindow()
        self.vbox = gtk.VBox(False, 2)
        self.vbox.pack_start(mb, False, False, 0)

        boolean=False
        for gest in gesture.get_all_gestures():
            frame=gtk.Frame()
            ev=gtk.EventBox()
            vbox2=gtk.VBox(False,2)
            vbox2.set_size_request(0,100)
            gest_name=gtk.Label("Gesture Name: "+str(gest[0]))
            comment=gtk.Label("Comment: "+str(gest[1]))
            command=gtk.Label("Command: "+str(gest[2]))
            sequence=gtk.Label("Sequence: "+str(gest[3]))
            hbox=gtk.HBox(False,2)
            edit=gtk.Button("Edit "+str(gest[0]))
            delete=gtk.Button("Delete "+str(gest[0]))

            #edit.connect("clicked",lambda x:edit_gesture_dialog.Edit(str(gest[0]),str(gest[1]),str(gest[2]),str(gest[3])))
            edit.connect("clicked",self.edit)
            delete.connect("clicked",self.delete_prompt)

            hbox.add(edit)
            hbox.add(delete)

            vbox2.add(gest_name)
            vbox2.add(comment)
            vbox2.add(command)
            vbox2.add(sequence)
            vbox2.add(hbox)
            ev.add(vbox2)
            frame.add(ev)
            if boolean:
                ev.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color("#ccc"))
            boolean= not boolean
            self.vbox.add(frame)

        self.sv.add_with_viewport(self.vbox)
        self.add(self.sv)
        self.show_all()

    def refresh_list(self):
        self.sv.destroy()
        self.update_list()

Settings()
gtk.main()
