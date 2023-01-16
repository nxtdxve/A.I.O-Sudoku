from generator import Generator
from solver import Solver

def main():
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    generator.print_board()
    print('\nGenerated solved string:')
    print(generator.solved)
    print('\nGenerated unsolved string:')
    print(generator.unsolved)
    print('\nSolved Grid without notation:')
    solver.start()
    print('\nSolved string:')
    print(solver.solved_string)


if __name__ == "__main__":
    main()