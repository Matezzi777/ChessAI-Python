import pygame
from game import Game
from menu import Menu

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption('ChessAI 3.0')
police = pygame.font.Sysfont('Arial', 24)

menu = Menu(screen, police)

menu.run()
pygame.quit()