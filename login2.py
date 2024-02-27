# login.
import requests

def login(nom, contrasenya):
    url = 'https://castelletsmxa.cat/app/login/'

    params = {'name': nom, 'pass': contrasenya}
    resp = requests.get(url=url, params=params, timeout=10)

    return resp.ok

# Opcio de registre al menú.
opcio = input("Què vols fer? (1) Iniciar sessió, (2) Registrar-se: ")

if opcio == 2

def registrarse():
nom = input("Introdueix el teu nom d'usuari: ")
contrasenya = input("Introdueix la teva contrasenya: ")
correu = input("Introdueix el teu correu electrònic (opcional): ")

usuaris = []  # Llista per emmagatzemar usuaris.

usuari = {"nom": nom, "contrasenya": contrasenya, "correu": correu}
usuaris.append(usuari)

print("Registre completat. Inicia sessió per continuar.")

if login(usuari, contrasenya):
    print("Login correcte.")
else:
    print("El login ha fallat. Intenta-ho de nou")