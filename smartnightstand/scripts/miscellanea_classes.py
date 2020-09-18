import pyglet
from pyglet.window import mouse
from pyglet.window import key
from pyglet.gl import *
from pyglet import clock
from pyglet import event
from pyglet import graphics
from pyglet import image
from pyglet import clock

# Extended pyglet.sprite.Sprite for extended functionalities

class Sprite(pyglet.sprite.Sprite):
	def __init__(self,
				 image,
				 x,
				 y,
				 width,
				 height,
				 window):
		pyglet.sprite.Sprite.__init__(self,image,x,y)
		self.window=window
		
	def update(self):
		self._texture.width=self.window.width
		self._texture.height=self.window.height
		self._update_position()
		
	

# Button class (on screen button)

class Button(Sprite):

	def __init__(self,
				 image,
				 x,
				 y,
				 width,
				 height,
				 batch,
				 window,
				 function):
		Sprite.__init__(self,image,x,y,width,height,window)
		self.image=image
		window.push_handlers(self.on_mouse_press)
		self.function=function
	
	def on_mouse_press(self,x,y,button,modifiers):
		if x>self.x and x<self.x+self.image.width and y>self.y and y<self.y+self.image.height:
			self.function()
			

        	
        
			
# Text class (on screen text)

class Text():
	def __init__(self,
				 text,
				 font,
				 font_size,
				 x,y,
				 color):
			
			self.label=pyglet.text.Label(text,
						font_name=font,
						font_size=font_size,
						x=x,y=y,
						anchor_x='center',
						anchor_y='center'
						)
			self.label.color=color

	def draw(self):
		self.label.draw()
		
	def update_text(self,text):
		self.label.text=text
		
		
# Create a background

class Background():
	def __init__(self,
				 image,
				 window):
			self.window=window
			self.image=image
			self.animation=Sprite(self.image,0,0,window.width,window.height,window)
	
	def draw_background(self):
		self.animation.update()
		self.animation.draw()
		
		
# Slide class

class Slide():
	def __init__(self,
				 title,
				 index,
				 background,
				 show_func,
				 window):
			self.back=Background(background,window)
			self.showf=show_func
	def show(self):
		self.back.draw_background()
		self.showf()

# Graphic object

class Graphic_object():
	def __init__(self,
				 x,y,
				 width,
				 height,
				 function,
				 show_func,
				 window):
			self.x=x
			self.y=y
			self.width=width
			self.height=height
			self.showf=show_func
			window.push_handlers(self.on_mouse_press)
			self.function=function
	
	def show(self):
		self.showf()
	
	def on_mouse_press(self,x,y,button,modifiers):
		if x>self.x and x<self.x+self.width and y>self.y and y<self.y+self.height:
			self.function()
