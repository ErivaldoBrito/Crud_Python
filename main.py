# .txt
# Banco de Dados
# SQLite

# SQL
# Linguagem de Consulta Estruturada
 
# SELECT * FROM CLIENTES
# (se um usuário) - nome, sobrenome, idade

# ORM - Objeto de Mapeamento Racional - Biblioteca de formato de programação

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

# I/O
# I = Input (entrada)
# O = Out (saída)

# Cloud = Computação na nuvem.
# Para fechar o banco de dados usa-se """ session.close() """

# Criando Tabela.

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column ("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

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

print("Solicitando dads do usuário")
usuario = Usuario("Marta", "marta@gmail.com", "123")
session.add(usuario)
session.commit()

usuario = Usuario(nome="Maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

# listando todos os usuários do Banco de Dados.
print("\nExibindo todos usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

# Fechando conexão.
session.close()
