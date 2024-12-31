import pygame
from new_board import Board, Coup
from pieces import Piece, King, Queen, Bishop, Knight, Rook, Pawn

# Définition de constantes
LEFT_CLICK = 1
RIGHT_CLICK = 3

class Game:
	def __init__(self, window, font):
		self.board = Board(window, font)
		self.clock = pygame.time.Clock()
		self.running: bool = True
		self.turn: int = 1
		self.piece_selected: Piece | None = None

	def handling_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				...
			if event.type == pygame.MOUSEBUTTONDOWN:
				...

	def update(self):
		...

	def display(self):
		self.board.display()
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handling_events()
			self.update()
			self.display()
			self.clock.tick(60)