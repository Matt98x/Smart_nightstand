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
				 window,
				 batch):
		pyglet.sprite.Sprite.__init__(self,image,x,y,batch=batch)
		self.window=window
		self.p=float(x)/window.width
		self.q=float(y)/window.height
		self.r=float(width)/window.width
		self.t=float(height)/window.height
		self.width_=width
		self.height_=height
		
	def update(self):
		self.width_=int(self.r*self.window.width)
		self.height_=int(self.t*self.window.height)
		new_x=int(self.p*self.window.width)
		new_y=int(self.q*self.window.height)
		self.set_position(new_x,new_y)
		self._texture.width=self.width_
		self._texture.height=self.height_
		self._update_position()
		
	def change_color(self,r,g,b,t):
		self._set_color((r,g,b))
		self._set_opacity(t)

# Button class (on screen button)

class Button(Sprite):

	def __init__(self,
				 image,
				 text,
				 x,
				 y,
				 width,
				 height,
				 batch,
				 window,
				 function):
		Sprite.__init__(self,image,x,y,width,height,window,batch)
		self.image=image
		print(width,height)
		self.text=Text(text,'Arial',12,x+width/2,y+height/2,color=(255,255,255,255))
		self.set_button_text()
		window.push_handlers(self.on_mouse_press)
		self.function=function
		self.window=window
		
		
		
	
	def on_mouse_press(self,x,y,button,modifiers):
		if x>self.x and x<self.x+self.width_ and y>self.y and y<self.y+self.height_:
			self.function()
			
		
	def show(self):
		self.update()
		self.draw()
		self.set_button_text()
		self.text.draw()
	
	def set_button_position(self,x,y):
		self.p=float(x)/self.window.width
		self.q=float(y)/self.window.height
		self.update()
		
	def set_button_text(self):
		self.text.update_position('center','center',self.x+self.image.width/2,self.y+self.image.height/2)
        	
        
			
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
						color=color
						)
			self.label.margin_botto=0
			self.label.color=color
			self.x=x
			self.y=y
			self.label.begin_update()
			self.label.x=self.x
			self.label.y=self.y
			self.label.end_update()

	def draw(self):
		self.label.draw()
		
	def update_text(self,text):
		self.label.text=text
		
	def update_position(self,anchor_x,anchor_y,x,y):
		self.label.begin_update()
		self.label.anchor_x=anchor_x
		self.label.anchor_y=anchor_y
		self.label.x=x
		self.label.y=y
		self.label.end_update()
		
		
# Create a background

class Background():
	def __init__(self,
				 image,
				 window,
				 batch):
			self.window=window
			self.image=image
			self.animation=Sprite(self.image,0,0,window.width,window.height,window,batch)
	
	def draw_background(self):
		self.update()
		self.animation.draw()
	
	def update(self):
		self.animation.update()
		
		
# Slide class

class Slide():
	def __init__(self,
				 title,
				 index,
				 background,
				 show_func,
				 window,
				 batch):
			self.back=Background(background,window,batch)
			self.showf=show_func
	def show(self):
		self.back.draw_background()
		self.showf()

# Graphic object

class Graphic_object():
	def __init__(self,
				 window,
				 batch,
				 update_texts):
			self.buttons=[]
			self.texts=[]
			self.sprites=[]
			self.backgrounds=[]
			self.update_texts=update_texts
	def show(self):
		self.update_texts()
		for i in self.backgrounds:
				i.draw_background()
		for i in self.sprites:
				i.update()
				i.draw()
		for i in self.buttons:
				i.show()
		for i in self.texts:
				i.draw()
		


