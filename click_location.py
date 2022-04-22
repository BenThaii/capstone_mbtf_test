# from pynput.mouse import Button, Controller
from pynput.mouse import Listener, Button
import atexit

class Single_click:
    def __init__(self):
        self.click_loc = []

    def on_click(self, x, y, button, pressed):
        if(button == Button.left and pressed):      # only process left clicks
            self.click_loc = [x,y]
            return False


Single_col = Single_click()


print('click a location on the screen')
with Listener(on_click=Single_col.on_click) as listener:
    listener.join()

nav_goal_loc = Single_col.click_loc
print("clicked location: ", nav_goal_loc)


