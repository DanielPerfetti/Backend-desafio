import pymysql
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError

# Configurações do banco de dados
host = 'localhost'
user = 'root'  # Usuário do MySQL
password = '#Qq123456'  # Senha do MySQL para o usuário 'root'
db_name = 'empresa'  # Nome do banco de dados que será criado ou utilizado

# Conectando ao MySQL usando PyMySQL, sem especificar um banco de dados ainda
# Isso porque queremos criar o banco de dados se ele não existir
connection = pymysql.connect(host=host, user=user, password=password)

try:
    # Abrindo um cursor para executar comandos SQL
    with connection.cursor() as cursor:
        # Executa o comando para criar o banco de dados, se ele ainda não existir
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        print(f"Banco de dados '{db_name}' criado ou já existe.")
finally:
    # Fechando a conexão com o MySQL
    connection.close()

# Criando o engine usando SQLAlchemy para conectar ao banco de dados MySQL específico
# A string de conexão é formatada com o usuário, senha, host e nome do banco
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_name}")

try:
    # Estabelecendo uma conexão com o banco de dados 'empresa' através do engine
    with engine.connect() as connection:
        # Executando um comando SQL para criar a tabela 'pessoas' se ela ainda não existir
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INT AUTO_INCREMENT PRIMARY KEY,  # ID com incremento automático, chave primária
                nome_completo VARCHAR(100) NOT NULL,  # Nome completo, campo obrigatório
                data_nascimento DATE NOT NULL,  # Data de nascimento, campo obrigatório
                endereco VARCHAR(200),  # Endereço, campo opcional
                cpf VARCHAR(11) NOT NULL UNIQUE,  # CPF (11 dígitos), campo obrigatório e único
                estado_civil VARCHAR(20)  # Estado civil, campo opcional
            );
        """))
        # Se a tabela foi criada ou já existe, exibe a mensagem abaixo
        print("Tabela 'pessoas' criada ou já existe.")
except ProgrammingError as e:
    # Captura e trata erros de programação SQL, como problemas na sintaxe SQL
    print(f"Erro ao criar a tabela: {e}")