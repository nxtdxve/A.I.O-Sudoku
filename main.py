from operator import ge
from generator import Generator
from solver import Solver


def main():
    generator = Generator()
    solver = Solver()
    generator.generate_number()
    generator.print_board()

    

if __name__ == "__main__":
    main()