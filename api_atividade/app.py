from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#    'Edson':'123'
#}

#@auth.verify_password
#def autenticacao(login,senha):
#    if not (login,senha):
#        return False
#    return USUARIOS.get(login)==senha

@auth.verify_password
def autenticacao(login,senha):
    if not (login,senha):
        return False
    return Usuarios.query.filter_by(login=login,senha=senha).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status':'Erro.',
                'mensagem':'Pessoas não encontrada.'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'pessoa [{}] excluída com sucesso.'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso','mensagem':mensagem}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':p.id,'nome':p.nome,'idade':p.idade} for p in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'],
                         idade=dados['idade'])
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

class ListaAtividades(Resource):
    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response = [{'Pessoa':a.pessoa.nome,'Atividade': a.id, 'nome': a.nome} for a in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'Atividade:': atividade.nome,
            'Id':atividade.id
        }
        return response


api.add_resource(Pessoa,'/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoa/')
api.add_resource(ListaAtividades,'/atividades/')

if __name__ == '__main__':
    app.run(debug=True)