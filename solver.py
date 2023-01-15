from generator import Generator

class Solver:

    def __init__(self):
        self.M = 9
        self.generator = Generator()
        self.grid = self.generator.generate_number()


    def puzzle(self,grid):
        for i in range(self.M):
            for j in range(self.M):
                print(grid[i][j],end = " ")
            print()

    def is_valid(self,grid, row, col, num):
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

    def suduko_solver(self,grid, row, col):
        if (row == self.M - 1 and col == self.M):
            return True
        if col == self.M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return self.suduko_solver(grid, row, col + 1)
        for num in range(1, self.M + 1, 1): 
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.suduko_solver(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    def start(self):
        if (self.suduko_solver(self.grid, 0, 0)):
            self.puzzle(self.grid)
        else:
            print("Solution does not exist:(")


if __name__ == "__main__":
    solver = Solver()
    solver.start()
