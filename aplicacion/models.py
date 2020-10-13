# Por ahora solo hay una unica tabla
# TODO crear modelo de equipos, amigos, clanes, ...

from sqlalchemy import Column, Integer, String, Text, Boolean
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuarios(db.Model):
    '''Campos del modelo usuario'''
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password_hash = Column(String(128), nullable=False)
    avatar = Column(String(255), default="default_avatar.png")
    descripcion = Column(String(255), default="Le da miedo expresar sus emociones")
    warcry = Column(String(255))
    score = Column(Integer, default=0)
    range = Column(String(100), default="Novato")
    admin = Column(Boolean, default=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

    @property
    def password(self): # @property de password es getPassword()
        return AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # Lo usaremos en el login del usuario
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Controladores Flask Login
    # Esto depende de nuestra 'db' y modelo de datos

    def is_authenticated(self):
        return True

    def is_active(self):
        '''Al no haber un campo para indicar si
            un usuario está activo, siempre esta activo'''
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_admin(self):
        return self.admin
