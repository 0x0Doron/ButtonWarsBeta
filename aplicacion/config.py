#   Configuración de:
#   - la base de datos
#   - Secret keys
#   - ...

import os


SECRET_KEY = 'A4Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)  # Prompt working directory (para almacenar el fichero 'db' dentro de aplicacion)

DEBUG = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False # Funcionalidad que de la qie prescindimos para evitar cargas lentas.
