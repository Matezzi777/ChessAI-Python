import pygame
from game import Game

pygame.init()
window = pygame.display.set_mode((900, 900))
pygame.display.set_caption('ChessAI')
letter_font = pygame.font.SysFont('Arial', 24)

game = Game(window, letter_font)

game.run()
pygame.quit()