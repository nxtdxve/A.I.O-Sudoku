from generator import Generator
from solver import Solver

class Checker:

    def __init__(self, grid):
        self.grid = grid

        # TODO: Check if the grid is solvable
    def check_solvable(self, grid):
        pass

if __name__ == "__main__":
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    checker = Checker()
    print(checker.check_solvable(grid))

