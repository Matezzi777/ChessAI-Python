import pygame
from board import *
from graphics import *
from pieces import PIECES

# Définition de constantes
LEFT_CLICK = 1
RIGHT_CLICK = 3

class Game:
    def __init__(self, screen, letter_font):
        self.screen = screen
        self.letter_font = letter_font
        self.running = True
        self.clock = pygame.time.Clock()
        self.board = init_board()
        self.round: int = 1
        self.piece_selected = None

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                   # Si l'utilisateur clique pour fermer la fenêtre
                self.running = False                                            # Ferme la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:                        # Si l'utilisateur clique dans la fenêtre
                if (50 < event.pos[0] < 850 and 50 < event.pos[1] < 850):       # Si l'utilisateur clique sur l'échiquier
                    if (event.button == LEFT_CLICK):                                # Si c'est un clic gauche
                        if (clicked_on_piece(self.board, event.pos, self.round)):                    # Si le clic est sur une pièce alliée
                            ...
                        else:                                                           # Sinon
                            if (self.piece_selected):                                       # Si une pièce était sélectionnée
                                if (is_legal_move(self.board, self.piece_selected, event.pos)):             # Si le mouvement est légal
                                    ...
                                else:                                                           # Si le mouvement est illégal
                                    ...
                            else:                                                           # Si aucune pièce n'était sélectionnée
                                ...
                    elif (event.button == RIGHT_CLICK):                             # Si c'est un clic droit
                        ...

    def update(self):
        ...

    def display(self):
        put_background(self.screen, self.letter_font)
        put_pieces(self.screen, self.board, PIECES)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

def clicked_on_piece(board, position: tuple[int, int], tour: int) -> bool:
    if (tour % 2 == 0):                                                     # Si c'est au tour des Noirs
        set = ['k', 'q', 'b', 'n', 'r', 'p']
    else:                                                                   # Si c'est au tour des Blancs
        set = ['K', 'Q', 'B', 'N', 'R', 'P']

    x = clickx_to_boardx(position[0])
    y = clicky_to_boardy(position[1])

    if (board[y][x] in set):                                                # Si la pièce appartient à la couleur dont c'est le tour
        print(f"({position[0]},{position[1]} -> [{x+1},{8-y}]) - Click on allied piece [{board[y][x]}].")
        return (True)
    else:                                                                   # Sinon
        print(f"({position[0]},{position[1]} -> [{x+1},{8-y}]) - Click on something else [{board[y][x]}].")
        return (False)

def is_legal_move(piece_selected: tuple[int, int], position: tuple[int, int]) -> bool:
    ...

def clickx_to_boardx(posx: int) -> int:
    if (50 < posx <= 150):
        return (0)
    elif (150 < posx <= 250):
        return (1)
    elif (250 < posx <= 350):
        return (2)
    elif (350 < posx <= 450):
        return (3)
    elif (450 < posx <= 550):
        return (4)
    elif (550 < posx <= 650):
        return (5)
    elif (650 < posx <= 750):
        return (6)
    elif (750 < posx < 850):
        return (7)

def clicky_to_boardy(posy: int) -> int:
    if (50 < posy <= 150):
        return (0)
    elif (150 < posy <= 250):
        return (1)
    elif (250 < posy <= 350):
        return (2)
    elif (350 < posy <= 450):
        return (3)
    elif (450 < posy <= 550):
        return (4)
    elif (550 < posy <= 650):
        return (5)
    elif (650 < posy <= 750):
        return (6)
    elif (750 < posy < 850):
        return (7)