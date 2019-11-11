# -*- coding: utf-8 -*-

import core.config.helpme as opciones
import core.config.banners as banners

from core.config.clrscr import clrscr
from core.dictionary.by_letter import search_by_letter
from core.dictionary.by_pattern import search_by_pattern

def computer_kingdom_menu():

	selector = 0

	while(selector!="exit"):

		if(selector=="1"):

			search_by_letter()

		elif(selector=="2"):

			search_by_pattern()

		clrscr()
		print(banners.brainBanner)
		print(opciones.menu)
		selector = input(' CPK > ')
