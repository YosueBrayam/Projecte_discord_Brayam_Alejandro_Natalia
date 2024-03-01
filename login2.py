import requests

def login(nom, contrasenya):
    url = 'https://castelletsmxa.cat/app/login/'
    params = {'name': nom, 'pass': contrasenya}
    
    try:
        resp = requests.get(url=url, params=params, timeout=10)
        resp.raise_for_status()  # Llença una excepció si hi ha un error en la sol·licitud
        return resp.ok
    except requests.exceptions.RequestException as e:
        print("Error en la sol·licitud:", e)
        return False

def registrar(nom, contrasenya):
    url = 'https://castelletsmxa.cat/app/register/'
    dades_registre = {'name': nom, 'pass': contrasenya}
    
    try:
        resp = requests.post(url=url, json=dades_registre, timeout=10)
        resp.raise_for_status()  # Llença una excepció si hi ha un error en la sol·licitud
        if resp.ok:
            print("T'has registrat amb èxit!")
        else:
            print("Error en el registre.")
    except requests.exceptions.RequestException as e:
        print("Error en la sol·licitud:", e)

# Opció del menú
opcio = input("Què vols fer? (1) Iniciar sessió, (2) Registrar-se: ")

if opcio == '1':
    # Iniciar sessió
    nom = input("Introdueix el teu nom d'usuari: ")
    contrasenya = input("Introdueix la teva contrasenya: ")
    if login(nom, contrasenya):
        print("Has iniciat sessió amb èxit!")
    else:
        print("Error en iniciar sessió. Comprova les credencials.")
elif opcio == '2':
    # Registrar-se
    nom = input("Introdueix el teu nom d'usuari per al registre: ")
    contrasenya = input("Introdueix la contrasenya per al registre: ")
    registrar(nom, contrasenya)
else:
    print("Opció no vàlida.")