# from pynput.mouse import Button, Controller
from unicodedata import name
from pynput.mouse import Listener, Button
import atexit

class Single_click:
    def __init__(self):
        self.click_loc = []

    def on_click(self, x, y, button, pressed):
        # return the location of the left mouse click
        if(button == Button.left and pressed):      # only process left clicks
            self.click_loc = [x,y]
            return False


Single_col = Single_click()

# listen to a single click on the screen and return the click coordinate
print('click a location on the screen')
with Listener(on_click=Single_col.on_click) as listener:
    listener.join()

nav_goal_loc = Single_col.click_loc
print("clicked location: ", nav_goal_loc)


