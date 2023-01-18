import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from generator import Generator
from solver import Solver


def test_sudoku_solver():
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    # Write test to check if the solver is working
    solver.start()
    assert solver.solved_grid is not None



if __name__ == "__main__":
    test_sudoku_solver()