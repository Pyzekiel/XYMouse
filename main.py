#! pip install win10toast
import pygame
import sys
#! pip install win10toast
from win10toast import ToastNotifier

tnr = ToastNotifier()

pygame.init()
# Screen:
screen_size = screen_width, screen_height = 500, 400
screen = pygame.display.set_mode(screen_size)
title = "XYMouse | Pygame"
pygame.display.set_caption(title)

# Notification And Starting:
running = True
tnr.show_toast(title, "Your Application Is Starting", duration=10, threaded=True)
thickness = 3
# Font And Out Of Bounds Exception
font = pygame.font.SysFont('calibri', 20)

while running:

	screen.fill(pygame.Color("White"))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: running = False

	# You Can Index The mouse x and y because it's a uhh umm you know the ([0], [1])
	xm = pygame.mouse.get_pos()[0]
	ym = pygame.mouse.get_pos()[1]
  
	# Seperate The Text, instead of fix position we use the length of the text
	x = f"X: {xm}"
	y = f"Y: {ym}"

	xt = font.render(f'{x}', True, pygame.Color('black'))
	yt = font.render(f'{y}', True, pygame.Color('Black'))
	screen.blit(xt, (len(x), 10))
	screen.blit(yt, (len(y), 30))

	# Y:
	pygame.draw.rect(screen, pygame.Color('Green'), (xm,0, thickness, screen_height))
	# X:
	pygame.draw.rect(screen, pygame.Color('Red'), (0,ym, 500, thickness))
	pygame.display.flip()

pygame.quit()
sys.exit()
