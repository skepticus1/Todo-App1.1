import modules.functions
import PySimpleGUI

# label. or text msg to show user
label = PySimpleGUI.Text("Type in a to do")
# input box for user to enter todo
input_box = PySimpleGUI.InputText(tooltip = "Enter todo")
# button for user to interact with
button = PySimpleGUI.Button("Add")

# creates window instance
# putting label and input_box in same list, so on same line
window = PySimpleGUI.Window("My To Do App", layout=[[label], [input_box, button]])
# displays window instance
window.read()
# closes window instance display
window.close()


