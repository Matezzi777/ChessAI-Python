import pygame

PATH_IMG_FOLDER: str = "../pieces"

class Piece:
	def __init__(self):
		self.color: str
		self.type: str
		self.image: str
		self.position: tuple[int, int]

	def is_allied(self, piece):
		return (self.color == piece.color)
	
	def is_enemy(self, piece):
		return (self.color != piece.color)
	
	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

	def get_position(self) -> tuple[int, int]:
		...

class King(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color: str = color
		self.type: str = 'king'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_king.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Queen(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color: str = color
		self.type: str = 'queen'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_queen.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Bishop(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color: str = color
		self.type: str = 'bishop'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_bishop.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Knight(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color: str = color
		self.type: str = 'knight'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_knight.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Rook(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color: str = color
		self.type: str = 'rook'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_rook.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Pawn(Piece):
	def __init__(self, color: str):
		super().__init__()
		self.color: str = color
		self.type: str = 'pawn'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_pawn.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...