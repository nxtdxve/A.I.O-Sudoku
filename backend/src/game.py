import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide Pygame welcome message in console
import pygame

from generator import Generator
from solver import Solver
from checker import Checker

class SudokuGame:
    def __init__(self, grid):
        self.grid = grid
        pygame.init()
        pygame.key.set_repeat(100, 100)

        self.grid_size = 9
        self.grid_cell_size = 60
        self.subgrid_thickness = 1
        self.grid_thickness = 4
        self.screen_size = (self.grid_size * self.grid_cell_size, self.grid_size * self.grid_cell_size)

        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Sudoku")

        self.font = pygame.font.SysFont("comicsans", 40)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // self.grid_cell_size, event.pos[1] // self.grid_cell_size
                if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                    if self.grid[y][x] == 0:
                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    pygame.quit()
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.unicode.isnumeric():
                                        self.grid[y][x] = int(event.unicode)
                                        running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))

        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    x = j * self.grid_cell_size + (self.grid_cell_size - self.font.size(str(self.grid[i][j]))[0]) // 2 + self.grid_thickness - 3
                    y = i * self.grid_cell_size + (self.grid_cell_size - self.font.size(str(self.grid[i][j]))[1]) // 2 + self.grid_thickness - 4
                    text = self.font.render(str(self.grid[i][j]), 1, (0, 0, 0))
                    self.screen.blit(text, (x, y))

        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), thickness)

        pygame.display.flip()


if __name__ == "__main__":
    generator = Generator()
    generator.generate_number()
    grid = generator.grid

    game = SudokuGame(grid)

