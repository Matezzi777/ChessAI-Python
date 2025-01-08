import pygame
from menu import Menu

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen: pygame.Surface = pygame.display.set_mode((900, 900))
pygame.display.set_caption('ChessAI 2.0')

menu = Menu(screen)

menu.run()
pygame.quit()