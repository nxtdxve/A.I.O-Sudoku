from generator import Generator
from solver import Solver


def main():
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    solver.start()

if __name__ == "__main__":
    main()