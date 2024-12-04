import tkinter as tk
from tkinter import ttk

def create_window() -> tk.Tk:
	window = tk.Tk()
	window.title('AI Chess')
	window.geometry('1200x900')
	window.resizable(width=False, height=False)
	window.configure(bg="#333333")
	return (window)