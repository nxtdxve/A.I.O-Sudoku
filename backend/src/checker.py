from generator import Generator
from solver import Solver

class Checker:

    def __init__(self, grid):
        self.grid = grid

    def check_solvable(self, grid):
            solver = Solver(grid)
            temp_grid = grid.copy() # create a copy of the current grid
            if solver.suduko_solver(temp_grid, 0, 0): 
                return True
            else:
                return False

if __name__ == "__main__":
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    checker = Checker(grid)
    print(checker.check_solvable(grid))


