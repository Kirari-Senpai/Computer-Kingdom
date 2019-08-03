# -*- coding: utf-8 -*-
# Creador: Kirari
# Colaborador: DtxdF


# Reporte cualquier bug que encuentre en el programa y lo solucionaremos

# Disfrute de nuestro mini programilla ;)
# Se que les va a encantar

#####################################################
#                                                   #
# El conocimiento y el software debe ser compartido #
#                                                   #
#####################################################

import time as t
#from core.__configurations__ import *
from core.main import computer_kingdom_menu


if __name__ == '__main__':
	try:
		computer_kingdom_menu()
	except KeyboardInterrupt: 
		print(' [+] Vuelva pronto!')