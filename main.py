from pymisp import PyMISP

misp_url = 'Instance Misp'
misp_key = 'Cle Api'
misp_verifycert = True

misp = PyMISP(misp_url, misp_key, misp_verifycert)

def get_last_events():
    # Récupère les événements des dernières 24h
    events = misp.search(controller='events', last='24h')
    return events