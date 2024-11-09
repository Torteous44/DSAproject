from game2dboard import Board
import random
from waterLogic import waterPath

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

#function that runs whenever you click something
def mouse_fn(btn, row, col):
    temp = matrix[row][col].pop()
    if temp is not None:
        b[row][col] = temp
    else:
        b[row][col] = 0



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
