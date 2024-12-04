from tkinter import *

window = Tk()
window.geometry('400x400')
window.title('AI Chess')
window['bg'] = 'blue'
window.resizable(width = False, height = False)

label = Label(window, text="Click counter", font=("Arial", 20, "bold"), fg="white", bg="blue").pack(side=TOP, pady=150)
button = Button(window, text="Click me !", bg = "red", fg = "white").pack(side=TOP, pady=0)

window.mainloop()