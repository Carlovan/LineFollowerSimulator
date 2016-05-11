import sys
from   utils import *
import pygame
from   pygame.sprite import Sprite

class Robot(pygame.sprite.Sprite):
	'''Handle a line following robot'''
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((20, 20))
		self.image.fill((255,0,0))

		self.rect = pygame.Rect(10, 10, 20, 20)


class MainWindow:
	'''Handle the main game window'''
	def __init__(self, width=640, height=480, title="Main window"):
		pygame.init()

		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

		pygame.display.set_caption(title)

		self.robot = Robot()
		self.robots = pygame.sprite.RenderPlain(self.robot)

	def MainLoop(self):
		# Erase screen
		self.screen.fill((255,255,255))

		self.robots.draw(self.screen)

		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
		

if __name__ == "__main__":
	window = MainWindow(title="Line follower simulator")
	window.MainLoop()