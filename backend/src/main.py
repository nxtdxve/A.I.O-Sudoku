import os
from termcolor import colored
from generator import Generator
from solver import Solver
from checker import Checker
from import_sudoku import ImportSudoku

os.system('color')


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
    if choice == '1': # -- Generate a new puzzle
        generator = Generator()
        generator.generate_number()
        grid = generator.grid
        solver = Solver(grid)
        checker = Checker(grid)
        generator.print_board()
        choice = how_to_solve()
        if choice == '1':
            print(colored('Solving the puzzle yourself is not supported yet :(', 'red'))
        elif choice == '2':
            print(checker.check_solvable(grid))
        elif choice == '3':
            solved_grid = solver.start()
            generator.print_board(solved_grid)
        else:
            print(colored('Invalid choice, exiting program', 'red'))

    elif choice == '2': # -- Import a puzzle
        import_sudoku = ImportSudoku()
        grid = import_sudoku.import_sudoku()
        solver = Solver(grid)
        checker = Checker(grid)
        generator = Generator()
        generator.grid = grid
        generator.print_board(grid)
        choice = how_to_solve()
        if choice == '1':
            print(colored('Solving the puzzle yourself is not supported yet :(', 'red'))
        elif choice == '2':
            print(checker.check_solvable(grid))
        elif choice == '3':
            solved_grid = solver.start()
            generator.print_board(solved_grid)
        else:
            print(colored('Invalid choice, exiting program', 'red'))

    elif choice == '3': # -- Select a puzzle
        print(colored('Selecting a puzzle is not supported yet :(', 'red'))

    elif choice == '99': # -- Debug mode
        print(colored('Secret Debug Mode', 'magenta'))
        generator = Generator()
        generator.generate_number()
        grid = generator.grid
        solver = Solver(grid)
        print('Generated Grid:')
        generator.print_board()
        print('\nGenerated solved string:')
        print(generator.solved)
        print('\nGenerated unsolved string:')
        print(generator.unsolved)
        print('\nSolved Grid')
        solved_grid = solver.start()
        generator.print_board(solved_grid)
        print('\nSolved string:')
        print(solver.solved_string)


if __name__ == "__main__":
    main()