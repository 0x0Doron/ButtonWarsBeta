from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, TextAreaField, SelectField
from wtforms.validators import Required, InputRequired


class formLogin(FlaskForm):
    username = StringField("Nombre Usuario", validators=[Required()])
    password = PasswordField("Contraseña", validators=[Required()])
    submit = SubmitField("Entrar")


class formRegister(FlaskForm):
    username = StringField("Nombre Usuario:", validators=[Required()])
    password = PasswordField("Contraseña:", validators=[Required()])
    warcry = StringField("Grito de guerra:")
    descripcion = TextAreaField("Cuentanos algo sobre ti...")
    avatar = SelectField("Avatar:", coerce=str)
    submit = SubmitField("Registrarme")


class formEnsureDelete(FlaskForm):
    ''' Capa de seguridad para evitar borrados accidentales '''
    yes = SubmitField("Si")
    no = SubmitField("No")
