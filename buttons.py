import pygame
import sys
from game import Game
from options import Options
from constants import BUTTON_BACKGROUND_COLOR

#GENERIC BUTTON CLASS
class Button:
	def __init__(self,
			  image,
			  position: tuple[int, int],
			  text_input: str,
			  font,
			  base_color: tuple[int, int, int],
			  hovering_color: tuple[int, int, int]):
		self.image: pygame.Surface = image
		self.x_pos: int = position[0]
		self.y_pos: int = position[1]
		self.font = font
		self.base_color: tuple[int, int, int] = base_color
		self.hovering_color: tuple[int, int, int] = hovering_color
		self.text_input: str = text_input
		self.text: pygame.Surface = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect: pygame.Rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect: pygame.Rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen: pygame.Surface):
		if (self.image is not None):
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def check_for_input(self, position: tuple[int, int]):
		if ((position[0] in range(self.rect.left, self.rect.right)) and (position[1] in range(self.rect.top, self.rect.bottom))):
			return (True)
		return (False)

	def change_color(self, position: tuple[int, int]):
		if ((position[0] in range(self.rect.left, self.rect.right)) and (position[1] in range(self.rect.top, self.rect.bottom))):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	def callback(self, screen):
		...

#MAIN MENU
class ButtonPlay(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="PLAY",
				   font = pygame.font.SysFont("Arial", 50),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("MAIN MENU : PLAY pressed")
		scene = Game(screen)
		scene.run()

class ButtonOptions(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="OPTIONS",
				   font = pygame.font.SysFont("Arial", 50),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("MAIN MENU : OPTIONS pressed")
		scene = Options(screen)
		scene.run()

class ButtonQuit(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="QUIT",
				   font = pygame.font.SysFont("Arial", 50),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("MAIN MENU : QUIT pressed")
		pygame.quit()
		sys.exit()

#OPTIONS
class ButtonColorChoice(Button):
	def __init__(self, position: tuple[int, int]):
		super().__init__(image = None,
				   position = position,
				   text_input = "",
				   font = ...,
				   base_color = (),
				   hovering_color = ())

#GAME
class ButtonGetBetterMove(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="GET BETTER MOVE",
				   font = pygame.font.SysFont("Arial", 35),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("GAME : GET BETTER MOVE pressed")
		...

class ButtonAnalyzePosition(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="ANALYZE POSITION",
				   font = pygame.font.SysFont("Arial", 35),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("GAME : ANALYZE POSITION pressed")
		...

class ButtonTurnBoard(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="TURN BOARD",
				   font = pygame.font.SysFont("Arial", 35),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("GAME : TURN BOARD pressed")
		...

class ButtonResign(Button):
	def __init__(self, position: tuple[int, int], base_color: tuple[int, int, int], hover_color: tuple[int, int, int]):
		super().__init__(image=None,
				   position=position,
				   text_input="RESIGN",
				   font = pygame.font.SysFont("Arial", 35),
				   base_color = base_color,
				   hovering_color = hover_color)

	def callback(self, screen):
		print("GAME : RESIGN pressed")
		...