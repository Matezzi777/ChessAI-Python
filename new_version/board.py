from pieces import King, Queen, Bishop, Knight, Rook, Pawn

class Move:
	def __init__(self, origin: tuple[int, int], target: tuple[int, int]):
		self.origin = origin
		self.target = target

class Board:
	def __init__(self):
		self.board: list[list] = init_board()

	def display(self):
		...

	def evaluate_position(self) -> float:
		...

	def get_best_move(self, turn) -> Move:
		...

def init_board() -> list[list]:
	board = [
		[Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
		[Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None],
		[Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
		[Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
	]
	return (board)