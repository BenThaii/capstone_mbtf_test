# Instruction
steps:
1. run `click_location.py` to get positions of "2D Nav Goal" button
2. run `goal_locations.py` to get position & direction of the goal. Note, it is assumed that odd clicks are clicks on "2D Nav Goal", hence ignored. ONly even clicks are stored
3. terminate `goal_locations.py` by making a right mouse click
4. copy "2D Nav Goal" button location from step 1 and goal locations in step 2 into file `mbtf_test.py`
5. change interval between goal selections if desired
6. run `mbtf_test.py`