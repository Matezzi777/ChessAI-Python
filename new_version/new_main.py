import pygame
from new_game import Game

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
window = pygame.display.set_mode((900, 900))
pygame.display.set_caption('ChessAI 2.0')
font = pygame.font.SysFont('Arial', 24)

game = Game(window, font)

game.run()
pygame.quit()