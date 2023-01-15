from generator import Generator
from solver import Solver

def main():
    generator = Generator()
    solver = Solver()
    generator.generate_number()
    generator.print_board()
    print('\n\n')
    print(generator.solved)
    print('\n')
    print(generator.unsolved)
    print('\n\n')
    solver.start()


if __name__ == "__main__":
    main()