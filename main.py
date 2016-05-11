import sys
import pygame
from pygame.sprite import Sprite

class MainWindow:
	'''Handle the main game window'''
	def __init__(self, width=640, height=480, title="Main window"):
		pygame.init()

		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

		pygame.display.set_caption(title)

	def MainLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
		

if __name__ == "__main__":
	window = MainWindow(title="Line follower simulator")
	window.MainLoop()