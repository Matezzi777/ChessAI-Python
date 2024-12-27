import pygame
from pieces import King, Queen, Bishop, Knight, Rook, Pawn

#COLORS
BACKGROUND_COLOR = (48, 46, 43)
WHITE_TILE_COLOR = (237, 237, 237)
BLACK_TILE_COLOR = (49, 100, 71)
LETTER_COLOR = (148, 147, 145)

def put_background(window, font) -> None:
	...

def put_pieces(window, board, pieces) -> None:
	...

def place_piece(window, image, position: tuple[int, int]) -> None:
	...

def put_valid_moves(window, position: tuple[int, int]) -> None:
	...