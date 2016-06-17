#!/usr/bin/env python

# Text-maze 4
#mazemodpath = (os.path.join('MAZE', 'sample.MOD.txt'))



#>>cosmetic only<<
##############
#wordbindings:
##############
#FORWARD
FORWARDWORDBIND=('w')
#BACKWARD
BACKWARDWORDBIND=('s')
#left
LEFTWORDBIND=('a')
#right
RIGHTWODBIND=('d')
#quit
QUITWORDBIND=('q')
##############
#import LIBTIMG
#import libtextmaze
import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
#import pygame.mixer.music
import pygame
import time
import os
from pygame.locals import *

if 'mazefilepath' in globals():
	print ("Global variable: 'mazefilepath' detected, using as maze refrence.")
else:
	print ("Global variable: 'mazefilepath' not detected, using default maze.")
	mazefilepath = (os.path.join('MAZE', 'sample.MAZE'))

#load window icon, make window, set caption, start music, init things. etc.
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('AUDIO', 'vg-mus-2_spooky-hall.ogg'))
pygame.mixer.music.play(-1)
stepfx=pygame.mixer.Sound(os.path.join('AUDIO', 'step.ogg'))

pygame.display.init()
pygame.font.init()
windowicon=pygame.image.load(os.path.join('TILE', 'icon16.png'))
pygame.display.set_icon(windowicon)
screensurf=pygame.display.set_mode((240, 370))
pygame.display.set_caption("Text-maze 4", "Text-maze 4")

#load tiles
tilewall=pygame.image.load(os.path.join('TILE', 'wall.png'))
tileplayer=pygame.image.load(os.path.join('TILE', 'player.png'))
tileplayerB=pygame.image.load(os.path.join('TILE', 'playerB.png'))
tileplayerL=pygame.image.load(os.path.join('TILE', 'playerL.png'))
tileplayerR=pygame.image.load(os.path.join('TILE', 'playerR.png'))
tilefloor=pygame.image.load(os.path.join('TILE', 'floor.png'))
tileexit=pygame.image.load(os.path.join('TILE', 'exit.png'))
winscreen=pygame.image.load(os.path.join('TILE', 'winscreen.png'))

# *.MAZE file data loader
print ("loading data from:" + mazefilepath)
n = open(mazefilepath)
datacnt = 1
for datalst in n:
	if datacnt==1:
		mazetitle = datalst.replace("\n", "")
		print ("maze title:" + datalst.replace("\n", ""))
	if datacnt==2:
		mazemodpath = (os.path.join('MAZE',  (datalst.replace("\n", ""))))
		print ('.MOD.txt file: \n' + mazemodpath)
	if datacnt==3:
		mazesizey = int(datalst.replace("\n", ""))
		print ("maze size y:" + datalst.replace("\n", ""))
	if datacnt==4:
		mazesizex = int(datalst.replace("\n", ""))
		print ('maze size x:' + datalst.replace("\n", ""))
	if datacnt==5:
		playerstarty = int((datalst.replace("\n", "")))
		print ('player start y:' + datalst.replace("\n", ""))
	if datacnt==6:
		playerstartx = int((datalst.replace("\n", "")))
		print ('player start x:' + datalst.replace("\n", ""))
	if datacnt==7:
		endposy = int((datalst.replace("\n", "")))
		print ('end pos y:' + datalst.replace("\n", ""))
	if datacnt==8:
		endposx = int((datalst.replace("\n", "")))
		print ('end pos x:' + datalst.replace("\n", ""))
	datacnt += 1
n.close()
print ("data loaded. \n")
playx = playerstartx
playy = playerstarty
debugset = ('1')
gameend = ('0')
CANTMOVE = ("Can't move in that direction.")
WINGAME = ("You win!")
lastmove="F"
def tilegriddraw():
	
	
	
	if LEFTWARD3=="0":
		screensurf.blit(tilefloor, (0, 20))
	else:
		screensurf.blit(tilewall, (0, 20))
	if RIGHTWARD3=="0":
		screensurf.blit(tilefloor, (160, 20))
	else:
		screensurf.blit(tilewall, (160, 20))
	if FORWARD2=="0":
		screensurf.blit(tilefloor, (80, 20))
	else:
		screensurf.blit(tilewall, (80, 20))
	if RIGHTWARD2=="0":
		screensurf.blit(tilefloor, (160, 100))
	else:
		screensurf.blit(tilewall, (160, 100))
	if LEFTWARD2=="0":
		screensurf.blit(tilefloor, (0, 100))
	else:
		screensurf.blit(tilewall, (0, 100))
	if FORWARD=="0":
		screensurf.blit(tilefloor, (80, 100))
	else:
		screensurf.blit(tilewall, (80, 100))
	if lastmove=="F":
		screensurf.blit(tileplayer, (80, 180))
	if lastmove=="B":
		screensurf.blit(tileplayerB, (80, 180))
	if lastmove=="L":
		screensurf.blit(tileplayerL, (80, 180))
	if lastmove=="R":
		screensurf.blit(tileplayerR, (80, 180))
	if RIGHTWARD=="0":
		screensurf.blit(tilefloor, (160, 180))
	else:
		screensurf.blit(tilewall, (160, 180))
	if LEFTWARD=="0":
		screensurf.blit(tilefloor, (0, 180))
	else:
		screensurf.blit(tilewall, (0, 180))
	if BACKWARD=="0":
		screensurf.blit(tilefloor, (80, 260))
	else:
		screensurf.blit(tilewall, (80, 260))
	if RIGHTWARD0=="0":
		screensurf.blit(tilefloor, (160, 260))
	else:
		screensurf.blit(tilewall, (160, 260))
	if LEFTWARD0=="0":
		screensurf.blit(tilefloor, (0, 260))
	else:
		screensurf.blit(tilewall, (0, 260))
	
def winscreenwait():
	while True:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				return()
#datapoint lookup function. used to read data points from the .MOD.txt file.
#when the point i out-of-range. 1 is returned.
def lookpoint(lookptx, lookpty):
	lineycnt=1
	linexcnt=1
	lookuppointis=('1')
	m = open(mazemodpath)
	for lineylst in m:
		if lineycnt==lookpty:
			for linexlst in lineylst:
				if linexcnt==lookptx:
					lookuppointis = linexlst
				linexcnt += 1
		lineycnt += 1
	return (lookuppointis)
	
simplefont = pygame.font.SysFont(None, 16)

def drawfoottext(textto, linemode):
	text = simplefont.render(textto, True, (255, 255, 255), (0, 0, 0))
	if linemode==0:
		screensurf.blit(text, (0, 340))
	if linemode==1:
		screensurf.blit(text, (0, 353))

def drawheadertext(textto, linemode):
	text = simplefont.render(textto, True, (255, 255, 255), (0, 0, 0))
	if linemode==0:
		screensurf.blit(text, (0, 0))
	if linemode==1:
		screensurf.blit(text, (0, 12))

def keyread():
	while True:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_w:
				return(FORWARDWORDBIND)
			if event.type == KEYDOWN and event.key == K_a:
				return(LEFTWORDBIND)
			if event.type == KEYDOWN and event.key == K_s:
				return(BACKWARDWORDBIND)
			if event.type == KEYDOWN and event.key == K_d:
				return(RIGHTWODBIND)
			if event.type == KEYDOWN and event.key == K_q:
				return(QUITWORDBIND)
			if event.type == KEYDOWN and event.key == K_UP:
				return(FORWARDWORDBIND)
			if event.type == KEYDOWN and event.key == K_LEFT:
				return(LEFTWORDBIND)
			if event.type == KEYDOWN and event.key == K_DOWN:
				return(BACKWARDWORDBIND)
			if event.type == KEYDOWN and event.key == K_RIGHT:
				return(RIGHTWODBIND)

#old test data
#if lookpoint(2, 2)==('0'):
#	print ('blah')
#print (lookpoint(2, 2))
cantmoveflg=0
#main loop
while gameend==('0'):
	#POV coordinate determination
	#stage0
	POVleftx0 = playx + 1
	POVlefty0 = playy - 1
	POVrightx0 = playx - 1
	POVrighty0 = playy - 1
	#stage1
	POVforwardx = playx
	POVforwardy = playy + 1
	POVbackx = playx
	POVbacky = playy - 1
	POVleftx = playx + 1
	POVlefty = playy
	POVrightx = playx - 1
	POVrighty = playy
	#stage2
	POVleftx2 = playx + 1
	POVlefty2 = playy + 1
	POVrightx2 = playx - 1
	POVrighty2 = playy + 1
	POVforwardx2 = playx
	POVforwardy2 = playy + 2
	#stage3
	POVleftx3 = playx + 1
	POVlefty3 = playy + 2
	POVrightx3 = playx - 1
	POVrighty3 = playy + 2
	POVforwardx3 = playx
	POVforwardy3 = playy + 3
	#POV point lookup
	#stage0
	LEFTWARD0 = lookpoint(POVleftx0, POVlefty0)
	RIGHTWARD0 = lookpoint(POVrightx0, POVrighty0)
	#stage1
	FORWARD = lookpoint(POVforwardx, POVforwardy)
	BACKWARD = lookpoint(POVbackx, POVbacky)
	LEFTWARD = lookpoint(POVleftx, POVlefty)
	RIGHTWARD = lookpoint(POVrightx, POVrighty)
	#stage2
	FORWARD2 = lookpoint(POVforwardx2, POVforwardy2)
	LEFTWARD2 = lookpoint(POVleftx2, POVlefty2)
	RIGHTWARD2 = lookpoint(POVrightx2, POVrighty2)
	#stage3
	FORWARD3 = lookpoint(POVforwardx3, POVforwardy3)
	LEFTWARD3 = lookpoint(POVleftx3, POVlefty3)
	RIGHTWARD3 = lookpoint(POVrightx3, POVrighty3)
	#if debugset==('1'):
	#	print ("F:" + FORWARD + " B:" + BACKWARD)
	#	print ("L:" + LEFTWARD + " R:" + RIGHTWARD)
	#	print ("F2:" + FORWARD2 + " L2:" + LEFTWARD2 + " R2:" + RIGHTWARD2)
	#	print ("F3:" + FORWARD3 + " L3:" + LEFTWARD3 + " R3:" + RIGHTWARD3)
	# 3 stage maze drawing function.
	screensurf.fill((100, 120, 100))
	tilegriddraw()
	if cantmoveflg==1:
		drawheadertext(CANTMOVE, 1)
	drawheadertext(("Text-Maze 4 | " + mazetitle), 0)
	#print(libtextmaze.mazedraw3(FORWARD, BACKWARD, LEFTWARD, RIGHTWARD, FORWARD2, LEFTWARD2, RIGHTWARD2, FORWARD3, LEFTWARD3, RIGHTWARD3))
	pygame.display.update()
	pygame.event.pump()
	
	usrentry = ('null')
	#user prompt loop
	pygame.event.clear()
	while (usrentry!=FORWARDWORDBIND and usrentry!=BACKWARDWORDBIND and usrentry!=LEFTWORDBIND and usrentry!=RIGHTWODBIND and usrentry!=QUITWORDBIND):
		drawfoottext(("forward:" + FORWARDWORDBIND + " | backward:" + BACKWARDWORDBIND), 0)
		drawfoottext(("left:" + LEFTWORDBIND + " | right:" + RIGHTWODBIND + " | quit:" + QUITWORDBIND), 1)
		pygame.display.update()
		usrentry=keyread()
		
		
	#print (chr(27) + "[2J" + chr(27) + "[H")
	#wall detection logic
	cantmoveflg=0
	if usrentry==BACKWARDWORDBIND:
		BIND1 = playy - 1
		if lookpoint(playx, BIND1)==('1'):
			cantmoveflg=1
		elif lookpoint(playx, BIND1)==('0'):
			playy -= 1
			lastmove="B"
	if usrentry==FORWARDWORDBIND:
		BIND2 = playy + 1
		if lookpoint(playx, BIND2)==('1'):
			cantmoveflg=1
		elif lookpoint(playx, BIND2)==('0'):
			playy += 1
			lastmove="F"
	if usrentry==LEFTWORDBIND:
		BIND4 = playx + 1
		if lookpoint(BIND4, playy)==('1'):
			cantmoveflg=1
		elif lookpoint(BIND4, playy)==('0'):
			playx += 1
			lastmove="L"
	if usrentry==RIGHTWODBIND:
		BIND3 = playx - 1
		if lookpoint(BIND3, playy)==('1'):
			cantmoveflg=1
		elif lookpoint(BIND3, playy)==('0'):
			playx -= 1
			lastmove="R"
	#misic user commands
	if usrentry==QUITWORDBIND:
		gameend=('1')
	#game win check
	if cantmoveflg==0:
		stepfx.play()
	if (playx==endposx and playy==endposy):
		#print(WINGAME)
		wintext = simplefont.render("Press a key.", True, (255, 255, 255), (0, 0, 0))
		wintextbox = wintext.get_rect()
		wintextbox.centerx = screensurf.get_rect().centerx
		wintextbox.centery = ((screensurf.get_rect().centery))
		winscreenbox = winscreen.get_rect()
		winscreenbox.centerx = screensurf.get_rect().centerx
		winscreenbox.centery = ((screensurf.get_rect().centery) - 60)
		screensurf.blit(winscreen, winscreenbox)
		screensurf.blit(wintext, wintextbox)
		pygame.display.update()
		pygame.event.clear()
		winscreenwait()
		gameend=1
		
		

