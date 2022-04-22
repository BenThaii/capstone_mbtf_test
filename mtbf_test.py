from operator import truediv
import random
from pynput.mouse import Controller, Button
import time

random.seed(0)

nav_goal_loc = [474, 76]
goals = [[[124, 227], [164, 231]], [[470, 229], [515, 230]], [[456, 451], [502, 451]], [[174, 448], [141, 472]], [[84, 646], [131, 667]], [[461, 693], [500, 669]], [[612, 670], [664, 691]], [[524, 895], [492, 916]], [[102, 906], [94, 865]], [[975, 923], [1001, 921]], [[1106, 780], [1106, 750]], [[1255, 671], [1317, 672]], [[1537, 506], [1493, 505]], [[1558, 407], [1562, 383]], [[1486, 215], [1438, 223]], [[1109, 232], [1105, 274]], [[1145, 500], [1196, 508]], [[1126, 672], [1162, 686]], [[1562, 646], [1531, 660]], [[1567, 450], [1511, 451]], [[1570, 282], [1556, 264]], [[1579, 877], [1545, 903]], [[548, 909], [558, 855]], [[1096, 917], [1096, 886]], [[1083, 573], [1083, 603]], [[1149, 698], [1190, 707]], [[1070, 860], [1057, 885]], [[1310, 909], [1350, 909]], [[531, 259], [498, 252]], [[783, 471], [762, 484]], [[1238, 234], [1258, 234]], [[1571, 377], [1563, 399]], [[473, 438], [431, 442]], [[82, 434], [81, 396]], [[79, 614], [75, 642]]]
goal_interval = 6 # seconds

mouse = Controller()

def click_nav_goal():
    '''clicking  "2D Nav Goal" Button. This is done before the goal is selected on the map'''
    mouse.position = nav_goal_loc
    mouse.press(Button.left)
    mouse.release(Button.left)

    
def select_goal_location():
    '''clicking selecting user-defined goal location by clicking at a location, and drag the mouse to align with the desired orientation'''
    goal_idx = random.randint(0, len(goals)-1)
    goal_start = goals[goal_idx][0]
    goal_end = goals[goal_idx][1]
    

    mouse.position = goal_start
    mouse.press(Button.left)

    mouse.position = goal_end
    mouse.release(Button.left)

num_goals_selected = 0
while True:
    # click "2D Nav Goal" button on the screen
    click_nav_goal()
    # select & click random goal
    select_goal_location()
    num_goals_selected += 1
    print('selected goal #', num_goals_selected)
    time.sleep(goal_interval)                   # sleep for a desired amount of time between goal selection intervals

