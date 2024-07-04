# mysql_python

# DB.py

Este script Python DB.py foi desenvolvido para facilitar a conexão e a execução de comandos SQL em um banco de dados MySQL. Ele oferece funcionalidades para:

Conectar ao Banco de Dados:
Utiliza o módulo mysql.connector para estabelecer uma conexão com o MySQL.
Você pode especificar o usuário, senha, host, porta e opcionalmente o nome do banco de dados.

Executar Comandos SQL de um Arquivo:
O método execute_sql_file permite a execução de comandos SQL contidos em um arquivo especificado. Cada comando é executado sequencialmente.

Exemplo de Uso (main function):
Na função main(), são definidos o usuário, senha, host, porta e o caminho do arquivo SQL (sql_file_path) que contém os comandos a serem executados.
O script conecta-se ao MySQL utilizando as credenciais fornecidas e executa os comandos SQL do arquivo especificado (create_table.sql neste exemplo).
Após a execução bem-sucedida dos comandos, a conexão é fechada.
Como Usar

Preparação:

Certifique-se de ter o módulo mysql-connector-python instalado. Caso contrário, instale utilizando pip install mysql-connector-python.
Configuração:

Edite o script para fornecer suas próprias credenciais MySQL (user, password, host e port) e o caminho do arquivo SQL que você deseja executar (sql_file_path).
Execução:

Execute o script DB.py. Ele se conectará ao seu banco de dados MySQL e executará os comandos SQL do arquivo especificado.

# mysql-connector-python.py

Este script Python utiliza as bibliotecas mysql.connector e pandas para conectar-se a um banco de dados MySQL e executar uma consulta SQL, transformando o resultado em um DataFrame do pandas para análise e manipulação de dados.

Conectar ao Banco de Dados:
A função connect_db estabelece uma conexão com o MySQL utilizando as credenciais fornecidas (user, password, db, host e port).

Executar Consultas SQL:
A função execute_query recebe uma conexão ativa com o banco de dados, uma consulta SQL (query) e opcionalmente parâmetros (params) para executar consultas parametrizadas.
Retorna os resultados da consulta como uma lista de tuplas.

Processamento de Dados com pandas:
Na função main(), o script conecta-se ao banco de dados utilizando as credenciais especificadas.
Executa uma consulta SQL simples para selecionar todos os registros da tabela vagas.
Transforma os resultados da consulta em um DataFrame do pandas (df) para análise posterior.

Instalação das Dependências:

Certifique-se de ter as bibliotecas mysql-connector-python e pandas instaladas. Você pode instalá-las via terminal usando:

pip install mysql-connector-python pandas

Configuração:
Edite o script para fornecer suas próprias credenciais MySQL (user, password, db, host e port) e a consulta SQL desejada (query).