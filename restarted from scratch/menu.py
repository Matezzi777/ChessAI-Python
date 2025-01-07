import pygame
from buttons import Button

MAIN_MENU_BACKGROUND_COLOR = (48, 46, 43)
MAIN_MENU_POLICE_COLOR = (49, 100, 71)
MAIN_MENU_BUTTONS_TEXT_COLOR = (148, 147, 145)
MAIN_MENU_BUTTONS_IDLE_COLOR = (105, 103, 100)
MAIN_MENU_BUTTONS_CLICKED_COLOR = (49, 100, 71)

class Menu:
	def __init__(self, screen, police) -> None:
		self.screen = screen
		self.police = police
		self.running: bool = True

	def idle(self) -> None:
		draw_background(self.screen)
		draw_buttons(self.screen)
		draw_text(self.screen)

	def handle_events(self) -> None:
		...

	def run(self) -> None:
		while (self.running):
			self.idle()
			self.handle_events()

def draw_background(screen) -> None:
	screen.fill(MAIN_MENU_BACKGROUND_COLOR)

def draw_buttons(screen) -> None:
	play_button = Button()

def draw_text(screen) -> None:
	...