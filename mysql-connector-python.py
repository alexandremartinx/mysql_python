import mysql.connector
import pandas as pd
#execute no terminal o comando pip install mysql-connector-python e pip install pandas

""" conecta no banco de dados utilizando a lib importada
recebe o usuário, senha, nome banco, host e porta exposta """
def connect_db(user, password, db, host='host do banco', port='porta'):
    connection = False
    try:
        connection = mysql.connector.connect(host=host,
                                            port=port,
                                            database=db,
                                            user=user,
                                            passwd=password)
    except:
        pass
    #retorna o objeto da conexão com o banco
    return connection

#criação do cursor para a execução de query
def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    #se houver parâmetro, é passado junto com a query
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    
    return cursor.fetchall()

def main():
    connection = connect_db(user='usuario', password='senha', db='nome do banco', port='porta')
    if not connection:
        print("Error connecting to Database")
        exit(0)
    #query desejada
    query = '''
        SELECT
            *
        FROM
            vagas
    '''
    #comando no banco. Objeto da conexão + query desejada
    result = execute_query(connection, query)
    df = pd.DataFrame(result)
    print(df)

if __name__ == '__main__':
    main()