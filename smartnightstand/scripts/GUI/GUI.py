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
from pprint import pprint

a=2
print(globals()['a'])
def update_text_curtain():
	pass
def update_text_main():
	config.Main.buttons[0].text.text=config.date_dmy
	config.Main.buttons[1].text.text=config.hour_hms


build_curtain()
build_main()
config.Main.update_texts=update_text_main

text=Paragraph("ciao","Arial",12,50,50,'left','top',(255,255,255,255))


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
		
		global date,a
		window.clear()
		config.update_date_hour()
		if config.index==1:
			config.slides[1].show()
		else:
			text.multiline=True
			text.width=20
			text.update_position(0,config.window.height)
			text.text="happy\ncome\nstai adsjnkasdnjkasjndkajsndkajsndkjanskdjnaskdjnaksdjnaksdnjkasjdnkasjndkjsankdnkasndkjasndkjasnkd"

		#fps_display.draw()
		config.slides[0].show()
		text.draw()

		


## Main body

if __name__ == '__main__':
	rospy.init_node('GUI', anonymous=True)
	pyglet.app.run()
