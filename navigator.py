from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze)  :  self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        grid2 = [i[:] for i in self.navigator_maze]
        r = len(self.navigator_maze)
        c = len(self.navigator_maze[0])
        if start[0]>=r or start[1] >= c or end[0]>=r or end[1] >= c or grid2[start[0]][start[1]] == 1 or grid2[end[0]][end[1]] == 1 :
            raise PathNotFoundException
        if start == end:
            ans = [start]
            return ans 
        stack = Stack()
        stack.push(end)
        grid2[end[0]][end[1]] = 1
        found = False
        
        while not stack.is_empty() :
            neighbour = []
            x,y = stack.top()
            if x > 0 and grid2[x-1][y] == 0    :   neighbour.append(tuple((x-1, y)))    # Up
            if y < c - 1 and grid2[x][y+1] == 0:   neighbour.append(tuple((x, y+1)))    # Right
            if x < r - 1 and grid2[x+1][y] == 0:   neighbour.append(tuple((x+1, y)))    # Down
            if y > 0 and grid2[x][y-1] == 0.   :   neighbour.append(tuple((x, y-1)))    # Left
            if start in neighbour:
                stack.push(start)
                found = True
                break
            else:
                if neighbour:
                    stack.push(neighbour[0])
                    grid2[neighbour[0][0]][neighbour[0][1]] = 1
                else: stack.pop()
        if found:
            ans = []
            while not stack.is_empty():
                top = stack.pop()
                ans.append(tuple(top))
            return ans
        else: raise PathNotFoundException