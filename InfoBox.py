import pygame

class InfoBox:
	def __init__(self, info):
		self.info = info
		
	def draw(self, window):
		font = pygame.font.SysFont('centaur', 75)
		text = font.render(self.info[0], 1, (0, 0, 0))
		window.blit(text, (650, 50))
		for i in range(1, len(self.info)):
			font = pygame.font.SysFont('centaur', 25)
			text = font.render(self.info[i], 1, (0, 0, 0))
			window.blit(text, (650, 50 * (i + 1)))

print(pygame.font.get_fonts())