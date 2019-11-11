# -*- coding: UTF-8 -*-

import re
import requests
import sys
import signal
import webbrowser
from bs4 import BeautifulSoup

letras = [chr(ord('a')+x) for x in range(0, 26)]

def exit_for_signal(signum, frame):

	print('CTRL-C')
	sys.exit(1)

def search_by_pattern():

	signal.signal(signal.SIGINT, exit_for_signal)
	signal.signal(signal.SIGTERM, exit_for_signal)
	signal.signal(signal.SIGUSR1, exit_for_signal)
	signal.signal(signal.SIGUSR2, exit_for_signal)

	print()
	print('\033[1;3;37mSeleccione una letra:\033[0m', end='\n\n')

	for _ in letras:

		print('\033[1;34m*\033[0m) \033[1;37m~ \033[3m%c\033[0m' % (_.upper()))

	print()

	letter = input('Letra: ').lower()

	if not (letter.strip()):

		print('Debe seleccionar una letra')
		sys.exit(0)

	if (re.match(r'(?![a-zA-Z])', letter)):

		print('¡%s, no es una letra!' % (letter))
		sys.exit(0)

	else:

		letter = letter[0]

	content = requests.get('http://www.alegsa.com.ar/Dic/%c.htm' % (letter)).content
	scrap = BeautifulSoup(content, 'lxml').body
	list_scrap = []

	[list_scrap.append((x['href'], x.text)) for x in scrap.find_all(attrs={'id':'wrapper'})[3].find_all('a')]

	print()

	[print('\033[1;34m*\033[0m) \033[1;37m~ \033[3m%s\033[0m' % (x[1])) for x in list_scrap]

	print()

	pattern_to_search = input('Patrón: ')

	if not (pattern_to_search):

		print('No se introdujo un patrón')
		sys.exit(0)

	patterns = [(x[0], x[1]) for x in [(x[0], re.search(pattern_to_search, x[1], re.IGNORECASE)) for x in list_scrap] if not (x[1] == None)]

	if (patterns == []):

		print('No se encontraron coincidencias')
		sys.exit(1)

	print('\033[1;37m%d\033[0m ~ \033[1;3;37mCoincidencias\033[0m:' % (len(patterns)))
	print()

	for i, _ in enumerate(patterns):

		compiled = [str(x) for x in _[1].string]
		compiled[_[1].start():_[1].end()] = '\033[1;31m%s\033[0m' % (''.join(compiled[_[1].start():_[1].end()]))

		print('\033[1;34m%d\033[0m) \033[1;37m~ \033[3m%s\033[0m' % (i, ''.join(compiled)))

	print()

	index_for_pattern = input('Indíce: ')

	if not (index_for_pattern):

		print('No selecciono ningún patrón de la lista')
		sys.exit(1)

	try:

		index_for_pattern = int(index_for_pattern)

	except ValueError:

		print('El indíce debe ser numerico')
		sys.exit(1)

	else:

		if ('-' in str(index_for_pattern)):

			print('Warning: El indíce debe ser positivo')
			index_for_pattern = index_for_pattern*-1

		if not (index_for_pattern > len(patterns)-1):

			print('Abriendo en su navegador predeterminado...')
			webbrowser.open_new_tab(patterns[index_for_pattern][0])
			input()

		else:

			print('El indíce propuesto no existe...')
			sys.exit(1)
