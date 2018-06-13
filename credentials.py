import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('./config.rc')
    credentials = {
        'db_user':config['Credentials']['username'],
        'db_pass':config['Credentials']['password'],
    }
    return credentials
