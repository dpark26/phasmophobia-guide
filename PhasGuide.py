import pygame
from Button import Button
from Ghosts import Ghosts
from InfoBox import InfoBox

pygame.font.init()

window = pygame.display.set_mode((1200, 910))
pygame.display.set_caption("Phasmophobia Guide")
window.fill((200, 200, 200))

ghosts = Ghosts()

buttons = ghosts.getGhosts()
info = ghosts.getInfo()


run = True
while run:
	for i in buttons:
		if (i.color != (0, 0, 0)): i.draw(window)
	pygame.display.update()
	for e in pygame.event.get():
		if e.type == pygame.QUIT: run = False

		position = pygame.mouse.get_pos()

		if e.type == pygame.MOUSEMOTION:
			for i in buttons:
				if i.mouseOver(position): i.color = (219, 219, 219)
				else: i.color = (255, 178, 102)

		if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
			for i in buttons:
				if i.mouseOver(position): i.cross()

		if e.type == pygame.MOUSEBUTTONDOWN and e.button == 3:
			for i in range(len(buttons)):
				if buttons[i].mouseOver(position):
					window.fill((200, 200, 200))
					box = InfoBox(info[i])
					box.draw(window)