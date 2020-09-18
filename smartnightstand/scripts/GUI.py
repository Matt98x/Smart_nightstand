#!/usr/bin/env python

import rospy
import pyglet
from pyglet.window import mouse
from pyglet.window import key




window = pyglet.window.Window(width=1000,height=1000,resizable=True,vsync=True)
batch=pyglet.graphics.Batch()


label=pyglet.text.Label('Hello,world',
						font_name='Arial',
						font_size=36,
						x=window.width//2,y=window.height//2,
						anchor_x='center',anchor_y='center')

#EVENTS Functions
# A generic key is pressed
@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')
    
@window.event
def on_draw():
    window.clear()
    batch.draw()
    label.draw()
   
	
    
#Main body
if __name__ == '__main__':
	rospy.init_node('GUI', anonymous=True)
	pyglet.app.run()
