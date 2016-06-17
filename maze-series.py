#!/usr/bin/env python
import os

#some notes

#if the variable "mazefilepath" is unset when Text-maze.py is run, 
#it will default to: "(os.path.join('MAZE', 'sample.MAZE'))"
#(os.path.join is used for cross-platform compatibility resons.)
print ("this is a simple placeholder for the maze selection program, \n it will run Text-maze 4 with a series of mazes. \n")
execfile('Text-maze-4.py')
#you can choose a maze by pointing this to the *.MAZE of your choice. 
#(make sure its the *.MAZE and not the *.MOD.txt !!!
MAZEIS='similar.MAZE'

#mazes must be in the "MAZE" direcory!
#(the *.MOD.txt files are always looked for in there!)

mazefilepath=(os.path.join('MAZE', MAZEIS))
execfile('Text-maze-4.py')

MAZEIS='switchback1.MAZE'
mazefilepath=(os.path.join('MAZE', MAZEIS))
execfile('Text-maze-4.py')