from window import *
from ui import *
from board import *

window: tk.Tk = create_window()
board: list[str] = board_init()
board_canvas: tk.Canvas = create_board(window)
board_canvas.place(x=25, y=50)
side_canvas: tk.Canvas = create_side_canvas(window)
side_canvas.place(x=875, y=50)

window.mainloop()