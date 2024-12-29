import pygame

white_king = pygame.image.load('pieces/white_king.png')
white_queen = pygame.image.load('pieces/white_queen.png')
white_bishop = pygame.image.load('pieces/white_bishop.png')
white_knight = pygame.image.load('pieces/white_knight.png')
white_rook = pygame.image.load('pieces/white_rook.png')
white_pawn = pygame.image.load('pieces/white_pawn.png')
black_king = pygame.image.load('pieces/black_king.png')
black_queen = pygame.image.load('pieces/black_queen.png')
black_bishop = pygame.image.load('pieces/black_bishop.png')
black_knight = pygame.image.load('pieces/black_knight.png')
black_rook = pygame.image.load('pieces/black_rook.png')
black_pawn = pygame.image.load('pieces/black_pawn.png')

PIECES: list = [
	white_king,
	white_queen,
	white_bishop,
	white_knight,
	white_rook,
	white_pawn,
	black_king,
	black_queen,
	black_bishop,
	black_knight,
	black_rook,
	black_pawn,
]

class Coup:
	def __init__(self, piece, origin, target):
		self.piece: Piece = piece
		self.origin: tuple[int, int]
		self.target: tuple[int, int]

class Piece:
	def __init__(self):
		self.color: str
		self.position: tuple[int, int]
		self.image: str
		self.valid_moves: list[Coup]

	def is_allied(self, piece) -> bool:
		return (self.color == piece.color)

	def is_enemy(self, piece) -> bool:
		return (self.color != piece.color)
	
	def get_valid_movesss(self, row: int, col: int):
		valid_moves: list[tuple[int, int]] = []
		print(f"Tile selected : {['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]}{8-row}")
		tupl: tuple[int, int] = (row-1, col)
		valid_moves.append(tupl)
		return (valid_moves)

class King(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color = color
		self.image: str = f"pieces/{color}_king.png"
	

class Queen(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color = color
		self.image: str = f"pieces/{color}_queen.png"

class Bishop(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color = color
		self.image: str = f"pieces/{color}_bishop.png"

class Knight(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color = color
		self.image: str = f"pieces/{color}_knight.png"

class Rook(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color = color
		self.image: str = f"pieces/{color}_rook.png"

class Pawn(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color = color
		self.image: str = f"pieces/{color}_pawn.png"
