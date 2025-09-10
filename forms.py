from flask_wtf import FlaskForm
from wtforms import (
     StringField,
     IntegerField,
     BooleanField,
     PasswordField,
     TextAreaField,
     SubmitField
)

class CamposForm(FlaskForm):
    nome = StringField(
        label='Nome completo',
        default='fulano da silva'
    )

    idade =  IntegerField(
        label='Sua idade',
        default=18,
        render_kw={
            'min':14,
            'max':120,
            'tyte': 'number',
        }
    )

    aceita_termos = BooleanField(
        label='Aceita os termos de uso',
        default=True,
    )

    senha = PasswordField(
        label='Senha',
    )

    comentario = TextAreaField(
        label='Comentario',
        render_kw= {
            'rows': 5,
            'cols': 50,
            'placeholder': 'Deixe seu comentario'
        }
    )

    enviar = SubmitField(
        label='Enviar'
    )