from generator import Generator
from solver import Solver

def options():
    print('1. Generate a new puzzle')
    print('2. Solve a puzzle')
    print('3. Exit')
    choice = input('Enter your choice: ')
    return choice


def main():
    choice = options()
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    generator.print_board()
    solved_grid = solver.start()
    generator.print_board(solved_grid)


if __name__ == "__main__":
    main()