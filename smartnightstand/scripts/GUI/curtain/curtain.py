import sys
sys.path.insert(1,'../')
from miscellanea_classes import *
from miscellanea_functions import *
import config


p=1
general=config.general
window=config.window
batch=config.batch

def build_curtain():
	global p,general,window,batch
	upper_curtain=Button(config.curtain_logo,'slides',window.width/2-100,window.height-50,200,55,batch,window,curtain_pressed)
	curtain1=Sprite(config.curtain_logo,0,window.height-200,window.width,250,window,batch)
	curtain1.visible=False
	general.buttons.append(upper_curtain)
	general.sprites.append(curtain1)

# Curtain retracted
def curtain_pressed():
		global p,window,batch,general
		if p==0:
			p=1
			general.buttons[0].set_button_position(int(window.width/2-general.buttons[0].width_/2),int(window.height-general.buttons[0].height_+5))
			general.sprites[0].visible=False
		else:
			p=0
			general.buttons[0].set_button_position(int(window.width/2-general.buttons[0].width_/2),int(general.sprites[0].y-general.buttons[0].height_))
			general.sprites[0].visible=True
			


