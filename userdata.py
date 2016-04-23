""" Module with functions for user administration """

def new_user(order, data):
    """ 
    enters new user data in a dictionary; 
    arguments: list that determines order of elements; dictionary that stores user data 
    """
    for k in order:
        data[k] = input('Bitte gib Dein(en) {} ein und drücke ENTER: '.format(k))
    print('Hier sind Deine Daten: ')
    for k in order:
        print(k + ': ' + data[k])
    check_again = input('Ist alles korrekt? j für ja/n für nein: ')
    if check_again == 'n':
        check_user(order, data)
    return data

def check_user(order, data):
    """ 
    go over user data, check them, if necessary, alter them; 
    arguments: list that determines order of elements; dictionary that stores user data
    """
    for k in order:
        check = input('Ist {} noch Dein(e) korrekte(r) {}? j für ja/n für nein: '.format(data[k], k))
        if check == 'n':
            data[k] = input('Bitte gib den/die korrekte {} ein: '.format(k))
        else:
            print('OK')
    print('Hier sind die korrigierten Daten: ')
    for k in order:
        print(k + ': ' + data[k])
    check_again = input('Ist jetzt alles korrekt? j für ja/n für nein: ')
    if check_again == 'n':
        check_user(order, data)
    else:
        print('OK, super!')
    return data
