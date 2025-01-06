import pygame

white_king = pygame.image.load('pieces/white_king.png')
white_queen = pygame.image.load('pieces/white_queen.png')
white_bishop = pygame.image.load('pieces/white_bishop.png')
white_knight = pygame.image.load('pieces/white_horse.png')
white_rook = pygame.image.load('pieces/white_rook.png')
white_pawn = pygame.image.load('pieces/white_pawn.png')
black_king = pygame.image.load('pieces/black_king.png')
black_queen = pygame.image.load('pieces/black_queen.png')
black_bishop = pygame.image.load('pieces/black_bishop.png')
black_knight = pygame.image.load('pieces/black_horse.png')
black_rook = pygame.image.load('pieces/black_rook.png')
black_pawn = pygame.image.load('pieces/black_pawn.png')

class Move:
	def __init__(self, piece: str, start: tuple[int, int], end: tuple[int, int], piece_captured: str):
		self.piece: str = piece
		self.start: tuple[int, int] = start
		self.end: tuple[int, int] = end
		self.piece_captured: str = piece_captured

	def undo(self, board: list[list[str]]) -> None:
		board[self.start[1]][self.start[0]] = self.piece
		board[self.end[1]][self.end[0]] = self.piece_captured

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