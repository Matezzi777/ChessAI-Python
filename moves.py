from pieces import Move

#Mouvements légaux de Pion
def get_pawn_valid_moves(board, piece_selected, x: int, y: int, last_move: Move) -> list[tuple[int, int]] | None:
	if (piece_selected == 'p'):
		allied_piece = ['k', 'q', 'b', 'n', 'r', 'p']
		enemy_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
	elif (piece_selected == 'P'):
		allied_piece = ['K', 'Q', 'B', 'N', 'R', 'P']
		enemy_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
	else:
		print("ERROR : Piece selected was supposed to be a pawn but is not.")

	potential_moves: list[tuple[int, int]] = []
	if (piece_selected == 'p'):
		print(f"Tests :\n - x = {x} | y == 4 (y == {y})\n - last_move.piece == 'P' (last_move.piece == '{last_move.piece}')\n - last_move.start[1] == 6 (last_move.start[1] == {last_move.start[1]})\n - last_move.end[1] == 4 (last_move.end[1] == {last_move.end[1]})")
		print(f" - last_move.start[0] == x-1 or last_move.start[0] == x+1 (last_move.start[0] == {last_move.start[0]})")
		if (last_move != None):
			if ((y == 4) and (last_move.piece == 'P') and (last_move.start[1] == 6) and (last_move.end[1] == 4) and (last_move.start[0] == x-1 or last_move.start[0] == x+1)):
				if (last_move.start[0] == x+1):
					potential_moves.append((y+1,x+1))
				elif (last_move.start[1] == x-1):
					potential_moves.append((y+1,x-1))
		if (not board[y+1][x] in enemy_pieces):
			potential_moves.append((x,y+1))
			if (y == 1 and (not board[y+2][x] in enemy_pieces)):
				potential_moves.append((x,y+2))
		if ((not x == 0) and (board[y+1][x-1] in enemy_pieces)):
			potential_moves.append((x-1,y+1))
		if ((not x == 7) and (board[y+1][x+1] in enemy_pieces)):
			potential_moves.append((x+1,y+1))

	if (piece_selected == 'P'):
		if (last_move != None):
			if ((y == 3) and (last_move.piece == 'p') and (last_move.start[0] == 1) and (last_move.end[0] == 3) and (((x > 0) and (last_move.start[1] == x-1)) or last_move.start[1] == x+1)):
				potential_moves.append((y+1,last_move.start[1]))
		if (not board[y-1][x] in enemy_pieces):
			potential_moves.append((x,y-1))
			if (y == 6 and (not board[y-2][x] in enemy_pieces)):
				potential_moves.append((x,y-2))
		if ((not x == 0) and (board[y-1][x-1] in enemy_pieces)):
			potential_moves.append((x-1,y-1))
		if ((not x == 7) and (board[y-1][x+1] in enemy_pieces)):
			potential_moves.append((x+1,y-1))
	
	valid_moves: list[tuple[int, int]] = []
	for move in potential_moves:
		if ((is_on_board(move)) and (not is_on_allied_piece(board, move, allied_piece)) and (not discover_allied_king(board, (x,y), move))):
			valid_moves.append(move)
	if (valid_moves):
		return (valid_moves)
	return (None)

#Mouvements légaux de Roi
def get_king_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	if (piece_selected == 'k'):
		allied_pieces = ['q', 'b', 'n', 'r', 'p']
	elif (piece_selected == 'K'):
		allied_pieces = ['Q', 'B', 'N', 'R', 'P']
	else:
		print(f"ERROR : Piece selected was supposed to be a king but is not.")

	potential_moves: list[tuple[int, int]] = [
		(x-1, y-1),
		(x, y-1),
		(x+1, y-1),
		(x-1, y),
		(x+1, y),
		(x-1, y+1),
		(x, y+1),
		(x+1, y+1)]

	valid_moves : list[tuple[int, int]] = []

	for move in potential_moves:
		if ((is_on_board(move)) and (not is_on_allied_piece(board, move, allied_pieces)) and (not discover_allied_king(board, (x,y), move))):
			valid_moves.append(move)
	
	if (valid_moves):
		return (valid_moves)
	else:
		return (None)

#Mouvements légaux de Dame
def get_queen_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	if (piece_selected == 'q'):
		allied_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
		enemy_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
	elif (piece_selected == 'Q'):
		allied_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
		enemy_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
	else:
		print("ERROR : Piece selected was supposed to be a queen but is not.")
		return (None)
	
	potential_moves: list[tuple[int, int]] = []

	temp_x = x
	temp_y = y
	while(is_on_board((temp_x+1, temp_y+1)) and (not is_on_allied_piece(board, (temp_x+1, temp_y+1), allied_pieces))):
		temp_x+=1
		temp_y+=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x-1, temp_y-1)) and (not is_on_allied_piece(board, (temp_x-1, temp_y-1), allied_pieces))):
		temp_x-=1
		temp_y-=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x-1, temp_y+1)) and (not is_on_allied_piece(board, (temp_x-1, temp_y+1), allied_pieces))):
		temp_x-=1
		temp_y+=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x+1, temp_y-1)) and (not is_on_allied_piece(board, (temp_x+1, temp_y-1), allied_pieces))):
		temp_x+=1
		temp_y-=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x, temp_y+1)) and (not is_on_allied_piece(board, (temp_x, temp_y+1), allied_pieces))):
		temp_y+=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x, temp_y-1)) and (not is_on_allied_piece(board, (temp_x, temp_y-1), allied_pieces))):
		temp_y-=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x+1, temp_y)) and (not is_on_allied_piece(board, (temp_x+1, temp_y), allied_pieces))):
		temp_x+=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while(is_on_board((temp_x-1, temp_y)) and (not is_on_allied_piece(board, (temp_x-1, temp_y), allied_pieces))):
		temp_x-=1
		potential_moves.append((temp_x,temp_y))
		if(board[temp_y][temp_x] in enemy_pieces):
			break

	valid_moves: list[tuple[int, int]] = []

	for move in potential_moves:
		if (is_on_board(move) and (not is_on_allied_piece(board, move, allied_pieces)) and (not discover_allied_king(board, (x,y), move))):
			valid_moves.append(move)

	if (valid_moves):
		return (valid_moves)
	return (None)

#Mouvements légaux de Fou
def get_bishop_valid_moves(board, piece_selected, x, y) -> list[tuple[int, int]] | None:
	if (piece_selected == 'b'):
		allied_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
		enemy_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
	elif (piece_selected == 'B'):
		allied_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
		enemy_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
	else:
		print("ERROR : Piece selected was supposed to be a bishop but is not.")
		return (None)
	
	potential_moves: list[tuple[int, int]] = []
	
	temp_x = x
	temp_y = y
	while (is_on_board((temp_x+1,temp_y+1)) and (not is_on_allied_piece(board, (temp_x+1,temp_y+1), allied_pieces))):
		temp_x+=1
		temp_y+=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while (is_on_board((temp_x-1,temp_y-1)) and (not is_on_allied_piece(board, (temp_x-1,temp_y-1), allied_pieces))):
		temp_x-=1
		temp_y-=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while (is_on_board((temp_x+1,temp_y-1)) and (not is_on_allied_piece(board, (temp_x+1,temp_y-1), allied_pieces))):
		temp_x+=1
		temp_y-=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	temp_y = y
	while (is_on_board((temp_x-1,temp_y+1)) and (not is_on_allied_piece(board, (temp_x-1,temp_y+1), allied_pieces))):
		temp_x-=1
		temp_y+=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break

	valid_moves: list[tuple[int, int]] = []

	for move in potential_moves:
		if (is_on_board(move) and (not is_on_allied_piece(board, move, allied_pieces)) and (not discover_allied_king(board, (x,y), move))):
			valid_moves.append(move)

	if (valid_moves):
		return (valid_moves)
	return (None)

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
	if (piece_selected == 'r'):
		allied_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
		enemy_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
	elif (piece_selected == 'R'):
		allied_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
		enemy_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
	else:
		print("ERROR : Piece selected was supposed to be a rook but is not.")
		return (None)
	
	potential_moves: list[tuple[int, int]] = []
	
	temp_x = x
	temp_y = y
	while (is_on_board((temp_x+1,temp_y)) and (not is_on_allied_piece(board, (temp_x+1,temp_y), allied_pieces))):
		temp_x+=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	while (is_on_board((temp_x-1,temp_y)) and (not is_on_allied_piece(board, (temp_x-1,temp_y), allied_pieces))):
		temp_x-=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break
	temp_x = x
	while (is_on_board((temp_x,temp_y-1)) and (not is_on_allied_piece(board, (temp_x,temp_y-1), allied_pieces))):
		temp_y-=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break
	temp_y = y
	while (is_on_board((temp_x,temp_y+1)) and (not is_on_allied_piece(board, (temp_x,temp_y+1), allied_pieces))):
		temp_y+=1
		potential_moves.append((temp_x,temp_y))
		if (board[temp_y][temp_x] in enemy_pieces):
			break

	valid_moves: list[tuple[int, int]] = []

	for move in potential_moves:
		if (is_on_board(move) and (not is_on_allied_piece(board, move, allied_pieces)) and (not discover_allied_king(board, (x,y), move))):
			valid_moves.append(move)

	if (valid_moves):
		return (valid_moves)
	return (None)

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