# Project #2 Alex Hall Dijkstra Algorithm
import matplotlib.pyplot as plt  # For Path Visualization
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from queue import PriorityQueue
import math
import time

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\achal\Downloads\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'

# Priority Queue to store the nodes and Pop the node with the least cost
open_list = PriorityQueue()
# Cost Grid to store the cost of each node and update the cost if a lesser cost is found
cost_grid = [[float('inf')] * 500 for _ in range(1200)]
# Close list to kepp the track of the visited nodes (Only the coordinate (x,y) is stored in the close list)
close_list = set()
# Tracker to keep the track of the visited nodes (All the information of the node is stored in the visited list)
# This will be used to backtrack the path
tracker = []

# Defining the obstacle Space, Return True if inside obstacle space and false if in free space.
def obst(node):
    if 95 <= node[3][0] <= 180 and 95 <= node[3][1] <= 500:
        return True
    elif 270 <= node[3][0] <= 355 and 0 <= node[3][1] <= 405:
        return True
    elif (node[3][1] + .576 * node[3][0] - 464.4 > 0 and node[3][0] - 511 > 0 and
          node[3][1] - .576 * node[3][0] - 36 < 0 and node[3][0] - 789 < 0 and
          node[3][1] - .576 * node[3][0] + 284.4 > 0 and node[3][1] + .576 * node[3][0] - 784 < 0):  # Hexagon
        return True
    elif 895 <= node[3][0] <= 1105 and 45 <= node[3][1] <= 130:
        return True
    elif 895 <= node[3][0] <= 1105 and 370 <= node[3][1] <= 455:
        return True
    elif 1015 <= node[3][0] <= 1105 and 130 <= node[3][1] <= 370:
        return True
    elif node[3][0] <= 5:
        return True
    elif node[3][0] >= 1195:
        return True
    elif node[3][1] <= 5:
        return True
    elif node[3][1] >= 495:
        return True
    else:
        return False

# ENTER DESIRED START AND END POINTS
start_x = input("Enter Start Node X Coordinate:")
start_y = input("Enter Start Node Y Coordinate:")

if 95 <= int(start_x) <= 180 and 95 <= int(start_y) <= 500:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif 270 <= int(start_x)  <= 355 and 0 <= int(start_y) <= 405:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif (int(start_y) + .576 * int(start_x)  - 464.4 > 0 and int(start_x)  - 511 > 0 and
      int(start_y) - .576 * int(start_x) - 36 < 0 and int(start_x) - 789 < 0 and
      int(start_y) - .576 * int(start_x) + 284.4 > 0 and int(start_y) + .576 * int(start_x) - 784 < 0):
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif 895 <= int(start_x)  <= 1105 and 45 <= int(start_y) <= 130:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif 895 <= int(start_x)  <= 1105 and 370 <= int(start_y) <= 455:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif 1015 <= int(start_x) <= 1105 and 130 <= int(start_y) <= 370:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif int(start_x) <= 5:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif int(start_x) >= 1195:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif int(start_y) <= 5:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif int(start_y) >= 495:
    print("Coordinate in obstacle, try again:")
    start_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
else:
    print("Nice! Start Coordinates Are In Free Space")


goal_x = input("Enter Goal Node X Coordinate:")
goal_y = input("Enter Goal Node Y Coordinate:")

if 95 <= int(goal_x) <= 180 and 95 <= int(start_y) <= 500:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif 270 <= int(goal_x)  <= 355 and 0 <= int(start_y) <= 405:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif (int(goal_y) + .576 * int(goal_x)  - 464.4 > 0 and int(goal_x)  - 511 > 0 and
      int(goal_y) - .576 * int(goal_x) - 36 < 0 and int(goal_x) - 789 < 0 and
      int(goal_y) - .576 * int(goal_x) + 284.4 > 0 and int(goal_y) + .576 * int(goal_x) - 784 < 0):
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif 895 <= int(goal_x) <= 1105 and 45 <= int(goal_y) <= 130:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif 895 <= int(goal_x) <= 1105 and 370 <= int(goal_y) <= 455:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif 1015 <= int(goal_x) <= 1105 and 130 <= int(goal_y) <= 370:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif int(goal_x) <= 5:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif int(goal_x) >= 1195:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    start_y = input("Enter Start Node Y Coordinate Again")
elif int(goal_y) <= 5:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
elif int(goal_y) >= 495:
    print("Coordinate in obstacle, try again:")
    goal_x = input("Enter Start Node X Coordinate Again:")
    goal_y = input("Enter Start Node Y Coordinate Again")
else:
    print("Nice! Goal Coordinates Are In Free Space")

start_node = (int(start_x), int(start_y))
goal_node = (int(goal_x), int(goal_y))

# Defining the actions and updating parent, index and cost
def move_up(node):

    cost = node[0] + 1
    parent = node[3]
    coordinates = (node[3][0], node[3][1] + 1)
    index = coordinates
    child_1 = (cost, index, parent, coordinates)
    return child_1


def move_down(node):
    cost = node[0] + 1
    parent = node[3]
    coordinates = (node[3][0], node[3][1] - 1)
    index = coordinates
    child_2 = (cost, index, parent, coordinates)
    return child_2


def move_right(node):
    cost = node[0] + 1
    parent = node[3]
    coordinates = (node[3][0] + 1, node[3][1])
    index = coordinates
    child_3 = (cost, index, parent, coordinates)
    return child_3


def move_left(node):
    cost = node[0] + 1
    parent = node[3]
    coordinates = (node[3][0] - 1, node[3][1])
    index = coordinates
    child_4 = (cost, index, parent, coordinates)
    return child_4


def move_up_right(node):
    cost = node[0] + math.sqrt(2)
    parent = node[3]
    coordinates = (node[3][0] + 1, node[3][1] + 1)
    index = coordinates
    child_5 = (cost, index, parent, coordinates)
    return child_5


def move_up_left(node):
    cost = node[0] + math.sqrt(2)
    parent = node[3]
    coordinates = (node[3][0] - 1, node[3][1] + 1)
    index = coordinates
    child_6 = (cost, index, parent, coordinates)
    return child_6


def move_down_right(node):
    cost = node[0] + math.sqrt(2)
    parent = node[3]
    coordinates = (node[3][0] + 1, node[3][1] - 1)
    index = coordinates
    child_7 = (cost, index, parent, coordinates)
    return child_7


def move_down_left(node):
    cost = node[0] + math.sqrt(2)
    parent = node[3]
    coordinates = (node[3][0] - 1, node[3][1] - 1)
    index = coordinates
    child_8 = (cost, index, parent, coordinates)
    return child_8


def find_cost_by_coordinate(dictionary, coordinate):
    try:
        return dictionary[coordinate]
    except KeyError:
        print("No cost found")


# Add the start node to the open list
open_list.put((0, 0, 0, start_node))

# Start point for back track
back_track_node_start = None
start_time = time.time()
while not open_list.empty():
    print(".", end="")

    # Pop the node with the least cost
    node = open_list.get()

    # Add the node to the close list
    close_list.add(node[3])

    # Add the node to the tracker for backtracking
    tracker.append(node)

    if node[3] == goal_node:
        # This is the start point for back track
        back_track_node_start = node
        print("!!! GOAL REACHED !!!")
        break
    else:
        child_1 = move_up(node)
        child_2 = move_down(node)
        child_3 = move_right(node)
        child_4 = move_left(node)
        child_5 = move_up_right(node)
        child_6 = move_up_left(node)
        child_7 = move_down_right(node)
        child_8 = move_down_left(node)
        Children = [child_1, child_2, child_3, child_4, child_5, child_6, child_7, child_8]

        for child in Children:

            if child[3] not in close_list and obst(child) is False:
                # if child not in open_list_coordinate:  << Creating an alternative for this condition
                # If a cooridinate (x,y) is previously visited it will have a cost, i.e it won't be infinity
                # We add such a coordinate to the open list
                if cost_grid[child[3][0]][child[3][1]] == float('inf'):
                    open_list.put(child)
                    cost_grid[child[3][0]][child[3][1]] = child[0]
                else:
                    if cost_grid[child[3][0]][child[3][1]] > child[0]:
                        open_list.put(child)
                        cost_grid[child[3][0]][child[3][1]] = child[0]


# BACKTRACKING
back_track = []
node = back_track_node_start  # Start from the goal node as the node
print("Back tracking with node:", node)
while not node[2] == start_node:  # Check if the parent is the start node (start node has parent id 0/None)
    back_track.append(node[3])
    for n in tracker:  # Iterate through the tracker to find the parent of the node
        if n[1] == node[2]:  # visited node id = current node parent id
            node = n  # Set the parent as the child and repeat the process
    print("Added node to back track:", node)

forward_path = back_track[::-1]  # reverse back_track to get forward path
print("PATH TO SUCCESS:", forward_path)
end_time = time.time()
print("Time (s) of algorithm w/ backtracking:", end_time - start_time)
print("Working on Animation...")

# Points for all explored nodes and optimal path
XS = [x[0] for x in forward_path]  
YS = [y[1] for y in forward_path]
coordinate_x = [x[3][0] for x in tracker]
coordinate_y = [y[3][1] for y in tracker]
coordinates = [xy[3] for xy in tracker]

# Visualization Of Path Area
start_time_1 = time.time()
fig, ax = plt.subplots()
ax.set_xlim([0, 1200])
ax.set_ylim([0, 500])
rectangle = plt.Rectangle((100, 100), 75, 400, fc='r')
rectangle_1 = plt.Rectangle((275, 0), 75, 400, fc='r')
hexagon_points = [(516, 175), (516, 325), (650, 405), (784, 325), (784, 175),
                  (650, 95)]
hexagon = plt.Polygon(hexagon_points, fc='r')
rectangle_2 = plt.Rectangle((900, 50), 200, 75, fc='r')
rectangle_3 = plt.Rectangle((900, 375), 200, 75, fc='r')
rectangle_4 = plt.Rectangle((1020, 125), 80, 250, fc='r')

plt.gca().add_patch(rectangle)
plt.gca().add_patch(rectangle_1)
plt.gca().add_patch(rectangle_2)
plt.gca().add_patch(rectangle_3)
plt.gca().add_patch(rectangle_4)
plt.gca().add_patch(hexagon)
plt.gca().set_aspect('equal')
graph, = plt.plot([], [], 'o', color="gold", markersize=2)
graph_1, = plt.plot([], [], 'o', color="g", markersize=2)

# Using 1000 frame multiplier and divider to increase speed
def animate(i):
    graph.set_data(coordinate_x[:i*1000], coordinate_y[:i*1000])
    if i == len(coordinate_y)//1000 - 10:
        graph_1.set_data(XS, YS)
    return graph, graph_1,


ani = FuncAnimation(fig, animate, repeat=False, interval=1, frames=len(coordinate_y)//1000, blit=True)
plt.show()
writer_video = animation.FFMpegWriter(fps=60)
ani.save(filename="HALL_DIJKSTRA_ANIMATION.mp4", writer=writer_video)
end_time_1 = time.time()
print("Time (s) of animation and save:", end_time_1 - start_time_1)

