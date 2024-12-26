import pygame
from board import *
from graphics import *
from pieces import PIECES

# Définition de constantes
LEFT_CLICK = 1
RIGHT_CLICK = 3

class Game:
    def __init__(self, screen, letter_font):
        self.screen = screen                                                #La variable de la fenêtre de jeu
        self.letter_font = letter_font                                      #La police de caractère des chiffres et lettres des lignes et colonnes
        self.running: bool = True                                           #La variable permettant d'arrêter la boucle de jeu
        self.clock = pygame.time.Clock()                                    #Un genre de métronome permettant de lisser les performance entre les différents ordinateurs à 60fps
        self.board = init_board()                                           #Un tableau de caractères représentant le plateau
        self.turn: int = 1                                                  #Le compteur de tour pour savoir si c'est au tour des Noirs ou des Blancs
        self.piece_selected: tuple[int, int] | None = None                  #Un tuple représentant la position de la pièce sélectionnée s'il y en a une. Vaut None si aucune pièce n'est sélectionnée
        self.valid_moves: list[tuple[int, int]] | None = None               #La liste des tuples représentant les coups légaux de la pièce sélectionnée s'il y en a une. Vaut None si aucune pièce n'est sélectionnée

    def handling_events(self):
        for event in pygame.event.get():
            #Si l'event est un clic sur la fermeture de la fenêtre
            if event.type == pygame.QUIT:
                self.running = False
            #Si l'event est une touche pressée
            if event.type == pygame.KEYDOWN:
                if (event.unicode == ' '):
                    self.piece_selected = None
                    self.valid_moves = None
            #Si l'event est un clic
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Si l'utilisateur clique sur l'échiquier
                if (50 < event.pos[0] < 850 and 50 < event.pos[1] < 850):
                    #Clic gauche
                    if (event.button == LEFT_CLICK):
                        #Une pièce est sélectionnée
                        if (self.piece_selected):
                            #Si le coup est légal
                            if ((clickx_to_boardx(event.pos[0]), clicky_to_boardy(event.pos[1])) in self.valid_moves):
                                make_move(self.board, self.piece_selected, (clickx_to_boardx(event.pos[0]), clicky_to_boardy(event.pos[1])))
                                self.piece_selected = None
                                self.valid_moves = None
                                self.turn += 1
                            #Si le coup est illégal
                            else:
                                self.piece_selected = None
                                self.valid_moves = None
                        #Aucune pièce n'est sélectionnée
                        else:
                            #Clic sur une pièce de la bonne couleur
                            if (clicked_on_allied_piece(self.board, event.pos, self.turn)):
                                self.piece_selected = (clickx_to_boardx(event.pos[0]),clicky_to_boardy(event.pos[1]))
                                self.valid_moves = get_valid_moves(self.piece_selected)
                    #Clic droit
                    elif (event.button == RIGHT_CLICK):
                        if (self.piece_selected):
                            self.piece_selected = None
                            self.valid_moves = None

    def update(self):
        ...

    def display(self):
        put_background(self.screen, self.letter_font)
        if (self.piece_selected):
            for move in self.valid_moves:
                place_valid_move(self.screen, move[0], move[1])
        put_pieces(self.screen, self.board, PIECES)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

####################################################### FUNCTIONS #######################################################

#Effectue le mouvement sélectionné
def make_move(board, origin: tuple[int, int], target: tuple[int, int]) -> None:
    ...

#Retourne la liste des mouvements légaux pour la pièce sélectionnée
def get_valid_moves(piece_position: tuple[int, int]) -> list[tuple[int, int]] | None:
    valid_moves: list[tuple[int, int]] = []
    ...
    return (valid_moves)

#Retourne la colonne correspondante à la case cliquée (0-7)
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

#Retourne la rangée correspondante à la case cliquée (0-7)
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

#Retourne True si le clic se situe sur une pièce de la couleur du joueur dont c'est le tour sinon renvoie False
def clicked_on_allied_piece(board, position: tuple[int, int], tour: int) -> bool:
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