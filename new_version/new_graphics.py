import pygame
from pieces import Piece, King, Queen, Bishop, Knight, Rook, Pawn

#COLORS
BACKGROUND_COLOR = (48, 46, 43)
WHITE_TILE_COLOR = (237, 237, 237)
BLACK_TILE_COLOR = (49, 100, 71)
LETTER_COLOR = (148, 147, 145)

def put_background(window, font) -> None:
	window.fill(BACKGROUND_COLOR)
	row: int = 0
	counter: int = 0
	while (row < 8):
		col: int = 0
		while (col < 8):
			if counter % 2 == 0:
				pygame.draw.rect(window, BLACK_TILE_COLOR, pygame.Rect(col*100+50, 750-(row*100), 100, 100))
			else:
				pygame.draw.rect(window, WHITE_TILE_COLOR, pygame.Rect(col*100+50, 750-(row*100), 100, 100))
			counter += 1
			col += 1
		counter -= 1
		row += 1
	counter = 8
	letters: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	while (counter > 0):
		window.blit(font.render(f'{counter}', True, LETTER_COLOR), (20,885-(counter*100)))
		window.blit(font.render(f'{letters[counter-8]}', True, LETTER_COLOR), (885-(counter*100),865))
		counter -= 1

def put_piece(window, piece: Piece, position: tuple[int, int]) -> None:
	piece_image = pygame.image.load(piece.image)
	piece_image.convert()
	window.blit(piece_image, (position[1]*100+50, position[0]*100+50))

def put_valid_moves(window, position: tuple[int, int]) -> None:
	...