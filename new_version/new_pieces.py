import pygame

PATH_IMG_FOLDER: str = "./pieces"

class Piece:
	def __init__(self):
		self.color: str
		self.id: int
		self.type: str
		self.image: str

	def is_allied(self, piece):
		if (piece):
			return (self.color == piece.color)
		return (False)

	def is_enemy(self, piece):
		if (piece):
			return (self.color != piece.color)
		return (False)

	def get_valid_moves(self, board: list[list]) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

	def get_position(self, board: list[list]) -> tuple[int, int]:
		row: int = 0
		while (row < 8):
			col: int = 0
			while (col < 8):
				piece: Piece | None = board[row][col]
				if piece:
					if piece.color == self.color and piece.type == self.type and piece.id == self.id:
						return ((row,col))
				col += 1
			row += 1

class King(Piece):
	def __init__(self, color: str, id: int):
		super().__init__()
		self.color: str = color
		self.id = id
		self.type: str = 'king'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_king.png"

	def get_valid_moves(self, board) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Queen(Piece):
	def __init__(self, color: str, id: int):
		super().__init__()
		self.color: str = color
		self.id = id
		self.type: str = 'queen'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_queen.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Bishop(Piece):
	def __init__(self, color: str, id: int):
		super().__init__()
		self.color: str = color
		self.id = id
		self.type: str = 'bishop'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_bishop.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Knight(Piece):
	def __init__(self, color: str, id: int):
		super().__init__()
		self.color: str = color
		self.id = id
		self.type: str = 'knight'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_knight.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Rook(Piece):
	def __init__(self, color: str, id: int):
		super().__init__()
		self.color: str = color
		self.id = id
		self.type: str = 'rook'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_rook.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...

class Pawn(Piece):
	def __init__(self, color: str, id: int):
		super().__init__()
		self.color: str = color
		self.id = id
		self.type: str = 'pawn'
		self.position: tuple[int, int]
		self.image: str = f"{PATH_IMG_FOLDER}/{color}_pawn.png"

	def get_valid_moves(self) -> list[tuple[int, int]]:
		...

	def display_valid_moves(self) -> None:
		...