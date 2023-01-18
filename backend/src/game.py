import pygame
import requests

from generator import Generator
from solver import Solver
from checker import Checker

class game:
    def __init__(self, grid):
        self.grid = grid
        self.generator = Generator()
        self.solver = Solver()
        self.checker = Checker()
        