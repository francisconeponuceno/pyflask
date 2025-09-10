<<<<<<< HEAD
from flask import Flask, redirect, render_template,request
from config import Config
from extenssions import toolbar, csrf
from forms import CamposForm
=======
# pip install flask-debugtoolbar
from flask import Flask, abort
from config import Config
import errors
from extensions import toolbar
>>>>>>> 9d5ee9a48893bea55668029a91f3e3f729f3f050

def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)
<<<<<<< HEAD
    
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
=======
>>>>>>> 9d5ee9a48893bea55668029a91f3e3f729f3f050

    if app.debug:
        toolbar.init_app(app)

    errors.init_app(app)
    
    @app.route('/')
    def index():
        return '''
            <body>
                <h1>Olá Mundo!</h1> 
            </body>
        '''


    @app.route('/erro')
    def error_page():
        abort(code=500)
        return 'Bem dindo'
    
    
    return app