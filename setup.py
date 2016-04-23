#!/usr/bin/env python3
""" Setup - Programm
    Interview - nimmt Userdaten entgegen 
    generiert die Datenbank + Tabelle
    determiniert die wichtigen Verzeichnisse (template data, Arbeitsverzeichnis) und speichert sie für alle Programmteile, die darauf zugreifen müssen, lesbar ab -> muss was über os lernen!"""

import shelve
import sqlite3
# from os import system 
from userdata import new_user, check_user

# this list serves to ask the user for the data in an order they expect
order = ['Name','Straße Hausnummer','PLZ Ort','mobil','E-mail','www']
# dictionary with the user data: check here if there is already a dictionary shelve; if there is, open that; if there isn't, initialize this empty directory.
# if :
#     # open shelved dict
# else: 
#     user_data = {'Name':'','Straße Hausnummer':'','PLZ Ort':'','Telefon':'','mobil':'','E-mail':'','www':''}

def start():
    """ checks if userdata file already exists; if not, calls new_user; if userdata file exists, but 'Name' is empty, calls new_user as well """
    if user_data['Name'] == '': 
        new_user(order, user_data)
        check_user(order, user_data)
    else:
        print('Hello {}!'.format(user_data['Name']))
        edituser = input('Möchtest Du Deine Daten prüfen oder korrigieren? Bitte gib j für ja oder n für nein ein: ')
        if edituser == 'j':
            check_user(order, user_data)
        else:
            print('Hab\' einen schönen Tag!')

start()
# set_dirs()
# db_init()
