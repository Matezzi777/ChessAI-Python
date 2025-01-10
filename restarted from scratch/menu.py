import pygame
import sys
from buttons import Button, ButtonPlay, ButtonOptions, ButtonQuit
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MAIN_MENU_BACKGROUND_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR, MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_POLICE_COLOR

#SCENES
class Menu:
	def __init__(self, screen: pygame.Surface) -> None:
		self.screen: pygame.Surface = screen
		self.running: bool = True
		self.buttons: list[Button] = [ButtonPlay((SCREEN_WIDTH/2,SCREEN_HEIGHT/2), MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR),
								ButtonOptions((SCREEN_WIDTH/2,SCREEN_HEIGHT/2+75), MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR),
								ButtonQuit((SCREEN_WIDTH/2,SCREEN_HEIGHT/2+150), MAIN_MENU_BUTTONS_IDLE_COLOR, MAIN_MENU_BUTTONS_CLICKED_COLOR)]

	def handle_events(self) -> None:
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:
			button.change_color(mouse_position)
			button.update(self.screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("MAIN MENU : Close Window clicked")
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
		title_rect = title.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/4))
		self.screen.blit(title, title_rect)
		pygame.display.flip()

	def run(self) -> None:
		while (self.running):
			self.handle_events()
			self.display()