"""Programa/Aplicação principal.

Função jsonify transforma o json em string para ser enviada.
"""

from flask import Flask, request, jsonify
from data import alchemy
from model import show, episode

# É o nome do programa (análogo ao .self das classes).
# Instancia o Flask
app = Flask(__name__)

# string de conexão com BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# ficar conferindo se houve modificações e colocando isso na sessão (false)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# propagar as exceções de Banco para o SqlAlchemy
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'supersecreto'


# no primeiro request da API quero deixar o Banco pronto
@app.before_first_request
def create_table():
    """Cria todas as tabelas."""
    alchemy.create_all()


# criar uma rota/endpoint para raiz utilizando método GET
# utilizando a função abaixo
@app.route('/', methods=['GET'])
def home():
    """Função executada quando aplico o Get na rota da raiz."""
    return 'API Funcionando', 200


# incluir um recurso no Banco
# incluindo o recurso show e a qual método ele vai responder
@app.route('/show', methods=['POST'])
def create_show():
    """Cria um novo show/série com dados recebidos (post)."""
    # obtém json
    request_data = request.get_json()
    # cria novo show dos dados obtidos
    new_show = show.ShowModel(request_data['name'])
    new_show.save_to_db()
    # entender porque utilizar o find_by_id
    print(new_show.id)
    result = show.ShowModel.find_by_id(new_show.id)
    return jsonify(result.json())


# buscar os dados de show (GET)
# vou receber como parâmetro um name
# como rota na api será "servidor/show/nome_show_encontrar"
# se não especificar o método ele utiliza o GET
@app.route('/show/<string:name>')
def get_show(name):
    """Obtém uma série especificada pelo name.

    O parâmetro que entra na função é a mesma de /<string:name>.
    """
    result = show.ShowModel.find_by_name(name)
    if result:
        return result.json()
    return {'message': 'Série não encontrada'}, 404


# inserir episódio (POST)
@app.route('/show/<string:name>/episode', methods=['POST'])
def create_episode_in_show(name):
    """Adiciona um episódio a sua respectiva série."""
    request_data = request.get_json()
    # procura quem é o pai (série)
    parent = show.ShowModel.find_by_name(name)
    if parent:
        new_episode = episode.EpisodeModel(name=request_data['name'],
                                           season=request_data['season'],
                                           show_id=parent.id)
        new_episode.save_to_db()
        return new_episode.json()
    else:
        return {'message': 'Série não encontrada'}, 404


# deletar uma série
@app.route('/show/<int:id>', methods=['DELETE'])
def delete_show(id):
    """Deleta um série pelo ID."""
    # carrega a série para ser deletada
    show_deleted = show.ShowModel.find_by_id(id)
    show_deleted.delete_from_db()
    return {'message': 'Excluído com sucesso'}, 202


# rodar/executar aplicação Flask
# debug=True em ambiente de teste, em produção debug=False
# port=5000 é a porta padrão (editável)
if __name__ == '__main__':
    # preciso inicializar o Alchemy nessa App em especial
    # feito quando inicia a aplicação
    alchemy.init_app(app)
    app.run(port=5000, debug=True)
