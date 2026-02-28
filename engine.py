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
                    row.extend(["+", "━━━━"])
                else:
                    row.extend(["+", "   "])
        row.extend(["+", "\n"])
        for v in array:
            if v & 8 or v == 16:
                if v == 16:
                    row.extend(["┃", " ██ "]) 
                else:
                    row.extend(["┃", "    "])
            else:
                row.extend([" ", "   "])
        row.extend(["┃", "\n"])
        if i == (high - 1): 
            for v in array:
                if v & 4:
                    row.extend(["+", "━━━━"])
            row.extend(["+", "\n"])
        return(row)


    def print_maze(self):
        visual = []
        for i, array in enumerate(self.grid):
            visual.extend(self.r_row(array, self.height, i))
        return visual
            
## class Engine:
##     def __init__(slef, grid, entry, exitt):



def main():
    grid = Grid(HEIGHT, WIDTH)
    grid.make_42()
    lst = grid.print_maze()
    for x in lst:
        print(x, end="")

if __name__ == "__main__":
    main()

