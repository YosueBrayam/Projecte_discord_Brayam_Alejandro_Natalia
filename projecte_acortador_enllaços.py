# Aquestes línies importen les llibreries necessàries. 
# discord.py és una llibreria per que interactui amb la API de Discord, i el 'sqlite3' es fa servir per a la conexió a la base de dades SQLite.
import discord
from discord.ext import commands
import sqlite3
import random
import string



# Aquesta línia crea una instància del bot de Discord i defineix el prefix dels comandaments com '!'.
# Significa que els membres del servidor han d'iniciar els seus comandaments amb '!' perquè el bot els reconegui.
bot = commands.Bot(command_prefix='!')



# Connexió a la base de dades SQLite.
# Aquestes línies es connecten a la base de dades SQLite (o la creen si no existeix) i creen un cursor que permet executar comandes SQL.
conn = sqlite3.connect('escurçador_urls.db')
cursor = conn.cursor()



# Creació de la taula si no existeix.
# Aquest fragment crea una taula a la base de dades per emmagatxemar les URL llargues i els seus codis curts.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        llarga TEXT NOT NULL,
        curta TEXT NOT NULL UNIQUE
    )
''')
conn.commit()



# Funció per generar un codi curt aleatori.
# Aquesta funció genera codi curt aleatori de 6 caràcters utilitzant lletres majúscules, minúscules i dígits.
def generar_codi_curt():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))



# Aquest és el comandament '!escorçar'. Quan s'executa aquest comandament, la URL llarga es comprova a la base de dades.
# Si ja existeix, es retorna el codi curt existent; si no, es genera un nou codi curt, s'afegeix a la base de dades i es retorna.
# Ruta per acortar una URL.
@bot.command()
async def escorçar(ctx, llarga):
    # Comprovar si la URL ja està a la base de dades.
    cursor.execute('SELECT curta FROM urls WHERE llarga = ?', (llarga,))
    resultat = cursor.fetchone()

    if resultat:
        # Si ja existeix, retornar el codi curt existent.
        codi_curt = resultat[0]
    else:
        # Si no existeix, generar un nou codi curt.
        codi_curt = generar_codi_curt()

        # Afegir a la base de dades.
        cursor.execute('INSERT INTO urls (llarga, curta) VALUES (?, ?)', (llarga, codi_curt))
        conn.commit()



# Aquest és el comandament '!redirigir'. Quan un usuari executa aquest comandament amb un codi curt, el bot de dades per a la URL llarga corresponent.
# Si existeix, redirigeix l'usuari; si no, envia un missatge d'error.
    await ctx.send(f'Codi Curt: {codi_curt}')

# Ruta per redirigir a la URL llarga.
@bot.command()
async def redirigir(ctx, codi_curt):
    cursor.execute('SELECT llarga FROM urls WHERE curta = ?', (codi_curt,))
    resultat = cursor.fetchone()

    if resultat:
        # Si el codi curt existeix, redirigir a la URL llarga.
        await ctx.send(f'Redirigint a: {resultat[0]}')
    else:
        # Si no existeix, retornar un missatge d'error.
        await ctx.send('URL no trobada')

# Iniciar el bot.
bot.run('TOKEN_DEL_BOT')
