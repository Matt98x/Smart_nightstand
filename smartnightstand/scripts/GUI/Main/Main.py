import sys
sys.path.insert(1,'../')
from miscellanea_classes import *
from miscellanea_functions import *
import config


general=config.Main
window=config.window
batch=config.batch

def build_main():
	global general,window,batch
	main_back1=Background(config.logo1,window,batch)
	main_sprite_left=Sprite(config.curtain_logo,25,50,config.window.width/2-50,config.window.height-150,config.window,config.batch)
	main_sprite_right=Sprite(config.curtain_logo,config.window.width/2+25,50,config.window.width/2-75,config.window.height-150,config.window,config.batch)
	general.backgrounds.append(main_back1)
	main_sprite_left.change_color(0,0,255,200)
	main_sprite_right.change_color(0,0,255,200)
	date_text=Button(config.curtain_logo,config.date_dmy,35,window.height-150,200,55,batch,window,nada)
	date_text.change_color(0,0,0,0)
	hour_text=Button(config.curtain_logo,config.hour_hms,35,window.height-300,window.width/2-75,55,batch,window,nada)
	hour_text.text.font_size=70
	hour_text.change_color(0,0,0,0)
	general.sprites.append(main_sprite_left)
	general.sprites.append(main_sprite_right)
	general.buttons.append(date_text)
	general.buttons.append(hour_text)

