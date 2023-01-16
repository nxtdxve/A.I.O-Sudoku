from generator import Generator

class Solver:

    def __init__(self, grid):
        self.M = 9
        self.grid = grid
        self._solved_string = ''
        self._solved_grid = [[0 for i in range(9)] for j in range(9)]

        @property
        def solved_string(self):
            return self._solved_string

        @property
        def solved_grid(self):
            return self._solved_grid

        @solved_string.setter
        def solved_string(self, solved_string):
            self._solved_string = solved_string

        @solved_grid.setter
        def solved_grid(self, solved_grid):
            self._solved_grid = solved_grid

    def puzzle(self,grid):
            solved_string = ""
            self.solved_grid = grid
            for i in range(self.M):
                for j in range(self.M):
                    solved_string += str(grid[i][j])
                    # print(grid[i][j],end = " ")
                # print()
            self.solved_string = solved_string

    def is_valid(self, grid, row, col, num):
        for x in range(self.M):
            if grid[row][x] == num:
                return False
        for x in range(self.M):
            if grid[x][col] == num:
                return False
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def suduko_solver(self, grid, row, col):
        if (row == self.M - 1 and col == self.M):
            return grid
        if col == self.M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return self.suduko_solver(grid, row, col + 1)
        for num in range(1, self.M + 1, 1): 
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.suduko_solver(grid, row, col + 1):
                    return grid
            grid[row][col] = 0
        return False

    def start(self):
        if (self.suduko_solver(self.grid, 0, 0)):
            self.puzzle(self.grid)
        else:
            print("Solution does not exist:(")


if __name__ == "__main__":
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    solver.start()