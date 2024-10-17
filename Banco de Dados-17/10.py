
import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
# Criando banco de Dados.

MEU_BANCO = create_engine("sqlite:///meubanco.db")

# ORM
# CREATE DATABASE meubanco;

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando Tabela.

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"

    self = Column ("self", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)
    telefone = Column("telefone", Integer)

    # DEFININDO ATRIBUTOS DA CLASSE   

    def __init__(self, nome: str, idade: int, cpf: int, setor: str, funcao: str, salario: int, telefone: int,):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

# primary_key = Chave primária. Chaves candidatas.
# autoincrement = 

#Exemplo:

def criar_funcionario(nome, idade, cpf, setor, funcao, salario, telefone, novo_funcionario = Funcionario(
        nome=nome, idade=idade, cpf=cpf, setor=setor, funcao=funcao
)
session.add(novo_funcionario)
session.commit()

def listar_todos_funcionararios():
    funcionarios = session.query(Funcionario).all()
    for func in funcionarios:
        print(func)

def salvar_funcionario():
#   pass

#   pass
def atualizar_funcionario(funcionario):
#   pass
def excluir_funcionario(funcionario):
#   pass 

# TECNOLOGIAS
""" 
  - ORM: SQLAlchemy
  - Banco de Dados: SQLite
  - Versionamento: Git
"""


# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no Banco de Dados "commit = Salvar"
os.system("cls || clear")

# CREATE.
print("Solicitando dados do usuário")
inserir_nome = input("Digite seu Nome: ")
inserir_idade = input("Digite sua Idade: ")
inserir_cpf = input("Digite seu CPF: ")
inserir_setor = input("Digite seu Setor: ")
inserir_funcao = input("Digite sua Função: ")
inserir_salario = input("Digite seu salário: ")
inserir_telefone = input("Digite seu Telefone: ")

usuario = Funcionario(nome="Maria", idade="457", cpf="456.212.332-23", setor="Mecanico", funcao="Técnico Mecânica", salario="3.456,45", telefone="71-999254458" )
session.add(usuario)
session.commit()

# listando todos os usuários do Banco de Dados.
print("\nExibindo todos usuários do banco de dados.")
lista_usuarios = session.query(Funcionario).all()

for usuario in lista_usuarios:
    print(f"{usuario.nome} - {usuario.idade} - {usuario.cpf} - {usuario.setor} - {usuario.funcao} - {usuario.salario} - {usuario.telefone}")

# Fechando conexão.
session.close()

# Resultado esperado:
# Um sistema onde o usuário veja um menu e escolher dentre as opções disponíveis.

print(
"""      === RH System ===

    1 - Adicionar funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário
    5 - Listar todos os funcionários
    0 - Sair do sistema.
""")
