#Mouvements légaux de Pion
def get_pawn_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	...

#Mouvements légaux de Roi
def get_king_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	...

#Mouvements légaux de Dame
def get_queen_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	...

#Mouvements légaux de Fou
def get_bishop_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	...

#Mouvements légaux de Cavalier
def get_knight_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	if (piece_selected == 'n'):
		allied_pieces = ['p', 'r', 'n', 'b', 'q', 'k']
	elif (piece_selected == 'N'):
		allied_pieces = ['P', 'R', 'N', 'B', 'Q', 'K']
	else:
		print(f"ERROR : Piece selected was supposed to be a knight but is not.")
		return (None)
	
	potential_moves: list[tuple[int, int]] = [
		(x-1,y-2),
		(x-1,y+2),
		(x+1,y-2),
		(x+1,y+2),
		(x-2,y-1),
		(x-2,y+1),
		(x+2,y-1),
		(x+2,y+1)
	]
	valid_moves: list[tuple[int, int]] = []

	for move in potential_moves:
		if (is_on_board(move) and (not is_on_allied_piece(board, move, allied_pieces)) and (not discover_allied_king(board, (x, y), move))):
			valid_moves.append(move)

	if valid_moves:
		return (valid_moves)
	else:
		return (None)


#Mouvements légaux de Tour
def get_rook_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	...

################################################ Conditions ################################################
#Vérifie si les coordonnées sont sur le plateau
def is_on_board(move: tuple[int, int]) -> bool:
	if (not 0 <= move[0] <= 7):
		return(False)
	if (not 0 <= move[1] <= 7):
		return (False)
	return (True)

#Vérifie si les coordonnées ne sont pas déjà occupées par une pièce alliée
def is_on_allied_piece(board, move: tuple[int, int], allied_pieces: list) -> bool:
	if (board[move[1]][move[0]] in allied_pieces):
		return (True)
	return (False)

#Vérifie si le déplacement met le roi allié en échec
def discover_allied_king(board, origin: tuple[int, int], move: tuple[int, int]) -> bool:
	potential_board = copy_board(board)
	piece = board[origin[1]][origin[0]]
	potential_board[origin[1]][origin[0]] = ' '
	potential_board[move[1]][move[0]] = piece
	if (piece in ['p', 'r', 'n', 'b', 'q', 'k']):
		is_white = False
	elif (piece in ['P', 'R', 'N', 'B', 'Q', 'K']):
		is_white = True
	else:
		print(f"ERROR : Piece appeard to be not Black or White (possibly an empty tile) ('{piece}').")
	if (is_allied_check(potential_board, is_white)):
		return (True)
	return (False)

#Vérifie si le roi de la couleur spécifiée est en échec dans cette position
def is_allied_check(board, is_white: bool) -> bool:
	king_position: tuple[int, int] = get_king_pos(board, is_white)
	if (is_white):
		...
	else:
		...
	return (False)

#Retourne la position du roi de la couleur spécifiée sur l'échiquier
def get_king_pos(board, is_white) -> tuple[int, int]:
	if (is_white):
		target = 'K'
	else:
		target = 'k'
	i: int = 0
	while (i < 8):
		j: int = 0
		while (j < 8):
			if (board[i][j] == target):
				return ((j, i))
			j += 1
		i += 1
	print(f"ERROR : Le Roi n'a pas été trouvé sur le plateau.")

#Retourne une copie du plateau de jeu
def copy_board(board) -> list[list]:
	new_board: list[list] = []
	i: int = 0
	while (i < 8):
		row: list = []
		j: int = 0
		while (j < 8):
			row.append(board[i][j])
			j += 1
		new_board.append(row)
		i += 1
	return (new_board)