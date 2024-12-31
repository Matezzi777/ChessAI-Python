from pieces import Piece, King, Queen, Bishop, Knight, Rook, Pawn
from new_graphics import put_background, put_piece

class Coup:
	def __init__(self, start, target):
		self.start = start
		self.target = target

class Board:
	def __init__(self, window, font):
		self.board: list[list] = init_board()
		self.window = window
		self.font = font

	def display(self):
		put_background(self.window, self.font)
		row: int = 0
		while (row < 8):
			col: int = 0
			while (col < 8):
				piece: Piece | None = self.board[row][col]
				if piece != None:
					put_piece(self.window, piece, (row, col))
				col += 1
			row += 1

	def evaluate_position(self) -> float:
		...

	def get_best_move(self, turn) -> tuple[int, int]:
		...

def init_board() -> list[list]:
	board = [
		[Rook('black', 1), Knight('black', 1), Bishop('black', 1), Queen('black', 1), King('black'), Bishop('black', 2), Knight('black', 2), Rook('black', 2)],
		[Pawn('black', 1), Pawn('black', 2), Pawn('black', 3), Pawn('black', 4), Pawn('black', 5), Pawn('black', 6), Pawn('black', 7), Pawn('black', 8)],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[Pawn('white', 1), Pawn('white', 2), Pawn('white', 3), Pawn('white', 4), Pawn('white', 5), Pawn('white', 6), Pawn('white', 7), Pawn('white', 8)],
		[Rook('white', 1), Knight('white', 1), Bishop('white', 1), Queen('white', 1), King('white'), Bishop('white', 2), Knight('white', 2), Rook('white', 2)]
	]
	return (board)