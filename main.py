import pygame
from game import Game

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
window = pygame.display.set_mode((900, 900))
pygame.display.set_caption('ChessAI')
letter_font = pygame.font.SysFont('Arial', 24)

game = Game(window, letter_font)

game.run()
pygame.quit()