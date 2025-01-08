import pygame
import sys
from buttons import Button, ButtonPlay, ButtonOptions, ButtonQuit

#COLORS
MAIN_MENU_BACKGROUND_COLOR = (48, 46, 43)
MAIN_MENU_POLICE_COLOR = (49, 100, 71)
MAIN_MENU_BUTTONS_TEXT_COLOR = (148, 147, 145)
MAIN_MENU_BUTTONS_IDLE_COLOR = (105, 103, 100)
MAIN_MENU_BUTTONS_CLICKED_COLOR = (49, 100, 71)

#SCENES
class Menu:
	def __init__(self, screen: pygame.Surface) -> None:
		self.screen: pygame.Surface = screen
		self.running: bool = True
		self.buttons: list[Button] = [ButtonPlay((450,400), MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR),
								ButtonOptions((450,500), MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR),
								ButtonQuit((450,600), MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR)]

	def handle_events(self) -> None:
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:
			button.change_color(mouse_position)
			button.update(self.screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("MAIN MENU : Window cross clicked")
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in self.buttons:
					if (button.check_for_input(mouse_position)):
						button.callback(self.screen)
	
	def display(self) -> None:
		self.screen.fill(MAIN_MENU_BACKGROUND_COLOR)
		for button in self.buttons:
			button.update(self.screen)
		title = pygame.font.SysFont("Arial", 100).render("Chess AI", True, MAIN_MENU_POLICE_COLOR)
		title_rect = title.get_rect(center=(450,200))
		self.screen.blit(title, title_rect)
		pygame.display.flip()

	def run(self) -> None:
		while (self.running):
			self.handle_events()
			self.display()