import gtk
import config
import cv
import threading
import time
from lib import track,x,gesture,basic
from gui import settings
class main(gtk.Window):
    def __init__(self):
        super(main, self).__init__()

        self.set_title("Jarvis")
        self.set_size_request(270,380)
        self.move(10000,10000)
        self.set_frame_dimensions(108,0,8,0)
        self.set_resizable(False)
        self.set_keep_above(config.ALWAYS_ON_TOP)
        if config.ON_ALL_WORKSPACES:
            self.stick()
        self.set_opacity(config.OPACITY)
        self.set_startup_id(config.WINDOW_ID)


        vbox = gtk.VBox(False, 0)

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
        exit.connect("activate", self.kill_jarvis)
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

        #Zeroth Row
        hbox0=gtk.HBox(True,5)
        self.video=gtk.Image()
        self.video.set_size_request(213,160)
        self.video.set_from_file(config.ICON)

        hbox0.add(self.video)

        halign0=gtk.Alignment(0,0,1,0)
        halign0.add(hbox0)
        halign0.set_border_width(1)
        vbox.pack_start(halign0, False, False, 10)

        #First Row
        hbox1=gtk.HBox(True,5)
        self.console_holder=gtk.ScrolledWindow()
        console=gtk.TextView()
        self.console_text=gtk.TextBuffer(table=None)
        console.set_buffer(self.console_text)
        console.set_editable(False)
        console.set_wrap_mode(True)
        console.set_size_request(400,100)
        self.console_holder.add(console)
        hbox1.add(self.console_holder)
        halign1=gtk.Alignment(0,0,1,0)
        halign1.add(hbox1)
        halign1.set_border_width(8)
        vbox.pack_start(halign1, False, False, 0)

        #Second Row
        hbox2=gtk.HBox(True,5)

        self.start_toggle=gtk.Button("Start Jarvis")
        self.STATUS=False

        #slr.connect("clicked",lambda x:self.gesture_box_text.insert_at_cursor("SLR->"))
        self.start_toggle.connect("clicked",self.jarvis_toggle)

        hbox2.add(self.start_toggle)
        halign2=gtk.Alignment(0,0,1,0)
        halign2.add(hbox2)
        halign2.set_border_width(8)
        vbox.pack_start(halign2, False, False, 10)


        self.connect("destroy", self.kill_jarvis)
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

    def jarvis_toggle(self,widget):
        self.STATUS=not self.STATUS
        if self.STATUS:
            self.log("Jarvis Started...")
            self.start_toggle.set_label("Stop Jarvis")
            self.jarvis=threading.Thread(target=self.run)
            self.jarvis.start()
        else:
            self.log("Jarvis Stopped...")
            self.start_toggle.set_label("Restart Jarvis")

    def run(self):
        old_center=None
        cv.NamedWindow("jarvis")
        capture=cv.CaptureFromCAM(0)
        #Click on named window and obtain its color using this callback
        cv.SetMouseCallback("jarvis",x.get_clicked_color,cv.QueryFrame(capture))

        #If manual configuration is enabled
        while config.MANUAL_CONFIGURATION:
            configuration=cv.QueryFrame(capture)
            cv.Flip(configuration,configuration,1)
            cv.ShowImage("jarvis",configuration)
            x.keyboard_callback(cv.WaitKey(10))
        cv.DestroyWindow("jarvis")

        gesture_tolerance=0 # holds number of continuous null returned
        gesture_started=False
        gesture_points=[]
        while self.STATUS:
            color_image,data=track.track_data(cv.QueryFrame(capture),config.TRACKER_COLOR)
            gesture_image,gesture_data=track.track_data(cv.QueryFrame(capture),config.GESTURE_COLOR)

            data=track.filter_contour(data)
            gesture_data=track.filter_contour(gesture_data)

            if data.areas:
                #if  not gesture_started and gesture_data.areas:
                tolerance=0.3
                if  not gesture_started and gesture_data.areas and max(gesture_data.areas)>(1-tolerance)*max(data.areas) and max(gesture_data.areas)<(1+tolerance)*max(data.areas):
                    gesture_tolerance=0
                    gesture_started=True
                    gesture_points=[]
                    self.log("gesture started!!")

                elif not gesture_data.areas and gesture_started:
                    if gesture_tolerance>3:
                        gesture_tolerance=0
                        gesture_started=False
                        try:
                            self.log("->".join(gesture.gesture_extract(gesture_points)))
                            self.log("Executing: "+gesture.search_gesture(gesture_points)[0][2])
                            basic._exe(str(gesture.search_gesture(gesture_points)[0][2]))
                        except:
                            self.log("No match!")
                        gesture_points=[]
                        self.log("gesture stopped!")
                    else:
                        gesture_tolerance+=1
                else:
                    #keep adding to gesture queue
                    gesture_points.append((data.center['x'],data.center['y']))

            #Optimize mouse center based on previous data before moving mouse
            optimized_centerX,optimized_centerY=track.optimize_mouse_center(old_center,data.center)

            if(optimized_centerX and optimized_centerY):
                x.mouse_move(optimized_centerX,optimized_centerY)
                old_center=data.center

            #Add to gtk.Image
            cv.CvtColor(color_image,color_image,cv.CV_BGR2RGB)
            pix_buf=track.ipl2array(color_image)
            pix_buf=gtk.gdk.pixbuf_new_from_array(pix_buf,gtk.gdk.COLORSPACE_RGB,8)
            pix_buf=pix_buf.scale_simple(213,160,gtk.gdk.INTERP_BILINEAR)
            self.video.set_from_pixbuf(pix_buf)
            time.sleep(0.01)

    def log(self,message):
        self.console_text.insert_at_cursor(message+"\n")
        #AUTO SCROLL
        adj=self.console_holder.get_vadjustment()
        adj.set_value(adj.upper - adj.page_size)
        time.sleep(0.01)

    def kill_jarvis(self,widget):
        self.STATUS=False
        time.sleep(0.01)
        gtk.gdk.threads_leave()
        gtk.main_quit()

if __name__=='__main__':
    gtk.gdk.threads_init()
    gtk.gdk.threads_enter()
    main()
    gtk.gdk.threads_leave()
    gtk.main()
