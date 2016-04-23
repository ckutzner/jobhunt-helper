""" Functions for user administration """

import shelve

userdata = {'Name (Vorname Nachname)':'','Straße Hausnummer':'','PLZ Ort':'','Telefon':'','mobil':'','E-mail':'','www':''}

def new_user(userd):
    """ enters new user data """
    for k in userd:
        userd[k] = input('Bitte gib Deine(n) {} ein und drücke ENTER: '.format(k))
    return userd
#    print(userd) # for test

def check_user(userd):
    """ go over user data, check them, if necessary, alter them """
    for k in userd:
        check = input('Ist {} noch Dein(e) korrekte(r) {}? j für ja/n für nein: '.format(userd[k], k))
        if check == 'n':
            userd[k] = input('Bitte gib den/die korrekte {} ein: '.format(k))
        else:
            print('OK')
    print('Hier sind die korrigierten Daten: ')
    for k in userd:
        print(k + ': ' + userd[k])
    return userd
