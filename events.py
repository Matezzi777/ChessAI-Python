import pygame

LEFT_CLICK = 1
RIGHT_CLICK = 3

def handle_click(pos: (int,int), button_pressed: int, piece_selected: (int, int), turn: int):
    if 50 < pos[0] < 850 and 50 < pos[1] < 850:
        if button_pressed == LEFT_CLICK:
            print(f"Left Click on ({pos[0]},{pos[1]})")
            if piece_selected:
                if is_legal_move(piece_selected, pos):
                    make_move(piece_selected, pos)
                return None
            else:
                if clicked_on_a_valid_piece(pos, turn):
                    ...
        elif button_pressed == RIGHT_CLICK:
            print(f"Right Click on ({pos[0]},{pos[1]})")
            ...
    else:
        print("Click outside of the board.")

def is_legal_move(piece: (int, int), destination: (int, int)) -> bool:
    ...

def make_move(piece: (int, int), destination: (int, int)):
    ...

def clicked_on_a_valid_piece(pos: (int, int), turn: int):
    ...