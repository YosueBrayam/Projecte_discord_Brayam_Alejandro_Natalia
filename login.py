
import requests

def login(nom, contrasenya):
    url = 'https://castelletsmxa.cat/app/login/?name=admin&pass=1234'

    params = {
        'name': nom,
        'pass': contrasenya
    }
    
    resp = requests.get(url=url, params=params, timeout=15)
    
    return resp.ok


    
usuari = input("digues el teu nom d'usuari \n")
contrasenya = input("digues la teva contrasenya \n")
try:
    resultat = login(usuari, contrasenya)
except:
    print('no s\'ha pogut iniciar sessio perque hi ha hagut un error en la connexio amb el servidor')
else:
    if resultat == True:
        print('Benvingut ', usuari)
    else:
        print('L\'usuari o la contrasenya no son correctes')


    
# resultat = previsio_del_temps()

# latitud = resultat['latitude']
# print(latitud)

# temperatura = resultat['hourly']['temperature_2m']
# print(temperatura)
