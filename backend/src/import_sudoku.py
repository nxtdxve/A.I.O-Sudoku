from generator import Generator

class ImportSudoku:
    def __init__(self):
        self.grid = []

        @property
        def grid(self):
            return self._grid

        @grid.setter
        def grid(self, grid):
            self._grid = grid

    def import_sudoku(self):
        sudoku_input = input("Enter a string of 81 characters or a list of lists (9x9 grid) representing the sudoku puzzle: ")
        if isinstance(sudoku_input, str) and len(sudoku_input) == 81:
            # convert string to list of lists
            for i in range(9):
                row = []
                for j in range(9):
                    row.append(int(sudoku_input[i*9 + j]))
                self.grid.append(row)
        elif isinstance(sudoku_input, list) and len(sudoku_input) == 9:
            # check if all elements of the list are lists of length 9
            if all(isinstance(i, list) and len(i) == 9 for i in sudoku_input):
                self.grid = sudoku_input
            else:
                raise ValueError("Input is not a 9x9 grid")
        else:
            raise ValueError("Input is not a valid sudoku puzzle")
        return self.grid

if __name__ == "__main__":
    # Create an instance of ImportSudoku
    importer = ImportSudoku()

    # Convert input to grid
    importer.import_sudoku()

    # set grid in generator class
    generator = Generator()
    generator.grid = importer.grid

    # print the grid
    generator.print_board(generator.grid)





