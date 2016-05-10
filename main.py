import sys
import pygame
from pygame.sprite import Sprite

# Screen constants
screen_width  = 600
screen_height = 600
screen_size = (screen_width, screen_height)

def main():
	pygame.init()

	screen = pygame.display.set_mode(screen_size)

	# Main loop
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()

if __name__ == "__main__":
	main()