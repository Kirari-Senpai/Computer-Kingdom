
# -*- coding: utf-8 -*-


import core.config.helpme as opciones
import core.config.banners as banners

from core.config.clrscr import clrscr
from core.dictionary.by_letter import search_by_letter

def computer_kingdom_menu():

	clrscr()
	print(banners.brainBanner)
	print(opciones.menu)

	selector = input(' CPK > ')

	while(selector!="exit"):

		if(selector=="1"): 
			clrscr()
			print(banners.brainBanner)
			search_by_letter()
			clrscr()
			print(banners.brainBanner)
		
		selector = input(' CPK > ')