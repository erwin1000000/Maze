import random

WIDTH = 21
HEIGHT = 19
ENTRY = 0,0
EXIT = 19,14
PERFECT = True

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[15 for x in range(width)] for y in range(height)]
    
    def make_42(self):
        h = int(self.height / 2)
        w = int(self.width / 2)
        
        self.grid[h][w - 1] = 16
        self.grid[h][w - 2] = 16
        self.grid[h][w - 3] = 16
        
        self.grid[h - 1][w - 3] = 16
        self.grid[h - 2][w - 3] = 16
        
        self.grid[h + 1][w - 1] = 16
        self.grid[h + 2][w - 1] = 16
       


        self.grid[h][w + 1] = 16
        self.grid[h][w + 2] = 16
        self.grid[h][w + 3] = 16

        self.grid[h + 1][w + 1] = 16
        self.grid[h + 2][w + 1] = 16
        
        self.grid[h + 2][w + 2] = 16
        self.grid[h + 2][w + 3] = 16
        
        self.grid[h - 1][w + 3] = 16
        self.grid[h - 2][w + 3] = 16

        self.grid[h - 2][w + 2] = 16
        self.grid[h - 2][w + 1] = 16
        
    @staticmethod
    def r_row(array, high, i):
        row = []
        for v in array:
                if v & 1 or v == 16:
                    row.extend(["███████"])
                else:
                    row.extend(["██", "     "])
        row.extend(["██", "\n"])
        for x in range(2):
            for v in array:
                if v & 8 or v == 16:
                    if v == 16:
                        row.extend(["███████"]) 
                    else:
                        row.extend(["██", "     "])
                else:
                    row.extend(["       "])
            row.extend(["██", "\n"])
        if i == (high - 1): 
            for v in array:
                if v & 4:
                    row.extend(["███████"])
            row.extend(["██", "\n"])
        return(row)


    def print_maze(self):
        visual = []
        for i, array in enumerate(self.grid):
            visual.extend(self.r_row(array, self.height, i))
        return visual
            
class Engine:
    def __init__(self, grid):
        self.maze = grid

    def dfs(self, y, x):
        moves = [(-1, 0, 1), (0, 1, 2), (0, -1, 8), (1, 0, 4)]
        random.shuffle(moves)
        for move in moves:
            yy = move[0]
            xx = move[1]
            wall = move[2]
            yyy = y + yy
            xxx = x + xx
            if 0 <= xxx < self.maze.width and 0 <= yyy < self.maze.height:
                if self.maze.grid[yyy][xxx] == 15:
                    self.maze.grid[y][x] -= wall
                    if wall == 1:
                        self.maze.grid[yyy][xxx] -= 4
                    elif wall == 2:
                        self.maze.grid[yyy][xxx] -= 8
                    elif wall == 4:
                        self.maze.grid[yyy][xxx] -= 1
                    elif wall == 8:
                        self.maze.grid[yyy][xxx] -= 2
                    self.dfs(yyy, xxx)

def main():
    grid = Grid(HEIGHT, WIDTH)
    grid.make_42()
    engine = Engine(grid)
    engine.dfs(0, 0)
    lst = grid.print_maze()
    for x in lst:
        print(x, end="")

if __name__ == "__main__":
    main()

