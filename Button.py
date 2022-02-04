import pygame

class Button:
	def __init__(self, color, x, y, text):
		self.color = color
		self.x = x;
		self.y = y;
		self.width = 200
		self.height = 130
		self.text = text
		self.name = text
		self.isCrossed = False

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

		font = pygame.font.SysFont('centaur', int(self.width / len(self.text))+5)
		text = font.render(self.text, 1, (0, 0, 0))
		window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
		if (self.isCrossed):
			font = pygame.font.SysFont('inkfree', 150, bold = pygame.font.Font.bold)
			text = font.render('X', 1, (0, 0, 0))
			window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

	def mouseOver(self, position):
		if position[0] > self.x and position[0] < self.x + self.width and position[1] > self.y and position[1] < self.y + self.height: return True
		return False

	def cross(self):
		if (self.isCrossed):
			self.isCrossed = False
		else:
			self.isCrossed = True

	def recover(self):
		if (self.text != self.name): self.text = self.name