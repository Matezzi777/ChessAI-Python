import pygame
import sys
import buttons
import game_objects
from constants import GAME_LETTERS_COLOR, GAME_BUTTONS_IDLE_COLOR, GAME_BUTTONS_HOVER_COLOR

class Game:
	def __init__(self, screen):
		#Tech Variables
		self.running: bool = True
		self.screen: pygame.Surface = screen
		self.clock = pygame.time.Clock()
		#Game Variables
		self.buttons: list[buttons.Button] = [
			buttons.ButtonGetBetterMove((1100, 180), GAME_BUTTONS_IDLE_COLOR, GAME_BUTTONS_HOVER_COLOR),
			buttons.ButtonAnalyzePosition((1100, 360), GAME_BUTTONS_IDLE_COLOR, GAME_BUTTONS_HOVER_COLOR),
			buttons.ButtonTurnBoard((1100, 540), GAME_BUTTONS_IDLE_COLOR, GAME_BUTTONS_HOVER_COLOR),
			buttons.ButtonResign((1100, 720), GAME_BUTTONS_IDLE_COLOR, GAME_BUTTONS_HOVER_COLOR)
		]
		self.board: game_objects.Board = game_objects.Board()
		self.tile_selected: game_objects.Case | None = None
		self.valid_moves: list[game_objects.Move] | None = None
		self.last_move: game_objects.Move | None = None
		self.turn: int = 1

	def handle_events(self):
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:
			button.change_color(mouse_position)
			button.update(self.screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("GAME : Close Window clicked")
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in self.buttons:
					if (button.check_for_input(mouse_position)):
						button.callback(self.screen)
			if event.type == pygame.KEYDOWN:
				...

	def display(self):
		self.board.display(self.screen)
		for button in self.buttons:
			button.update(self.screen)
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handle_events()
			self.display()