from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# String de conexão com o banco de dados MySQL
# Formato: "mysql+pymysql://<usuário>:<senha>@<host>/<nome_do_banco>"

DATABASE_URL = "mysql+pymysql://root:#Qq123456@localhost/empresa" #renomear com seu
# Criação do 'engine' que gerencia a comunicação com o banco de dados
# O 'engine' é responsável por abrir a conexão com o banco de dados e
# executar as instruções SQL
engine = create_engine(DATABASE_URL)
# Criação de uma fábrica de sessões (SessionLocal) para gerenciar as transações
# autocommit=False: As transações não serão automaticamente confirmadas no banco
# autoflush=False: A sessão não será automaticamente sincronizada com o banco até o commit
# bind=engine: Associa essa sessão ao 'engine', que contém a conexão com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Classe Base que será herdada por todas as classes de modelos
# A 'Base' é usada para declarar as tabelas no banco de dados
# Todas as classes de modelos do SQLAlchemy devem herdar desta classe
Base = declarative_base()
