#!/usr/bin/env python

## Index
'''
	- Libraries
	- Loading images
	- Events functions
	- Variables definition
	- Main body
'''

## Libraries 

import rospy
import pyglet
from pyglet.window import mouse
from pyglet.window import key
from pyglet import clock
import miscellanea_functions as f
from miscellanea_classes import *
import os

## Loading images
print(os.listdir('Images and multimedia/'))
logo=pyglet.image.load('Images and multimedia/Images/logo.jpeg')
logo1=f.load_gif('./Images and multimedia/background_animation/slide1/')	

## Variables definition

window = pyglet.window.Window(width=1000,height=1200,resizable=True,vsync=True)
batch=pyglet.graphics.Batch()
fps_display=pyglet.clock.ClockDisplay()
t=1
index=1
dreaw=Button(logo,10,10,20,50,batch,window,f.write)
label=Text('Hello,world','Arial',36,500,400,(255,255,255,255))
first=Slide('Main',
				 1,
				 logo1,
				 f.nada,
				 window)
second=Slide('second',
				 2,
				 logo,
				 f.nada,
				 window)
## Functions

# A generic key is pressed

@window.event
def on_key_press(symbol, modifiers):
		global index
		global t
		print('A key was pressed')
		label.update_text(str('Ciaaaaaaooooo'))
		if index==1:
			index=2
		else:
			index=1
		global t
		t=0
		
@window.event
def on_mouse_drag(x,y,dx,dy,button,modifiers):
	print(dy)
	if button & mouse.LEFT and (dy>20 or dy<-20):
		print('Scrolled')
	
@window.event
def on_draw():
		global t
		global index
		window.clear()
		if index==1:
			first.show()
		else:
			second.show()
		#fps_display.draw()
		if t==1:
			dreaw.draw()
		label.draw()

## Main body

if __name__ == '__main__':
	rospy.init_node('GUI', anonymous=True)
	pyglet.app.run()
