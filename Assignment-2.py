'''
A* Algorithm Implementation
'''
# from copy import deepcopy
variable_name = "" #@param {type:"string"}
class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

user_input = [[0, 2, 3], [1, 4, 6], [7, 5, 8]]
start = Node(user_input, 0, 0)
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
open = []
closed = []

def copy(curr):
    temp = []
    for i in curr:
        t = []
        for j in i:
            t.append(j)
            temp.append(t)
    return temp

def generate_children(curr):
    global level
    for i in range(3):
        for j in range(3):
            if curr.data[i][j] == 0:
                row = i
                col = j
    children = []
    temp = curr.data
    level = curr.level
    if row - 1 >= 0:
        child1 = copy(temp)
        t = child1[row][col]
        child1[row][col] = child1[row-1][col]
        child1[row-1][col] = t
        child = Node(child1, level+1, 0)
        children.append(child)
    if row + 1 < 3:
        child1 = copy(temp)
        t = child1[row][col]
        child1[row][col] = child1[row+1][col]
        child1[row+1][col] = t
        child = Node(child1, level+1, 0)
        children.append(child)
        level += 1
    if col - 1 >= 0:
        child1 = copy(temp)
        t = child1[row][col]
        child1[row][col] = child1[row][col-1]
        child1[row][col-1] = t
        child = Node(child1, level+1, 0)
        children.append(child)
        level += 1
    if col + 1 < 3:
        child1 = copy(temp)
        t = child1[row][col]
        child1[row][col] = child1[row][col+1]
        child1[row][col+1] = t
        child = Node(child1, level+1, 0)
        children.append(child)
        level += 1
    return children

def f(curr):
    hval = h(curr.data)
    return  hval + curr.level

def h(curr):
    temp = 0
    for i in range(3):
        for j in range(3):
            if curr[i][j] != goal[i][j] and curr[i][j] != 0:
                temp += 1
    return temp

print("Starting matrix: ", start.data)
open.append(start)
while True:
    curr = open[0]
    if h(curr.data) == 0:
        print(h(curr.data))
        print("Goal reached: ", curr.data)
        break
    children = generate_children(curr)
    for i in children:
        i.fval = f(i)
        open.append(i)
    closed.append(curr)
    del open[0]
    open.sort(key=lambda x: f(curr), reverse=False)
