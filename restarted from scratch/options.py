import pygame
import sys
import buttons

class Options:
	def __init__(self, screen):
		self.running: bool = True
		self.screen: pygame.Surface = screen
		self.buttons: list[buttons.Button] = []

	def handle_events(self):
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:
			button.change_color(mouse_position)
			button.update(mouse_position)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("OPTIONS : Close Window clicked")
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				...

	def display(self):
		self.screen.fill((0, 0, 255))
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handle_events()
			self.display()