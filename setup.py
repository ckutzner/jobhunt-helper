#!/usr/bin/env python3
""" Setup - Programm
    Interview - nimmt Userdaten entgegen 
    generiert die Datenbank + Tabelle
    determiniert die wichtigen Verzeichnisse (template data, Arbeitsverzeichnis) und speichert sie für alle Programmteile, die darauf zugreifen müssen, lesbar ab -> muss was über os lernen!"""

import shelve
import sqlite3
# from os import system 
from userdata import new_user, check_user
# from init_latex import letterheader # it's just 1 function; move it into this file?? 

# this list serves to ask the user for the data in an order they expect
order = ['Name','Straße Hausnummer','PLZ Ort','mobil','E-mail','www']
# generate shelve object that will be the userdata dictionary
user_data = shelve.open('userfile')

def dict_init():
    """ if 'Name' does not exist in user_data, loops over order and initializes all the values """
    if not 'Name' in user_data:
	for i in order:
            user_data[i] = ''

def start():
    """ if 'Name' is empty, calls new_user and then check_user, else goes to check_user if user wants"""
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

dict_init()
start()
# set_dirs()
# letterheader()

# close user_data shelve object
user_data.close()
# db_init()
