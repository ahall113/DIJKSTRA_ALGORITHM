ALEXANDER HALL DIJKSTRA ALGORITHM PROJECT 2

import matplotlib.pyplot as plt >>>> Used for plotting and visualization
from matplotlib import animation >>>> Used for plotting and visualization
from matplotlib.animation import FuncAnimation >>>> Used for plotting and visualization
from queue import PriorityQueue >>>> Priority Queue data structure used for the dijkstra algorith
import math >>>> Used for sqrt fucntion 
import time >>>> Used to keep track of alogrithm time 

I had to add the following in order to save an mp4 file, ffmpeg writer was required for this. The computer running the program may not need this, mine did. It may run with this commented out or the path changed to where-ever the ffmpeg.exe file is on the computer running the program.

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\achal\Downloads\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'

once the code is ran it will prompt the user for a start_node and goal_node. This will be entered by x and y coordinate for each. If the coordinate that is entered is in the obstacle space, it will notify the user. Note that the 5 mm border around the entire arena is in the obstacle space so starting at (6,6) is a good starting point. 

The user will be notified when the goal is reached.

The figured is saved on the current file path as DIJKSTRA_ANIMATION.mp4. "Working on Animation..." is shown while the animation is being constructed and saved. 
