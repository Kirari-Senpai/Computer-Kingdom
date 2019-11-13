import sys
import core.config.banners as banners

from os.path import splitext, basename
from ..config.clrscr import clrscr

try:
    import requests
    import webbrowser
    from tabulate import tabulate
    from bs4 import BeautifulSoup as bs4
except ImportError as error:
	print(" [x] Error: ", error)
	sys.exit()


def search_by_letter():

	abc = [chr(ord('a')+x) for x in range(0, 25)]

	user_agent = 'Lynx/2.8.9rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/3.6.5'

	for _ in abc:
		print(" [*] - %s" % (_))

	print('\n')

	letter = input(' CPK (indice) > ').lower()

	while (letter!='back'):
		if(letter!=''):
			glosario = {}
			tabla = [['Palabras','Mas informacion']]

			data = requests.get("http://www.alegsa.com.ar/Dic/%s.htm" % (letter), headers={'User-Agent':user_agent})
			html = bs4(data.content, 'lxml')

			for _ in html.body.find_all('a'):
				if ('Definicion de ' in _.text):
					base = splitext(basename(_['href']))[0]
					link = _['href']
					tabla.append([base,link])
					glosario[base] = link

			print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))


			word = input(' CPK (palabra) > ').lower()

			while (word!='back'):

				if(word!=''):

					try:
						url = glosario[word]

						data = requests.get(url, headers={'User-Agent':user_agent})
						html = bs4(data.content, 'lxml')

						definition = (html.find("div", {"id": "HOTWordsTxt"}).getText())

						if('Relacionado:' in definition):
							suprimir = definition.index('Relacionado:')
							definition = definition[:suprimir]

						d = []

						for i in range(len(definition)):
							for j in range(len(abc)):
								definition = (definition.replace('\n','')).replace("."+abc[j].upper(),'. '+abc[j].upper())

						definition = (definition).split(' ')


						clrscr()
						print(banners.brainBanner)


						aux = len(definition)

						oraciones = []

						while(aux!=0):
							oraciones.append(definition[:15])
							definition = definition[15:]
							aux = len(definition)


						print('[+] Definicion de ' + word + ':\n')

						for oracion in oraciones:
							print(' '.join(oracion))


						print('\n')

					except KeyError:
						print("\n [x] La palabra buscada no se encuentra en esta seccion o no existe.\n")

				word = input(' CPK (palabra) > ').lower()
				
		letter = input(' CPK (indice) > ').lower()
