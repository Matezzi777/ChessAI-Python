import tkinter as tk
from tkinter.constants import *

def create_board(window: tk.Tk) -> tk.Canvas:
	canvas = tk.Canvas(window, width=800, height=800, bg="#333333")
	#A
	canvas.create_rectangle((0,700), (100,800), fill="#000000")
	canvas.create_rectangle((100,700), (200,800), fill="#ff0000")
	canvas.create_rectangle((200,700), (300,800), fill="#000000")
	canvas.create_rectangle((300,700), (400,800), fill="#ff0000")
	canvas.create_rectangle((400,700), (500,800), fill="#000000")
	canvas.create_rectangle((500,700), (600,800), fill="#ff0000")
	canvas.create_rectangle((600,700), (700,800), fill="#000000")
	canvas.create_rectangle((700,700), (800,800), fill="#ff0000")
	#B
	canvas.create_rectangle((0,600), (100,700), fill="#ff0000")
	canvas.create_rectangle((100,600), (200,700), fill="#000000")
	canvas.create_rectangle((200,600), (300,700), fill="#ff0000")
	canvas.create_rectangle((300,600), (400,700), fill="#000000")
	canvas.create_rectangle((400,600), (500,700), fill="#ff0000")
	canvas.create_rectangle((500,600), (600,700), fill="#000000")
	canvas.create_rectangle((600,600), (700,700), fill="#ff0000")
	canvas.create_rectangle((700,600), (800,700), fill="#000000")
	#C
	canvas.create_rectangle((0,500), (100,600), fill="#000000")
	canvas.create_rectangle((100,500), (200,600), fill="#ff0000")
	canvas.create_rectangle((200,500), (300,600), fill="#000000")
	canvas.create_rectangle((300,500), (400,600), fill="#ff0000")
	canvas.create_rectangle((400,500), (500,600), fill="#000000")
	canvas.create_rectangle((500,500), (600,600), fill="#ff0000")
	canvas.create_rectangle((600,500), (700,600), fill="#000000")
	canvas.create_rectangle((700,500), (800,600), fill="#ff0000")
	#D
	canvas.create_rectangle((0,400), (100,500), fill="#ff0000")
	canvas.create_rectangle((100,400), (200,500), fill="#000000")
	canvas.create_rectangle((200,400), (300,500), fill="#ff0000")
	canvas.create_rectangle((300,400), (400,500), fill="#000000")
	canvas.create_rectangle((400,400), (500,500), fill="#ff0000")
	canvas.create_rectangle((500,400), (600,500), fill="#000000")
	canvas.create_rectangle((600,400), (700,500), fill="#ff0000")
	canvas.create_rectangle((700,400), (800,500), fill="#000000")
	#E
	canvas.create_rectangle((0,300), (100,400), fill="#000000")
	canvas.create_rectangle((100,300), (200,400), fill="#ff0000")
	canvas.create_rectangle((200,300), (300,400), fill="#000000")
	canvas.create_rectangle((300,300), (400,400), fill="#ff0000")
	canvas.create_rectangle((400,300), (500,400), fill="#000000")
	canvas.create_rectangle((500,300), (600,400), fill="#ff0000")
	canvas.create_rectangle((600,300), (700,400), fill="#000000")
	canvas.create_rectangle((700,300), (800,400), fill="#ff0000")
	#F
	canvas.create_rectangle((0,200), (100,300), fill="#ff0000")
	canvas.create_rectangle((100,200), (200,300), fill="#000000")
	canvas.create_rectangle((200,200), (300,300), fill="#ff0000")
	canvas.create_rectangle((300,200), (400,300), fill="#000000")
	canvas.create_rectangle((400,200), (500,300), fill="#ff0000")
	canvas.create_rectangle((500,200), (600,300), fill="#000000")
	canvas.create_rectangle((600,200), (700,300), fill="#ff0000")
	canvas.create_rectangle((700,200), (800,300), fill="#000000")
	#G
	canvas.create_rectangle((0,100), (100,200), fill="#000000")
	canvas.create_rectangle((100,100), (200,200), fill="#ff0000")
	canvas.create_rectangle((200,100), (300,200), fill="#000000")
	canvas.create_rectangle((300,100), (400,200), fill="#ff0000")
	canvas.create_rectangle((400,100), (500,200), fill="#000000")
	canvas.create_rectangle((500,100), (600,200), fill="#ff0000")
	canvas.create_rectangle((600,100), (700,200), fill="#000000")
	canvas.create_rectangle((700,100), (800,200), fill="#ff0000")
	#H
	canvas.create_rectangle((0,0), (100,100), fill="#ff0000")
	canvas.create_rectangle((100,0), (200,100), fill="#000000")
	canvas.create_rectangle((200,0), (300,100), fill="#ff0000")
	canvas.create_rectangle((300,0), (400,100), fill="#000000")
	canvas.create_rectangle((400,0), (500,100), fill="#ff0000")
	canvas.create_rectangle((500,0), (600,100), fill="#000000")
	canvas.create_rectangle((600,0), (700,100), fill="#ff0000")
	canvas.create_rectangle((700,0), (800,100), fill="#000000")
	return (canvas)

def create_side_canvas(window: tk.Tk) -> tk.Canvas:
	side_canvas = tk.Canvas(window, width=300, height=800, bg="#333333")
	return (side_canvas)

def place_pieces(canvas: tk.Canvas, board: list[str]) -> None:
	y: int = 0
	for line in board:
		x: int = 0
		while (x < 8):
			if (line[x] == 'K'):
				piece = tk.PhotoImage(file="pieces/white_king.png")
			elif (line[x] == 'Q'):
				piece = tk.PhotoImage(file="pieces/white_queen.png")
			elif (line[x] == 'B'):
				piece = tk.PhotoImage(file="pieces/white_bishop.png")
			elif (line[x] == 'N'):
				piece = tk.PhotoImage(file="pieces/white_horse.png")
			elif (line[x] == 'R'):
				piece = tk.PhotoImage(file="pieces/white_rook.png")
			elif (line[x] == 'P'):
				piece = tk.PhotoImage(file="pieces/white_pawn.png")
			if (line[x] == 'k'):
				piece = tk.PhotoImage(file="pieces/black_king.png")
			elif (line[x] == 'q'):
				piece = tk.PhotoImage(file="pieces/black_queen.png")
			elif (line[x] == 'b'):
				piece = tk.PhotoImage(file="pieces/black_bishop.png")
			elif (line[x] == 'n'):
				piece = tk.PhotoImage(file="pieces/black_horse.png")
			elif (line[x] == 'r'):
				piece = tk.PhotoImage(file="pieces/black_rook.png")
			elif (line[x] == 'p'):
				piece = tk.PhotoImage(file="pieces/black_pawn.png")
			else:
				piece = None

			# if (not piece == None):
			if (piece):
				canvas.create_image((x*100, y*100), image=piece, anchor=NW)
			x += 1
		y += 1