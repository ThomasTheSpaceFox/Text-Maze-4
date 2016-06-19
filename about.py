#!/usr/bin/env python
import os
import pygame
import time
from pygame.locals import *
#some notes

#this acts as a simple file parser that will show the contents of a file in a pygame window. 
#in this case it is used for the about screen (using the text file: 'live-about.txt'

pygame.display.init()
pygame.font.init()

screensurf=pygame.display.set_mode((400, 260))
screensurf.fill((100, 120, 100))
pygame.display.set_caption("Text-maze 4 about", "Text-maze 4 about")
simplefont = pygame.font.SysFont(None, 16)
abt = open('live-about.txt')
pixcnt1=0
pixjmp=14

for fnx in abt:
	fnx=fnx.replace('\n', '')
	abttext=simplefont.render(fnx, True, (255, 255, 255), (0, 0, 0))
	screensurf.blit(abttext, (0, pixcnt1))
	pixcnt1 += pixjmp
pygame.display.update()
evhappenflg2=0
while evhappenflg2==0:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_RETURN:
				evhappenflg2=1
				break
screensurf=pygame.display.set_mode((240, 370))