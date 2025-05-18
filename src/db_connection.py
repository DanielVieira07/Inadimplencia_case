#Conexão com ao Banco de dados PostegreSQL via psycopg2
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

#conectando com o banco de dados
def conecct_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print(e)


#Criando Dataframe
def creat_df(registros, columns):
    df = pd.DataFrame(registros, columns=columns)
    return df

#Salvando o dataframe e convertendo para csv
def save_data(df: pd.DataFrame, table_name: str):
    df.to_csv(table_name, sep=';', index=False)


if __name__ == "__main__":
    tabelas_list = [
        'public."CLIENTES"', 
        'public."CREDITO"', 
        'public."EMPREGO"',
        'public."ESTADOCIVIL"',
        'public."FIADOR"',
        'public."HABITACAO"',
        'public."HISTORICO_CREDITO"',
        'public."INVESTIMENTOS"',
        'public."OUTROSFINANC"',
        'public."PROFISSAO"',
        'public."PROPOSITO"'
    ]
    
    conexao = conecct_db()
    if conexao:
        try:
            cursor = conexao.cursor()
            for tabela in tabelas_list:
                try:
                    #consultando a tabela
                    cursor.execute(f"SELECT * FROM {tabela}")

                    #obtendo todos os dados
                    registros = cursor.fetchall()

                    #obtendo as colunas
                    columns = [desc[0] for desc in cursor.description]

                    df = creat_df(registros, columns)
                    nome_arquivo = tabela.split(' . ')[-1].replace('"', '') + ".csv"
                    save_data(df, f"./data/{nome_arquivo}")
                except Exception as e:
                    print(e)
        finally:
            cursor.close()
            conexao.close()
   