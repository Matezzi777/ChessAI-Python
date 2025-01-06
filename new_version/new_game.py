import pygame
from new_board import Board, Coup
from new_pieces import Piece, King, Queen, Bishop, Knight, Rook, Pawn

# Définition de constantes
LEFT_CLICK = 1
RIGHT_CLICK = 3

class Game:
	def __init__(self, window, font):
		self.window = window
		self.board = Board(window, font)
		self.clock = pygame.time.Clock()
		self.running: bool = True
		self.turn: int = 1
		self.piece_selected: Piece | None = None
		self.valid_moves: list[Coup] | None

	def handling_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:				#Si la touche SPACE est pressée
					self.piece_selected = None
					self.valid_moves = None
			if (event.type == pygame.MOUSEBUTTONDOWN):
				position = event.pos
				button = event.button
				if (50 <= position[0] <= 850 and 50 <= position[1] <= 850):							#Si le clique est sur l'échiquier
					if (button == LEFT_CLICK):															#Si c'est un clic gauche
						board_pos: tuple[int, int] = click_to_board(position)
						if (self.piece_selected == None):													#Si aucune pièce n'est déjà sélectionnée
							if (clicked_on_allied_piece(board_pos, self.board, self.turn)):						#Si clic sur une pièce alliée
								self.piece_selected = self.board[board_pos[0]][board_pos[1]]
								self.piece_selected.display_valid_moves(self.window, self.board, board_pos)
						else:																				#Si une pièce était déjà sélectionnée
							if (board_pos in self.valid_moves):							#Si le click est sur un mouvement valide
								move = Coup()
								self.board.make_move(move)
					elif (button == RIGHT_CLICK):														#Si c'est un clic droit
						self.piece_selected = None
						self.valid_moves = None
				else:																				#Si le clic est en dehors de l'échiquier
					self.piece_selected = None
					self.valid_moves = None

	def display(self):
		self.board.display()
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handling_events()
			self.update()
			self.display()
			self.clock.tick(60)

def click_to_board(click: tuple[int, int]) -> tuple[int, int]:
	board_pos_x: int
	board_pos_y: int
	if (50 <= click[0] < 150):
		board_pos_x = 0
	elif (150 <= click[0] < 250):
		board_pos_x = 1
	elif (250 <= click[0] < 350):
		board_pos_x = 2
	elif (350 <= click[0] < 450):
		board_pos_x = 3
	elif (450 <= click[0] < 550):
		board_pos_x = 4
	elif (550 <= click[0] < 650):
		board_pos_x = 5
	elif (650 <= click[0] < 750):
		board_pos_x = 6
	elif (750 <= click[0] <= 850):
		board_pos_x = 7
	else:
		print(f"ERROR : Unable to translate this click to a board position.\n	Click : {click[0]}{click[1]}.")
		exit(0)
	if (50 <= click[1] < 150):
		board_pos_y = 0
	elif (150 <= click[1] < 250):
		board_pos_y = 1
	elif (250 <= click[1] < 350):
		board_pos_y = 2
	elif (350 <= click[1] < 450):
		board_pos_y = 3
	elif (450 <= click[1] < 550):
		board_pos_y = 4
	elif (550 <= click[1] < 650):
		board_pos_y = 5
	elif (650 <= click[1] < 750):
		board_pos_y = 6
	elif (750 <= click[1] <= 850):
		board_pos_y = 7
	else:
		print(f"ERROR : Unable to translate this click to a board position.\n	Click : {click[0]}{click[1]}.")
		exit(0)
	print(f"Clicked on ({click[0]},{click[1]}) -> ({board_pos_x},{board_pos_y}).")
	return ((board_pos_x, board_pos_y))

def clicked_on_allied_piece(position: tuple[int, int], board: list[list[Piece | None]], turn) -> bool:
	piece = board[position[1]][position[0]]
	if (piece):
		if (turn%2 == 1):
			if (piece.color == 'white'):
				return (True)
		else:
			if (piece.color == 'black'):
				return (True)
	return (False)