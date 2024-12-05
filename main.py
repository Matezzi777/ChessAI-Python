from window import *
from ui import *
from board import *

#INITIALISATION
window: tk.Tk = create_window()
board: list[str] = board_init()
board_canvas: tk.Canvas = create_board(window)
place_pieces(board_canvas, board)
board_canvas.place(x=50, y=50)
side_canvas: tk.Canvas = create_side_canvas(window)
side_canvas.place(x=900, y=50)


window.mainloop()