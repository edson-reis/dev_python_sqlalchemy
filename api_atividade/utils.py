from models import Pessoas, Usuarios

# insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Elias', idade=49)
    pessoa.save()
    print(pessoa)

# consulta dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Edson')
    for p in pessoa:
        print(p)
    #pessoa = Pessoas.query.filter_by(nome='Edson').first()
    #print(pessoa.idade)

# altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Edson').first()
    pessoa.idade = 50
    pessoa.save()

# exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Elias').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    insere_usuario('Edson','123')
    consulta_usuarios()