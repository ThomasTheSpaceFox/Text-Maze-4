#!/usr/bin/env python
import os
import pygame
import time
from pygame.locals import *
#some notes

#this is the maze selection program/main menu for Text-maze 4. the mazes are semi-softcoded. 
#what i mean is the maze engine itself can be executed from another python program that
#points it to a *.MAZE file using a global variable: "mazefilepath"
#see maze-series.py's comments for more info on this.


menitm1='similar'
menitm2='sample'
menitm3='switchback1'
#must set MAZEIS first!

MENUFLG=1

mainlist=(menitm1, menitm2, menitm3, "about", "quit")
findcnt=0
for flx in mainlist:
	findcnt += 1


titlescreen=pygame.image.load(os.path.join('TILE', 'titlescreen.png'))



pygame.mixer.init()
pygame.mixer.music.load(os.path.join('AUDIO', 'vg-mus-2_spooky-hall.ogg'))
pygame.mixer.music.play(-1)


print ('Text-maze 4 maze selection menu')
pygame.display.init()
pygame.font.init()


screensurf=pygame.display.set_mode((240, 370))
screensurf.fill((100, 120, 100))

titlescreenbox = titlescreen.get_rect()
titlescreenbox.centerx = screensurf.get_rect().centerx
titlescreenbox.centery = ((screensurf.get_rect().centery) - 90)
screensurf.blit(titlescreen, titlescreenbox)


pygame.display.set_caption("Text-maze 4 menu", "Text-maze 4")
menuhighnum=1
menusel="null"
simplefont = pygame.font.SysFont(None, 16)
ixreturn=0
while menusel!="quit":
	if ixreturn==1:
		print ("Maze execution complete, returning to menu.")
		pygame.display.set_caption("Text-maze 4 menu", "Text-maze 4 menu")
		screensurf.fill((100, 120, 100))
		screensurf.blit(titlescreen, titlescreenbox)
		ixreturn=0
	menucnt=1
	evhappenflg=0
	if menuhighnum<=0:
		menuhighnum=findcnt
	elif menuhighnum>findcnt:
		menuhighnum=1
	texhigcnt=190
	texhigjump=14
	indlcnt=1
	for indx in mainlist:
		if indlcnt==menuhighnum:
			textit=simplefont.render(indx, True, (0, 0, 0), (255, 255, 255))
		else:
			textit=simplefont.render(indx, True, (255, 255, 255), (0, 0, 0))
		screensurf.blit(textit, (0, texhigcnt))
		texhigcnt += texhigjump
		indlcnt += 1
	pygame.display.update()
	pygame.event.pump()
	pygame.event.clear()
	while evhappenflg==0:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_UP:
				menuhighnum -= 1
				evhappenflg=1
			if event.type == KEYDOWN and event.key == K_DOWN:
				menuhighnum += 1
				evhappenflg=1
			if event.type == KEYDOWN and event.key == K_RETURN:
				ixreturn=1
				evhappenflg=1
				break
	
	indlcnt2=1
	if ixreturn==1:
		#print "blk1"
		for indxB in mainlist:
			#print indxB
			if indlcnt2==menuhighnum:
				if indxB==menitm1:
					MAZEIS='similar.MAZE'
					mazefilepath=(os.path.join('MAZE', MAZEIS))
					execfile('Text-maze-4.py')
				if indxB==menitm2:
					MAZEIS='sample.MAZE'
					mazefilepath=(os.path.join('MAZE', MAZEIS))
					execfile('Text-maze-4.py')
				if indxB==menitm3:
					MAZEIS='switchback1.MAZE'
					mazefilepath=(os.path.join('MAZE', MAZEIS))
					execfile('Text-maze-4.py')
				if indxB=='quit':
					menusel="quit"
				if indxB=='about':
					execfile('about.py')
			indlcnt2 += 1
	pygame.display.update()


