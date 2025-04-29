import pygame
import sys
import buttons
import game_objects
from constants import GAME_LETTERS_COLOR, GAME_BUTTONS_IDLE_COLOR, GAME_BUTTONS_HOVER_COLOR, LEFT_CLIC, RIGHT_CLIC

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

	def update(self):
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:						#HOVER BUTTONS
			button.change_color(mouse_position)
			button.update(self.screen)

	def handle_events(self):
		mouse_position = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:				#CROIX CLOSE
				print("GAME : Close Window clicked")
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:	#GESTION DES CLICS
				if event.button == LEFT_CLIC:				#CLIC GAUCHE
					for button in self.buttons:
						if (button.check_for_input(mouse_position)):
							button.callback(self.screen)
					if (is_on_board(mouse_position)):
						if (self.tile_selected == None):		#Si aucune case n'était sélectionnée
							clicked_tile: game_objects.Case = get_tile_selected(mouse_position, self.board, self.turn)
							if (clicked_tile.piece is not None):
								self.tile_selected: game_objects.Case = clicked_tile
							if (self.tile_selected is not None):
								print(f"Case sélectionnée : {self.tile_selected.algrebric_notation}")
								piece_selected: game_objects.Piece = self.tile_selected.piece
								print(f"	Pièce sélectionnée : {piece_selected.type} {piece_selected.color}")
								self.valid_moves = piece_selected.get_valid_moves(self.board)
								print(f"		Moves valides :")
								if (self.valid_moves is not None):
									for move in self.valid_moves:
										print(f"		- {move.origin[0]}{move.origin[1]} -> {move.target[0]}{move.target[1]}")
								else:
									print("		- No valid moves.")
							else:
								print(f"Case sélectionnée : None")
						else:									#Si une case était déjà sélectionnée
							clicked_tile: game_objects.Case = get_tile_selected(mouse_position, self.board, self.turn)
							proposed_move = game_objects.Move(self.tile_selected.piece, self.tile_selected.position, get_target_position(mouse_position))
							if (self.valid_moves is not None):
								if (proposed_move in self.valid_moves):
									print("			Move valide !")
									proposed_move.play(self.board)
									self.turn += 1
								else:
									print("			Move invalide !")
							self.valid_moves = None
							self.tile_selected = None
							print("Case sélectionnée : None")
								
				if event.button == RIGHT_CLIC:				#CLIC DROIT
					if (is_on_board(mouse_position)):
						self.tile_selected = None
						self.valid_moves = None
			if event.type == pygame.KEYDOWN:			#APPUIS DE TOUCHES
				if event.key == pygame.K_SPACE:
					self.tile_selected = None
					self.valid_moves = None

	def display(self):
		self.board.display(self.screen)
		for button in self.buttons:
			button.update(self.screen)
		if (self.valid_moves is not None):
			for move in self.valid_moves:
				move.display(self.screen)
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.update()
			self.handle_events()
			self.display()

#Fonctions

#Retourne True si le clic est sur le board, sinon False
def is_on_board(position: tuple[int, int]) -> bool:
	x = position[0]
	y = position[1]
	if ((50 < x < 850) and (50 < y < 850) and (not(x in [150,250,350,450,550,650,750])) and (not(y in [150,250,350,450,550,650,750]))):
		return (True)
	return (False)

#Retourne la Case cliquée si une pièce s'y trouve, sinon None
def get_tile_selected(position: tuple[int, int], board: game_objects.Board, turn: int) -> game_objects.Case | None:
	x : int = position[0]
	y : int = position[1]
	#Look at which player's turn it is
	if (turn % 2 == 0):
		player_color: str = "black"
	else:
		player_color: str = "white"
	#Translate x to board_x
	if (50 < x < 150):
		board_x : int = 0
	elif (150 < x < 250):
		board_x : int = 1
	elif (250 < x < 350):
		board_x : int = 2
	elif (350 < x < 450):
		board_x : int = 3
	elif (450 < x < 550):
		board_x : int = 4
	elif (550 < x < 650):
		board_x : int = 5
	elif (650 < x < 750):
		board_x : int = 6
	elif (750 < x < 850):
		board_x : int = 7
	#Translate y to board_y
	if (50 < y < 150):
		board_y : int = 7
	elif (150 < y < 250):
		board_y : int = 6
	elif (250 < y < 350):
		board_y : int = 5
	elif (350 < y < 450):
		board_y : int = 4
	elif (450 < y < 550):
		board_y : int = 3
	elif (550 < y < 650):
		board_y : int = 2
	elif (650 < y < 750):
		board_y : int = 1
	elif (750 < y < 850):
		board_y : int = 0
	#Get the tile selected
	tile_selected: game_objects.Case = board.board[7-board_y][board_x]
	return (tile_selected)

def get_target_position(clic_position: tuple[int, int]) -> tuple[int, int]:
	x = clic_position[0]
	y = clic_position[1]
	#Translate x to target_x
	if (50 < x < 150):
		target_x : int = 1
	elif (150 < x < 250):
		target_x : int = 2
	elif (250 < x < 350):
		target_x : int = 3
	elif (350 < x < 450):
		target_x : int = 4
	elif (450 < x < 550):
		target_x : int = 5
	elif (550 < x < 650):
		target_x : int = 6
	elif (650 < x < 750):
		target_x : int = 7
	elif (750 < x < 850):
		target_x : int = 8
	#Translate y to target_y
	if (50 < y < 150):
		target_y : int = 8
	elif (150 < y < 250):
		target_y : int = 7
	elif (250 < y < 350):
		target_y : int = 6
	elif (350 < y < 450):
		target_y : int = 5
	elif (450 < y < 550):
		target_y : int = 4
	elif (550 < y < 650):
		target_y : int = 3
	elif (650 < y < 750):
		target_y : int = 2
	elif (750 < y < 850):
		target_y : int = 1
	return ((target_x, target_y))