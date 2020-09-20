#!/usr/bin/env python

## /usr/lib/python2.7/dist-packages/pyglet/sprite.py
## Index
'''
	- Libraries
	- Loading images
	- Events functions
	- Variables definition
	- Main body
'''

## Libraries 
import os
import rospy
import pyglet
import sys
import config
from pyglet.window import mouse
from pyglet.window import key
from pyglet import clock
import miscellanea_functions
sys.path.insert(1,'./curtain')
from curtain import *
sys.path.insert(1,'./Main')
from Main import *

def update_text_curtain():
	pass
def update_text_main():
	config.Main.texts[0].update_text(config.date_dmy)


build_curtain()
build_main()
config.Main.update_texts=update_text_main

second=Slide('second',
				 2,
				 config.logo,
				 nada,
				 window,
				 batch)

config.slides.append(config.general)
config.slides.append(config.Main)

@window.event
def on_key_press(symbol, modifiers):

		if config.index==1:
			config.index=2
		else:
			config.index=1

		
	
@window.event
def on_draw():
		
		
		window.clear()
		
		if config.index==1:
			config.slides[1].show()
		else:
			second.show()
		#fps_display.draw()
		config.slides[0].show()
		


## Main body

if __name__ == '__main__':
	rospy.init_node('GUI', anonymous=True)
	pyglet.app.run()
