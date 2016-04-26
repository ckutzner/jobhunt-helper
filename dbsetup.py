""" module to set up the application database """

def dbsetup(dbname):
    """ initializes database with a table for application data; argument 'dbname' is provided by a variable in the program """
    db = sqlite3.connect(dbname)
    c = db.cursor()
    c.execute(CREATE TABLE applications (appl_id INTEGER PRIMARY KEY, jobname TEXT, source TEXT, company TEXT, recipient TEXT, recipient_address TEXT, street TEXT, zipcode TEXT, city TEXT, country TEXT, status TEXT, last_updated TEXT)) # recipient_address = gendered address if strictly necessary. I decided to keep zipcode and city as separate fields as the order and handling of zip code and city vary globally, so this should make i18n easier and allow extensions for international applications
    db.commit() # commit changes
    db.close() # close connection to database
