# from pynput.mouse import Button, Controller
from pynput.mouse import Listener, Button
import atexit


class Goal_collector:
    def __init__(self) -> None:
        self.click_start = []
        self.click_end = []
        self.nav_goal = []

        self.click_location_ls = []
        self.num_clicks = 0

    def on_click(self, x, y, button, pressed):
        if(button == Button.left):      # only process left clicks
            if pressed:
                # store key down location
                self.click_start = [x,y]
            else:
                # store key up location
                self.click_end = [x,y]            
                # store list of click locations
                self.num_clicks += 1
                if self.num_clicks % 2 == 0:
                    # only store even (not odd) clicks
                    print('clicked {} to {}'.format(self.click_start, self.click_end))
                    self.click_location_ls.append([self.click_start, self.click_end])
        else:
            # terminate the listener if the user clicks any button other than the left click
            return False
                    

    def exit_handler(self):
        # # ignore last location because it often refers to an erroneous click
        self.click_location_ls.pop()
        # print list of clicked locations
        print(self.click_location_ls)

Goal_col = Goal_collector()


# print list of clicked locations when program exits
atexit.register(Goal_col.exit_handler)

# listen to the series of clicks and return the even clicks (not odd)
print('ignore odd clicks (nav_goal)')
with Listener(on_click=Goal_col.on_click) as listener:
    listener.join()


