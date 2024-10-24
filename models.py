from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import date

# String de conexão com o banco de dados MySQL.
# O formato é: "mysql+pymysql://<usuário>:<senha>@<host>/<nome_do_banco>"
# Altere as credenciais de acordo com o seu ambiente.
DATABASE_URL = "mysql+pymysql://root:#Qq123456@localhost/empresa"

# Criação do engine que conecta ao banco de dados.
# O 'engine' é a interface para comunicar-se com o banco de dados.
engine = create_engine(DATABASE_URL)

# Criação da fábrica de sessões para gerenciar as transações no banco de dados.
# As sessões são necessárias para fazer consultas, inserir dados e manipular o banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação da base declarativa. A partir desta classe, todas as tabelas serão definidas.
Base = declarative_base()

# Definição da classe 'Pessoa' que mapeia a tabela 'pessoas' no banco de dados.
# Esta classe herda de 'Base', e cada atributo dela é uma coluna na tabela.
class Pessoa(Base):
    __tablename__ = 'pessoas'  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, index=True)  # ID da pessoa, chave primária e indexada para melhorar desempenho nas consultas
    nome = Column(String(100), index=True)  # Nome completo da pessoa, com um índice para buscas rápidas
    data_nascimento = Column(Date)  # Data de nascimento da pessoa, armazenado como DATE no MySQL
    endereco = Column(String(255))  # Endereço da pessoa, até 255 caracteres
    cpf = Column(String(11), unique=True)  # CPF único, 11 caracteres e com restrição de unicidade (unique)
    estado_civil = Column(String(20))  # Estado civil da pessoa, até 20 caracteres (opcional)

# Modelos Pydantic para validação de dados na entrada e saída da API.

# Modelo Pydantic para criação de uma nova pessoa (dados que são esperados na requisição POST).
class PessoaCreate(BaseModel):
    nome: str  # Nome completo da pessoa
    data_nascimento: date  # Data de nascimento
    endereco: str  # Endereço
    cpf: str  # CPF (11 caracteres)
    estado_civil: str  # Estado civil (solteiro, casado, etc.)

    # Configuração para permitir a conversão de objetos ORM (SQLAlchemy) para objetos Pydantic.
    class Config:
        from_attributes = True  # Habilita o uso do modelo SQLAlchemy para conversão em resposta Pydantic

# Modelo Pydantic para retornar os dados da pessoa (na resposta das rotas GET, POST, PUT, etc.).
class PessoaResponse(BaseModel):
    id: int  # ID da pessoa
    nome: str  # Nome completo
    data_nascimento: date  # Data de nascimento
    endereco: str  # Endereço
    cpf: str  # CPF
    estado_civil: str  # Estado civil

    # Configuração para permitir a conversão de objetos ORM (SQLAlchemy) para objetos Pydantic.
    class Config:
        from_attributes = True  # Permite a conversão de objetos ORM para o modelo Pydantic

# Criação das tabelas no banco de dados. Se elas não existirem, serão criadas com base na definição de 'Pessoa'.
# Este comando garante que a estrutura da tabela seja criada no banco.
Base.metadata.create_all(bind=engine)