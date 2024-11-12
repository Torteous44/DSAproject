import os
import pygame
from game2dboard import Board
import random
from waterLogic import waterPath

pygame.init()
pygame.mixer.init()


sounds_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.idea')


click_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'click_sound.wav'))
water_flow_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'water.wav'))


def play_click_sound():
    click_sound.play()

# Function to play the water flow sound (level finished)
def play_water_flow_sound():
    water_flow_sound.play()
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        else:
            number = self.top.value
            self.top = self.top.next
            return number


# Function to take a snapshot of the matrix and return a 2D list of heights
def get_matrix_snapshot(matrix, rows, cols):
    snapshot = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # Take the top value from the stack at position (i, j)
            top_value = matrix[i][j].pop()  # Pop to get the current height (or None if empty)
            if top_value is not None:
                snapshot[i][j] = top_value  # Set the height value in the snapshot
            matrix[i][j].push(top_value)  # Push the value back to keep the original stack intact

    return snapshot

#function that runs whenever you click something
def mouse_fn(btn, row, col):
    temp = matrix[row][col].pop()
    if temp is not None:
        b[row][col] = temp
    else:
        b[row][col] = 0

    snapshot = get_matrix_snapshot(matrix, rows, cols)
    path = waterPath(snapshot,row,col)

    for p in path:
        r,c = map(int, p.split(','))
        b[r][c] = "w"




#Board Dimensions
rows = 5
cols = 5
maxHeight = 10

#matrix of the defined size
matrix= [[[] for _ in range(cols)] for _ in range(rows)]

#populate the matrix with numbers from n to 1
for i in range(rows):
    for j in range(cols):
        #Random upper bound selected which will be top of the  stack
        upperBound = random.randint(1, maxHeight)

        stack = Stack()

        #fill up the stack at i j
        for k in range(1, upperBound):
            stack.push(k)

        #save stack to i j
        matrix[i][j] = stack

#board set up
b = Board(rows,cols)

#filling up the board with stacks
for i in range(rows):
    for j in range(cols):
        initVal = matrix[i][j].pop()
        if initVal is None:
            b[i][j] = 0
        else:
            b[i][j] = initVal


b.title = "Click me!"
b.cell_size = 120
b.cell_color = "bisque"

# Set the mouse click callback function
b.on_mouse_click = mouse_fn

# Show the board
b.show()

