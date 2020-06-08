# SkylineBOT

Aquest BOT programat en Python permet crear Skylines i manipular-los mitjançant un intèrpret. Projecte creat per l'assignatura LP de la Facultat d'Informàtica de Barcelona (UPC)

## Com funciona

### Prerequisits

1- Tenir Telegram instal·lat.

2- Instal·lar els prerequisits:

'''
pip3 install -r requirements.txt
'''

3- També és necessari un token proporcionat per Telegram per fer-lo funcionar:

- Anar al @BotFather.
- Utilitzar la comanda /newbot, i donar l'informació requerida.
- Crear un fitxer token.txt i guardar l'access token.
- Guardar l'adreça del bot.

### Execució

1-Descomprimir l'arxiu.

2-Dins la carpeta SkylineBOT, executar a la terminal:

'''
python3 bot.py
'''

Un cop fet això el bot ja està funcionant.

### Instruccions

#### Comandes
/start: Rebràs una salutació del bot.
/author: Informació sobre el creador del bot.
/lst: Llistat dels identificadors definits a la sessió actual i la seva corresponent àrea.
/clean: Esborra tots els identificadors definits a la sessió actual.
/save id: Guarda el Skyline definit per l'identificador id per a poder recuperar-lo a la pròxima sessió.
/load id: Carrega el Skyline definit per l'identificador id, i l'esborra dels guardats.

#### Llenguatge

Permet crear edificis de tres maneres:
- Simple: (xmin,alçada,xmax) on xmin i xmax són les posicions inicials i finals de l'edifici, i alçada l'alçada.
- Compostos: [(xmin,alçada,xmax),...] on es poden encadenar n edificis simples.
- Aleatoris: {n,h,w,xmin,xmax} on n és el nombre d'edificis generats, h l'alçada màxima, w l'amplada màxima, i xmin i xmax l'intèrval de posicions a on es poden generar els edificis.

Es permeten les següents operacions:
- skyline + slyline: unió.
- skyline * skyline: intersecció.
- skyline * N: replicació N vegades del skyline.
- skyline + N: desplaçament a la dreta de l'skyline N posicions.
- skyline - N: desplaçament a l'esquerre de l'skyline N posicions.
- (- skyline): skyline reflectit.

Es permet assignar skylines a variables utilitzant l'operador :=.

'''
id := (1,2,3)
'''

L'id pot ser una combinació de números i lletres, començant necessàriament per una lletra. Un cop un skyline està assignat a un identificador, ja pot ser utilitzat per operar amb ell.

### Explicacions i observacions

He decidit que quan tens un Skyline guardat amb el /save, s'esborri un cop el descarregues amb el /load, donat que únicament amb les comandes que ha de tenir aquest bot, no seria possible eliminar-los, solament sobreescriure'ls.

Al generador d'edificis aleatoris fica que les alçades dels edificis han d'estar entre 0 i h, ho he implementat literalment, el que vol dir que a vegades es generen edificis sense volum, els quals són eliminats immediatament.