import rospy
import pyglet
import sys
from pyglet import clock
from miscellanea_classes import *
from miscellanea_functions import *
import datetime
import os

# Images loading
logo=pyglet.image.load('Images and multimedia/Images/logo.jpeg')
curtain_logo=pyglet.image.load('Images and multimedia/Images/image_1.jpg')
logo1=load_gif('./Images and multimedia/background_animation/slide1/')


# System variables	
window = pyglet.window.Window(width=1000,height=1200,resizable=True,vsync=True)
batch=pyglet.graphics.Batch()
fps_display=pyglet.clock.ClockDisplay()

# Miscellanea Variables
t=1
index=1
slides=[]
today=datetime.datetime.today()
date_dmy=today.strftime("%A %d %B %Y")
print(date_dmy)

# Slides constructors
general=Graphic_object(window,batch,nada)
Main=Graphic_object(window,batch,nada)
Calendar=Graphic_object(window,batch,nada)



