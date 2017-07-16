import json
EMAIL_DOMAIN = '@ui.ac.id'
ANGKATAN = {"2017": "2017", "2016": "omega", 
            "2015": "capung", "2014": "orion", 
            "2013--": "alumni"}

def get_angkatan_by_npm(npm):
    try:
        suffix = npm[:2]        # get first two digit of NPM
        angkatan = '20' + suffix
        
        return ANGKATAN[angkatan]

    except Exception as e:
        return ANGKATAN['2013--']

def get_role_by_angkatan(angkatan):
    try:
        if angkatan == 1:
            return 3
        else:
            return 2

    except Exception as e:
        return 0

def get_email_by_username(username):
    try:
        return username + EMAIL_DOMAIN
    except Exception as e:
        return username

def load_data(data_dir):
    try:
        with open(data_dir) as data_file:    
            data = json.load(data_file)
        return data
    except Exception as e:
        return {'allowed_org':[]}