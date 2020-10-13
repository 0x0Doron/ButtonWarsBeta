# Clase que controla el uso de los distintos
# avatares disponibles para el usuario
# Dependiendo de su 'score' tendrá acceso
# a más o menos avatares

import os

PWD = os.path.abspath(os.curdir)

avatars = os.listdir(PWD + r"/aplicacion/static/avatars")
avatars.remove("default_avatar.png")

# Los ficheros cuyo nombre empieza por '1...'
# son para rangos bajo


def splitAvatarName(avatar):
    dotIndex = avatar.find('.')
    name = avatar[1:dotIndex]

    return avatar, name


def getNoobAvatars():
    noobAvatars = []
    for avatar in avatars:
        if avatar.startswith('1'):
            noobAvatars.append(splitAvatarName(avatar))

    return noobAvatars


def getRangeAvatars(range):
    ''' Devolvemos una lista con tuplas(ruta, nombre)'''

    if range == "Novato":
        return getNoobAvatars()

#print(getRangeAvatars("Novato"))
