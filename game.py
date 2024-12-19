import pygame
from board import *
from graphics import *
from pieces import PIECES
from events import *

class Game:
    def __init__(self, screen, letter_font):
        self.screen = screen
        self.letter_font = letter_font
        self.running = True
        self.clock = pygame.time.Clock()
        self.board = init_board()
        self.piece_selected = None
        self.turn = 1

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.piece_selected = handle_click(event.pos, event.button, self.piece_selected, self.turn)

    def update(self):
        ...

    def display(self):
        put_background(self.screen, self.letter_font)
        put_pieces(self.screen, self.board, PIECES)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)