from generator import Generator
from solver import Solver


def main():
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    generator.print_board()
    solved_grid = solver.start()
    generator.print_board(solved_grid)


if __name__ == "__main__":
    main()