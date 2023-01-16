class Generator:

    def __init__(self):
        self._grid = [[0 for i in range(9)] for j in range(9)]
        self.solved = ''
        self.unsolved = ''

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, grid):
        self._grid = grid

    def generate_number(self):
        base  = 3
        side  = base*base

        # Pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # Randomize rows, columns and numbers (of valid base pattern)
        from random import sample
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # Produce grid using randomized baseline pattern
        self._grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        # Turn the grid into a string and save it to solved
        for i in range(9):
            for j in range(9):
                self.solved += str(self._grid[i][j])

        # Remove numbers from the solved board and save it to unsolved
        squares = side*side
        empties = squares * 3//4
        for p in sample(range(squares),empties):
            self._grid[p//side][p%side] = 0

        numSize = len(str(side))
        for line in self._grid:
            self.unsolved += ''.join(str(num).rjust(numSize) for num in line)
        return self._grid

    # Print the board to console
    def print_board(self, grid=None):
        if grid is None:
            grid = self._grid
        print("\n\n+ ----------- + ----------- + ----------- +",end="")
        for row in range(9):
            print("\n",end="\n|  ")
            for col in range(9):
                num_end = "  |  " if ((col+1)%3 == 0) else "   "
                print(grid[row][col],end=num_end)
            if ((row+1)%3 == 0):
                print("\n\n+ ----------- + ----------- + ----------- +",end="")
    



                
    


if __name__ == "__main__":
    # Test the generator
    generator = Generator()
    generator.generate_number()
    print(f'Solved: {generator.solved}')
    print(f'Unsolved: {generator.unsolved}')
    print(f'Grid: {generator._grid}')
    generator.print_board(generator._grid)
