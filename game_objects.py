import pygame
from constants import BACKGROUND_COLOR, WHITE_TILE_COLOR, BLACK_TILE_COLOR, GAME_LETTERS_COLOR


#BOARD
class Board:
	def __init__(self):
		self.board: list[list[Case]] = [
			[Case("white", Rook("black"), 1, 8), Case("black", Knight("black"), 2, 8), Case("white", Bishop("black"), 3, 8), Case("black", Queen("black"), 4, 8), Case("white", King("black"), 5, 8), Case("black", Bishop("black"), 6, 8), Case("white", Knight("black"), 7, 8), Case("black", Rook("black"), 8, 8)],
			[Case("black", Pawn("black"), 1, 7), Case("white", Pawn("black"), 2, 7), Case("black", Pawn("black"), 3, 7), Case("white", Pawn("black"), 4, 7), Case("black", Pawn("black"), 5, 7), Case("white", Pawn("black"), 6, 7), Case("black", Pawn("black"), 7, 7), Case("white", Pawn("black"), 8, 7)],
			[Case("white", None, 1, 6), Case("black", None, 2, 6), Case("white", None, 3, 6), Case("black", None, 4, 6), Case("white", None, 5, 6), Case("black", None, 6, 6), Case("white", None, 7, 6), Case("black", None, 8, 6)],
			[Case("black", None, 1, 5), Case("white", None, 2, 5), Case("black", None, 3, 5), Case("white", None, 4, 5), Case("black", None, 5, 5), Case("white", None, 6, 5), Case("black", None, 7, 5), Case("white", None, 8, 5)],
			[Case("white", None, 1, 4), Case("black", None, 2, 4), Case("white", None, 3, 4), Case("black", None, 4, 4), Case("white", None, 5, 4), Case("black", None, 6, 4), Case("white", None, 7, 4), Case("black", None, 8, 4)],
			[Case("black", None, 1, 3), Case("white", None, 2, 3), Case("black", None, 3, 3), Case("white", None, 4, 3), Case("black", None, 5, 3), Case("white", None, 6, 3), Case("black", None, 7, 3), Case("white", None, 8, 3)],
			[Case("white", Pawn("white"), 1, 2), Case("black", Pawn("white"), 2, 2), Case("white", Pawn("white"), 3, 2), Case("black", Pawn("white"), 4, 2), Case("white", Pawn("white"), 5, 2), Case("black", Pawn("white"), 6, 2), Case("white", Pawn("white"), 7, 2), Case("black", Pawn("white"), 8, 2)],
			[Case("black", Rook("white"), 1, 1), Case("white", Knight("white"), 2, 1), Case("black", Bishop("white"), 3, 1), Case("white", Queen("white"), 4, 1), Case("black", King("white"), 5, 1), Case("white", Bishop("white"), 6, 1), Case("black", Knight("white"), 7, 1), Case("white", Rook("white"), 8, 1)]
		]

	def display(self, screen: pygame.Surface) -> None:
		screen.fill(BACKGROUND_COLOR)
		i: int = 0
		while (i < 8):
			row_name = pygame.font.SysFont("Arial", 25).render(f"{i+1}", True, GAME_LETTERS_COLOR)
			col_name = pygame.font.SysFont("Arial", 25).render(f"{['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][i]}", True, GAME_LETTERS_COLOR)
			row_name_rect = row_name.get_rect(center=(25,900-(100*(i+1))))
			col_name_rect = col_name.get_rect(center=(100*(i+1),875))
			screen.blit(row_name, row_name_rect)
			screen.blit(col_name, col_name_rect)
			i += 1
		for row in self.board:
			for case in row:
				case.display(screen)

#PIECES
class Piece:
	def __init__(self):
		self.color: str
		self.type: str
		self.image: str

	def is_allied_with(self, piece) -> bool:
		if (piece):
			return (self.color == piece.color)
		return (False)
	
	def is_enemy_with(self, piece) -> bool:
		if (piece):
			return (self.color != piece.color)
		return (False)

	def get_valid_moves(self, board: Board) -> list:
		...

	def display(self, screen: pygame.Surface, position):
		image = pygame.image.load(self.image)
		image.convert()
		screen.blit(image, (50+((position[0]-1)*100),50+((8-position[1])*100)))

class King(Piece):
	def __init__(self, color):
		self.color = color
		self.image = f"./pieces/{color}_king.png"
		self.type = "King"

	def get_valid_moves(self, board: Board) -> list:
		...

class Queen(Piece):
	def __init__(self, color):
		self.color = color
		self.image = f"./pieces/{color}_queen.png"
		self.type = "Queen"

	def get_valid_moves(self, board: Board) -> list:
		...

class Bishop(Piece):
	def __init__(self, color):
		self.color = color
		self.image = f"./pieces/{color}_bishop.png"
		self.type = "Bishop"

	def get_valid_moves(self, board: Board) -> list:
		...

class Knight(Piece):
	def __init__(self, color):
		self.color = color
		self.image = f"./pieces/{color}_knight.png"
		self.type = "Knight"

	def get_valid_moves(self, board: Board) -> list:
		...

class Rook(Piece):
	def __init__(self, color):
		self.color = color
		self.image = f"./pieces/{color}_rook.png"
		self.type = "Rook"

	def get_valid_moves(self, board: Board) -> list:
		...

class Pawn(Piece):
	def __init__(self, color):
		self.color: str = color
		self.image: str = f"./pieces/{color}_pawn.png"
		self.type: str = "Pawn"

	def get_valid_moves(self, board: Board) -> list:
		...

#OTHERS
class Move:
	def __init__(self, piece: Piece, origin: tuple[int, int], target: tuple[int, int]):
		self.piece = piece
		self.origin = origin
		self.target = target
		self.capture: bool = ...
		self.check: bool = ...
		self.checkmate: bool = ...

	def play(self, board: Board):
		...

	def display(self, screen):
		...

class Case:
	def __init__(self, color: str, piece: Piece | None, col: int, row: int):
		self.color: str = color
		self.piece: Piece | None = piece
		self.position: tuple[int, int] = (col, row)
		self.column: str = f"{['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col-1]}"
		self.row: str = f"{9-row}"
		self.algrebric_notation: str = f"{self.column}{self.row}"

	def is_empty(self) -> bool:
		if (self.piece == None):
			return (True)
		return (False)
	
	def is_occupied_by_white(self) -> bool:
		if (self.piece == None):
			return (False)
		if (self.piece.color == "black"):
			return (False)
		return (True)
	
	def is_occupied_by_black(self) -> bool:
		if (self.piece == None):
			return (False)
		if (self.piece.color == "white"):
			return (False)
		return (True)

	def display(self, screen):
		if (self.color == "white"):
			pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(50+((self.position[0]-1)*100), (50+((8-self.position[1])*100)), 100, 100))
		else:
			pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(50+((self.position[0]-1)*100), (50+((8-self.position[1])*100)), 100, 100))
		if (self.piece is not None):
			self.piece.display(screen, self.position)