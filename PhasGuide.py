import pygame
from Button import Button
from Ghosts import Ghosts
from InfoBox import InfoBox

pygame.font.init()

window = pygame.display.set_mode((1400, 910))
pygame.display.set_caption("Phasmophobia Guide")
window.fill((200, 200, 200))

reset_button = Button((255, 0, 255), 1200, 0, 200, 455, "RESET")
emf = Button((241, 246, 168), 1200, 455, 200, 65, "EMF Reader 5")
finger = Button((241, 246, 168), 1200, 520, 200, 65, "Fingerprints")
writing = Button((241, 246, 168), 1200, 585, 200, 65, "Ghost Writing")
freezing = Button((241, 246, 168), 1200, 650, 200, 65, "Freezing Temperatures")
dots = Button((241, 246, 168), 1200, 715, 200, 65, "D.O.T.S Projector")
orb = Button((241, 246, 168), 1200, 780, 200, 65, "Ghost Orbs")
box = Button((241, 246, 168), 1200, 845, 200, 65, "Spirit Box")

evidences = [
	emf,
	finger,
	writing,
	freezing,
	dots,
	orb,
	box
]

evid_strings = [
	"emf",
	"finger",
	"writing",
	"freezing",
	"dots",
	"orb",
	"box"
]

yes = []
no = []

ghosts = Ghosts()

buttons = ghosts.getGhosts()
info = ghosts.getInfo()
ghost_evidences = ghosts.getEvidence()


run = True
while run:
	reset_button.draw(window)
	for i in evidences:
		i.draw(window)
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
			for i in evidences:
				if i.color != (255, 128, 0):
					if i.mouseOver(position): i.color = (219, 219, 219)
					else: i.color = (255, 178, 102)
			if reset_button.mouseOver(position): reset_button.color = (219, 219, 219)
			else: reset_button.color = (255, 0, 255)

		if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
			for i in buttons:
				if i.mouseOver(position): i.cross()

			for i in range(len(evidences)):
				if evidences[i].mouseOver(position):
					if (evidences[i].color == (255, 128, 0)): # when false evidence
						evidences[i].color = (241, 246, 168) # orange
						evidences[i].cross()
						if evid_strings[i] not in no: no.append(evid_strings[i])
						if evid_strings[i] in yes: yes.remove(evid_strings[i])
						break

					elif (evidences[i].isCrossed): # when no evidence
						evidences[i].cross()
						if evid_strings[i] in yes: yes.remove(evid_strings[i])
						if evid_strings[i] in no: no.remove(evid_strings[i])
						break

					else: # when true evidence
						if evid_strings[i] not in yes: yes.append(evid_strings[i])
						if evid_strings[i] in no: no.remove(evid_strings[i])
						evidences[i].color = (255, 128, 0) # dark orange
						break

			if (position[0] >= 1200 and position[0] <= 1400 and position[1] >= 455 and position[1] <= 910):
				for i in buttons:
					if i.isCrossed: i.cross()

				for i in yes:
					for j in range(len(ghost_evidences)):
						if i not in ghost_evidences[j] and not buttons[j].isCrossed: buttons[j].cross()

				for i in no:
					for j in range(len(ghost_evidences)):
						if i in ghost_evidences[j] and not buttons[j].isCrossed: buttons[j].cross()


			if reset_button.mouseOver(position):
				window.fill((200, 200, 200))
				for i in buttons:
					if i.isCrossed: i.cross()

				for i in evidences:
					if (i.isCrossed): i.cross()
					if (i.color == (255, 128, 0)): i.color = (241, 246, 168)
				yes = []
				no = []

		if e.type == pygame.MOUSEBUTTONDOWN and e.button == 3:
			for i in range(len(buttons)):
				if buttons[i].mouseOver(position):
					window.fill((200, 200, 200))
					box = InfoBox(info[i])
					box.draw(window)