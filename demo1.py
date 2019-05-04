import pygame, sys, random
from pygame.locals import *

demo = pygame.display.set_mode((800, 800))
#demo.blit(pygame.image.load('images1.png'), [200,200])
table = pygame.image.load('images1.png')
table = pygame.transform.scale(table, (100, 100))

waiter = pygame.image.load('GT.png')
waiter = pygame.transform.scale(waiter, (100, 100))
playerPos = [0, 0] #initialize waiter position

#pygame.draw.rect(demo, (125, 125, 125), (500, 500, 50, 50))
pygame.display.update()

#class node for A star algorithm
class Node():
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

#A star function
def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

#main function
maze =  [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0]]

start = (0,0)
end = (5,4)

path = astar(maze, start, end)
print (path)
print (len(path))

for i in range(len(path)):
    demo.blit(waiter, [0,0])
    if i > len(path) - 2:
        break
    else :
        move_x = path[i+1][0] - path[i][0]
        move_y = path[i+1][1] - path[i][1]


    if move_x == 1 and (playerPos[0] < 8 - 1):
        playerPos[0] +=1
    if move_x == -1 and playerPos[0] > 0:
        playerPos[0] -=1
    if move_y == -1 and playerPos[1] > 0 and playerPos[0] < 8:
        playerPos[1] -=1
    if move_y == 1 and playerPos[1] < 8 - 1 and playerPos[0] < 8:
        playerPos[1] +=1

    pygame.draw.rect(demo, (255,255,255), (0, 0, 800, 800)) #Background color
    pygame.draw.rect(demo, (255,0,0), (0, 0, 100, 100)) #Starting point (0,0)
    pygame.draw.rect(demo, (0, 255, 0), (500, 400, 100, 100)) #destination (5,4)

    #table placement
    demo.blit(table, [100,100]) #(1,1)
    demo.blit(table, [300,100]) #(3,1)
    demo.blit(table, [500,100]) #(5,1)
    demo.blit(table, [0,300])   #(0,3)
    demo.blit(table, [200,300]) #(2,3)
    demo.blit(table, [400,300]) #(4,3)
    demo.blit(table, [600,300]) #(6,3)
    demo.blit(table, [100,500]) #(1,5)
    demo.blit(table, [300,500]) #(3,5)
    demo.blit(table, [500,500]) #(5,5)
    demo.blit(table, [0,700])   #(0,7)
    demo.blit(table, [200,700]) #(2,7)

    pygame.time.delay(1000)
    #move waiter
    demo.blit(waiter, [playerPos[0]*100, playerPos[1]*100])


    pygame.display.update()
