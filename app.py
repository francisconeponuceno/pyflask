from flask import Flask, redirect, render_template,request
from config import Config
from extenssions import toolbar, csrf
from forms import CamposForm

def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)
    
    if app.debug:
        toolbar.init_app(app)

    csrf.init_app(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = CamposForm()
        dados = {}

        if request.method == 'POST':
            dados = {
                'nome': form.nome.data,
                'idade': form.idade.data,
                'aceita_termos': form.aceita_termos.data,
                'senha': form.senha.data,
                'Comentario': form.comentario.data,
            }

        return render_template(
            template_name_or_list='index.html',
            form = form,
            dados=dados,
        )

    # Extenção
    return app