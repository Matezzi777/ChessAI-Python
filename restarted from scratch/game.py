import pygame
import sys
import buttons
import game_objects

class Game:
	def __init__(self, screen):
		#Tech Variables
		self.running: bool = True
		self.screen: pygame.Surface = screen
		self.clock = pygame.time.Clock()
		#Game Variables
		self.buttons: list[buttons.Button] = []
		self.board: game_objects.Board = game_objects.Board()
		self.tile_selected: game_objects.Case | None = None
		self.valid_moves: list[game_objects.Move] | None = None
		self.last_move: game_objects.Move | None = None
		self.turn: int = 1

	def handle_events(self):
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:
			button.change_color(mouse_position)
			button.update(mouse_position)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("GAME : Window cross clicked")
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				...
			if event.type == pygame.KEYDOWN:
				...

	def display(self):
		self.board.display(self.screen)
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handle_events()
			self.display()