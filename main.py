from tkinter import *
from tkinter.ttk import *

# Window Definition
window = Tk()									# Declare window
window.title('AI Chess')						# Set window's title
window.geometry('900x900')						# Set window's size
window.resizable(width = False, height = False)	# Lock window's size
window.configure(bg="#333333")					# Set window's background color

white_king_icon = PhotoImage(file = "Pieces_echecs_v2/white_king.png")
white_queen_icon = PhotoImage(file = "Pieces_echecs_v2/white_queen.png")
white_bishop_icon = PhotoImage(file = "Pieces_echecs_v2/white_bishop.png")
white_knight_icon = PhotoImage(file = "Pieces_echecs_v2/white_horse.png")
white_rook_icon = PhotoImage(file = "Pieces_echecs_v2/white_rook.png")
white_pawn_icon = PhotoImage(file = "Pieces_echecs_v2/white_pawn.png")

black_king_icon = PhotoImage(file = "Pieces_echecs_v2/black_king.png")
black_queen_icon = PhotoImage(file = "Pieces_echecs_v2/black_queen.png")
black_bishop_icon = PhotoImage(file = "Pieces_echecs_v2/black_bishop.png")
black_knight_icon = PhotoImage(file = "Pieces_echecs_v2/black_horse.png")
black_rook_icon = PhotoImage(file = "Pieces_echecs_v2/black_rook.png")
black_pawn_icon = PhotoImage(file = "Pieces_echecs_v2/black_pawn.png")

test = Button(window, text="?", image=white_king_icon)
test.configure()
Button(window, image=white_queen_icon).pack(side=TOP)
Button(window, image=black_king_icon).pack(side=TOP)

window.mainloop()