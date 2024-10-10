

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

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column ("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

 # DEFININDO ATRIBUTOS DA CLASSE   

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# primary_key = Chave primária. Chaves candidatas.
# autoincrement = 

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no Banco de Dados "commit = Salvar"
os.system("cls || clear")

# CREATE.
print("Solicitando dados do usuário")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")

usuario = Usuario(nome="Maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()