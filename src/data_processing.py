#Iremos fazer o pre-processamento dos dados e limpeza
import pandas as pd
import db_connection
from sklearn.preprocessing import LabelEncoder

df_credito = pd.read_csv("data/raw/public.CREDITO.csv", sep=";")
df_clientes = pd.read_csv("data/raw/public.CLIENTES.csv", sep=";")
df_emprego = pd.read_csv("data/raw/public.EMPREGO.csv", sep=";")
df_estadocivil = pd.read_csv("data/raw/public.ESTADOCIVIL.csv", sep=";")
df_fiador = pd.read_csv("data/raw/public.FIADOR.csv", sep=";")
df_habitacao = pd.read_csv("data/raw/public.HABITACAO.csv", sep=";")
df_historico_credito = pd.read_csv("data/raw/public.HISTORICO_CREDITO.csv", sep=";")
df_outrofinanciamento = pd.read_csv("data/raw/public.OUTROSFINANC.csv", sep=";")
df_profissao = pd.read_csv("data/raw/public.PROFISSAO.csv", sep=";")
df_proposito = pd.read_csv("data/raw/public.PROPOSITO.csv", sep=";")
df_investimentos = pd.read_csv("data/raw/public.INVESTIMENTOS.csv", sep=";")


#Verificando os primeiros arquivos
print(df_credito.head())
#verificando a quantidade de linhas e colunas
print(df_credito.shape)
print("\n")
#verificando a quantidade de dados nulos
print(df_credito.isnull().sum())
print("\n")
print("-*-"*20)
#Verificamos que Emprego, residenciaDesde e habitacao estão com dados nulos, vamos preencher pela moda que se encontra nessas colunas 
df_credito["Emprego"] = df_credito["Emprego"].fillna(df_credito["Emprego"].mode()[0])
df_credito["ResidenciaDesde"] = df_credito["ResidenciaDesde"].fillna(df_credito["ResidenciaDesde"].mode()[0])
df_credito["Habitacao"] = df_credito["Habitacao"].fillna(df_credito["Habitacao"].mode()[0])

#Depois de preencher os valores nulos das colunas, vamos verificar se ainda temos dados nulos
print(df_credito.isnull().sum())
print("\n")
#Agora vamos verificar se existem valores duplicados
print(f"Existem {df_credito.duplicated().sum()} valores duplicados na tabela de credito") 

#Agora iremos verificar se existem valores nulos nos outros arquivos.
print(df_clientes.isnull().sum())
print(df_emprego.isnull().sum())
print(df_estadocivil.isnull().sum())
print(df_fiador.isnull().sum())
print(df_habitacao.isnull().sum())
print(df_historico_credito.isnull().sum())
print(df_outrofinanciamento.isnull().sum())
print(df_profissao.isnull().sum())
print(df_proposito.isnull().sum())

print(df_emprego)
print("\n")
print(df_habitacao)
print("\n")
print(df_historico_credito)
print("\n")
print(df_clientes.shape)
print("\n")
print(df_investimentos)
"""Como foi verificado que na tabela de CREDITO existem dados em comum com as outras tabelas, os atributos das colunas das outras tabelas coensidem com os dados das 
outras tabelas e os valores também, por exemplo o IDEMPREGO da tabela de Emprego e o EMprego da tabela de CREDITO, vamos unir e explorar os dados nos notbooks 
exploracao_dados.
"""

#agora iremos salvar os dados processados para o data/processed
db_connection.save_data(df_credito, "data/processed/CREDITO.csv")
db_connection.save_data(df_clientes, "data/processed/CLIENTES.csv")
db_connection.save_data(df_emprego, "data/processed/EMPREGO.csv")
db_connection.save_data(df_estadocivil, "data/processed/ESTADOCIVIL.csv")
db_connection.save_data(df_fiador, "data/processed/FIADOR.csv")
db_connection.save_data(df_habitacao, "data/processed/HABITACAO.csv")
db_connection.save_data(df_historico_credito, "data/processed/HISTORICO_CREDITO.csv")
db_connection.save_data(df_outrofinanciamento, "data/processed/OUTROSFINANC.csv")
db_connection.save_data(df_profissao, "data/processed/PROFISSAO.csv")
db_connection.save_data(df_proposito, "data/processed/PROPOSITO.csv")
db_connection.save_data(df_investimentos, "data/processed/INVESTIMENTOS.csv")


