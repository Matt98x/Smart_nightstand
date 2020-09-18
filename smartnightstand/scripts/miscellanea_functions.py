import rospy
import pyglet
from pyglet.window import mouse
from pyglet.window import key
from pyglet import clock
import os

def nada():
	pass

def write():
	print('hello')

# function to load a gif from a foulder represented in txt (convert -verbose -coalesce ../Animated\ GIF-downsized_large.gif %03d.png)
def load_gif(text):
	background_animation=[]
	background_animation_list=os.listdir(text)
	for i in range(len(background_animation_list)):
		k=str(i)
		p=k.zfill(3)
		background_animation.append(pyglet.image.load(text+p+'.png'))
	gif=pyglet.image.Animation.from_image_sequence(background_animation,0.1,loop=True)
	return gif
	
# Upper_curtain show
def upper_curtain_show():
	pass

# Upper_curtain pressed function
def upper_curtain_pressed():
	pass
