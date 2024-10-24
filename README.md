# Backend-desafio
Este projeto implementa uma API RESTful para gerenciamento de pessoas utilizando FastAPI, SQLAlchemy e MySQL. A aplicação permite realizar operações de CRUD (Create, Read, Update, Delete) em uma tabela de pessoas, armazenando informações como nome completo, data de nascimento, endereço, CPF e estado civil.

## Pré-requisitos

- Python 3.13
- MySQL

## Instalação

1. Clone este repositório.
2. Criar um ambiente virtual
   ```bash
   py -m venv venv
3. Instale as dependências:
   ```bash
   pip install fastapi[all] sqlalchemy pymysql  cryptography
## Execução
1. Ativar o ambiente virtual
   ```bash
   venv\Scripts\activate

 2. Executar o programa
    ```bash
    uvicorn main:app --reload
 3. Abrir no navegador
    ```bash
    http://127.0.0.1:8000/docs
     
## NÃO ESQUEÇA DE ALTERAR SEUS DADOS MYSQL COMO NOME <SENHA> E NOME DO DB

