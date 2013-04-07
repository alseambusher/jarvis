from lib import gesture
from gui import add as add_gesture
class Edit(add_gesture.Add):
    def __init__(self,name,comment,command,sequence):
        super(Edit, self).__init__()
        self.set_title("Edit Gesture")
        self.gesture_box_text.insert_at_cursor(sequence+"->")
        self.gesture_name.set_text(name)
        self.gesture_name.set_editable(False)
        self.comment.set_text(comment)
        self.command.set_text(command)

    def add_gesture(self,name,comment,command,sequence):
        if not sequence:
            self.alert("Gesture cant exist without states!!")
            return
        if not command:
            self.alert("Command must NOT be empty")
            return
        if sequence[-2:]=="->":
            sequence=sequence[:-2]

        result=gesture.search_gesture_by_field('sequence',sequence)
        if result and str(result[0][0]) != name:
            self.alert("Gesture sequence already exists!!")
            return

        result=gesture.search_gesture_by_field('command',command)
        if result and str(result[0][0]) !=name:
            self.alert("Gesture command already exists!!")
            return
        gesture.update_gesture(sequence,name,comment,command)
        self.alert("Successfully updated gesture!","info")
        self.destroy()

