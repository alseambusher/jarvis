from lib import gesture
from gui import add as add_gesture
class Edit(add_gesture.Add):
    def __init__(self,name,comment,command,sequence):
        super(Edit, self).__init__()
        self.gesture_box_text.insert_at_cursor(sequence+"->")
        self.gesture_name.set_text(name)
        self.gesture_name.set_editable(False)
        self.comment.set_text(comment)
        self.command.set_text(command)

    #TODO change this
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
        gesture.add_gesture(sequence,name,comment,command)
        self.alert("Successfully added gesture!","info")
        self.destroy()

