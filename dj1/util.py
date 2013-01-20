# -*- coding: utf-8 -*-
import datetime
import pdb

MENU = {
	'HOME' : ('/', 'Accueil', None ),
	'TST' : ('/tst', 'Dev_Test', (( '/tst/cr', 'Nouveau Contact'), ('/tst', 'Liste'), ('/contact', 'Gcontact'), )),
	'FX' : ('/fx', 'FileXchange', (( '/fx/upload', 'Upload File(s)'), ('/fx/download', 'Download File(s)'), )),
	'LOGIN' : ('/cnx/login', 'Connexion', None),
	'LOGOUT' : ('/cnx/logout', 'Déconnexion', None),
	'ABOUT' : ('/about', 'A propos', (( '/about', 'A propos'),('/contact_us', 'Nous Contactez') )),
}

def get_pub_date():
	d = datetime.datetime.now()
	return d.strftime("%d/%m/%Y %X")

def set_menu( *liste ):
	r = []
	ALL_K = MENU.keys()
	for k in liste:
		if k in ALL_K:
			r.append(MENU[k])
	return r


if __name__ == '__main__':
	pdb.set_trace()
	print set_menu( 'HOME', 'TST', 'ABOUT', 'CONTACT_US' )
		
