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
	print(config.window.height)
	date_text=Text(config.date_dmy,'Arial',14,35,config.window.height-470-100,color=(255,255,255,255))
	general.sprites.append(main_sprite_left)
	general.sprites.append(main_sprite_right)
	general.texts.append(date_text)
	

