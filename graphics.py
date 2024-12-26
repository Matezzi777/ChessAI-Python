import pygame

#COLORS
BACKGROUND_COLOR = (48, 46, 43)
WHITE_TILE_COLOR = (237, 237, 237)
BLACK_TILE_COLOR = (49, 100, 71)
LETTER_COLOR = (148, 147, 145)

def put_background(screen, letter_font) -> None:
    screen.fill(BACKGROUND_COLOR)
    # row 1
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(50, 750, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(150, 750, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(250, 750, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(350, 750, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(450, 750, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(550, 750, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(650, 750, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(750, 750, 100, 100))
    # row 2
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(50, 650, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(150, 650, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(250, 650, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(350, 650, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(450, 650, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(550, 650, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(650, 650, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(750, 650, 100, 100))
    # row 3
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(50, 550, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(150, 550, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(250, 550, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(350, 550, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(450, 550, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(550, 550, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(650, 550, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(750, 550, 100, 100))
    # row 4
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(50, 450, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(150, 450, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(250, 450, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(350, 450, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(450, 450, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(550, 450, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(650, 450, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(750, 450, 100, 100))
    # row 5
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(50, 350, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(150, 350, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(250, 350, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(350, 350, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(450, 350, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(550, 350, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(650, 350, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(750, 350, 100, 100))
    # row 6
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(50, 250, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(150, 250, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(250, 250, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(350, 250, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(450, 250, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(550, 250, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(650, 250, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(750, 250, 100, 100))
    # row 7
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(50, 150, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(150, 150, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(250, 150, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(350, 150, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(450, 150, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(550, 150, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(650, 150, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(750, 150, 100, 100))
    # row 8
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(50, 50, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(150, 50, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(250, 50, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(350, 50, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(450, 50, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(550, 50, 100, 100))
    pygame.draw.rect(screen, WHITE_TILE_COLOR, pygame.Rect(650, 50, 100, 100))
    pygame.draw.rect(screen, BLACK_TILE_COLOR, pygame.Rect(750, 50, 100, 100))

    screen.blit(letter_font.render('8', True, LETTER_COLOR), (20, 85))
    screen.blit(letter_font.render('7', True, LETTER_COLOR), (20, 185))
    screen.blit(letter_font.render('6', True, LETTER_COLOR), (20, 285))
    screen.blit(letter_font.render('5', True, LETTER_COLOR), (20, 385))
    screen.blit(letter_font.render('4', True, LETTER_COLOR), (20, 485))
    screen.blit(letter_font.render('3', True, LETTER_COLOR), (20, 585))
    screen.blit(letter_font.render('2', True, LETTER_COLOR), (20, 685))
    screen.blit(letter_font.render('1', True, LETTER_COLOR), (20, 785))

    screen.blit(letter_font.render('a', True, LETTER_COLOR), (85, 865))
    screen.blit(letter_font.render('b', True, LETTER_COLOR), (185, 865))
    screen.blit(letter_font.render('c', True, LETTER_COLOR), (285, 865))
    screen.blit(letter_font.render('d', True, LETTER_COLOR), (385, 865))
    screen.blit(letter_font.render('e', True, LETTER_COLOR), (485, 865))
    screen.blit(letter_font.render('f', True, LETTER_COLOR), (585, 865))
    screen.blit(letter_font.render('g', True, LETTER_COLOR), (685, 865))
    screen.blit(letter_font.render('h', True, LETTER_COLOR), (785, 865))

def put_pieces(screen, board, pieces) -> None:
    i: int = 0
    while i < 8:
        j: int = 0
        while j < 8:
            if board[i][j] == ' ':
                piece_to_place = None
            elif board[i][j] == 'k':
                piece_to_place = pieces[6]
            elif board[i][j] == 'K':
                piece_to_place = pieces[0]
            elif board[i][j] == 'q':
                piece_to_place = pieces[7]
            elif board[i][j] == 'Q':
                piece_to_place = pieces[1]
            elif board[i][j] == 'b':
                piece_to_place = pieces[8]
            elif board[i][j] == 'B':
                piece_to_place = pieces[2]
            elif board[i][j] == 'n':
                piece_to_place = pieces[9]
            elif board[i][j] == 'N':
                piece_to_place = pieces[3]
            elif board[i][j] == 'r':
                piece_to_place = pieces[10]
            elif board[i][j] == 'R':
                piece_to_place = pieces[4]
            elif board[i][j] == 'p':
                piece_to_place = pieces[11]
            elif board[i][j] == 'P':
                piece_to_place = pieces[5]
            else:
                print(f"ERROR : Unexpected symbol found in board[{i}][{j}] : '{board[i][j]}'")
                exit(0)
            if piece_to_place:
                place_piece(screen, piece_to_place, i, j)

            j += 1
        i += 1

def place_piece(screen, piece, x: int, y: int) -> None:
    piece.convert()
    screen.blit(piece, (y*100 + 50, x*100 + 50))

def place_valid_move(screen, x: int, y: int) -> None:
    circle = pygame.image.load('pieces/yellow_circle.png')
    circle.convert()
    screen.blit(circle, (x*100 + 50, y*100 + 50))