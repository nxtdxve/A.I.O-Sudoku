from termcolor import colored
from generator import Generator
from solver import Solver
from checker import Checker

def select_sudoku():
    print(colored('\n     Which Sudoku would you like to use?', 'white'))
    print(colored('+' + '-'*42 + '+', 'cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + '1. Generate a new puzzle' + ' '*13, 'green') + colored('|','cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + '2. Import a puzzle' + ' '*19, 'green') + colored('|','cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + '3. Select a puzzle' + ' '*19, 'green') + colored('|','cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + 'Type "exit" to exit the program' + ' '*6, 'red') + colored('|','cyan'))
    print(colored('+' + '-'*42 + '+', 'cyan'))
    choice = input(colored('Enter your choice: ', 'yellow'))
    return choice

def how_to_solve():
    print(colored('\n\n What would you like to do with the puzzle?', 'white'))
    print(colored('+' + '-'*42 + '+', 'cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + '1. Solve the puzzle myself' + ' '*11, 'green') + colored('|','cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + '2. Check if the puzzle is solvable' + ' '*3, 'green') + colored('|','cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + '3. Solve the puzzle automatically' + ' '*4, 'green') + colored('|','cyan'))
    print(colored('|', 'cyan') + colored(' '*5 + 'Type "exit" to exit the program' + ' '*6, 'red') + colored('|','cyan'))
    print(colored('+' + '-'*42 + '+', 'cyan'))
    choice = input(colored('Enter your choice: ', 'yellow'))
    return choice


def main():
    print(colored('Welcome to my A.I.O Sudoku tool', 'cyan'))
    print(colored('This tool can generate a new puzzle, import a puzzle, solve a puzzle, and check if a puzzle is solvable', 'cyan'))
    print(colored('This tool is still in development, so some features may not work!!!', 'light_red'))
    choice = select_sudoku()
    if choice == '1':
        generator = Generator()
        generator.generate_number()
        grid = generator.grid
        solver = Solver(grid)
        checker = Checker()
        generator.print_board()
        choice = how_to_solve()
        if choice == '1':
            solver.solve_puzzle()
        elif choice == '2':
            checker.check_solvable(grid)
        elif choice == '3':
            solved_grid = solver.start()
            generator.print_board(solved_grid)
        else:
            print(colored('Invalid choice, exiting program', 'red'))
"""     generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solver = Solver(grid)
    generator.print_board()
    solved_grid = solver.start()
    generator.print_board(solved_grid) """


if __name__ == "__main__":
    main()