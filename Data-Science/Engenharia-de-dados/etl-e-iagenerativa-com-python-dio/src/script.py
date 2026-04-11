import pandas as pd

import json


df_csv = pd.read_csv('data/dados-para-etl-e-iagenerativa-com-python.csv')
#print(df_csv.head())


with open ('data/dados-para-etl-e-iagenerativa-com-python.json') as arquivo:
    dados_json = json.load(arquivo) 

df_json = pd.json_normalize(dados_json)
#print(df_json.head())



'''
###############
'''
print("##### ENTENDENDO OS DADOS #####")
print(f"DF csv -> {df_csv.shape}")
#print(df_csv.info())

print(f"DF json - > {df_json.shape}")
#print(df_json.info())


print(df_csv.columns)
#print(df_json.columns)

print("Valores nulos por coluna:")
#print(df_csv.isnull().sum())
#print(df_json.isnull().sum())


print("##### TRANSFORMANDO OS DADOS #####")
df_csv.columns = [col.lower() for col in df_csv.columns]
df_json.columns = [col.lower() for col in df_json.columns]


# Corrigir no número de colunas para os conjuntos de dados
df_csv_clean = df_csv.drop(columns=['id_account'])

colunas_interesse_json = ['id', 'name', 'account.number', 'account.agency', 'account.balance', 'account.limit']   
df_json_clean = df_json[colunas_interesse_json].copy() 


# Padronizar os nomes das colunas para os conjuntos de dados
df_columns = ['id', 'name', 'acc_number', 'agency', 'balance', 'limit']
df_csv_clean.columns = df_columns
df_json_clean.columns = df_columns

print("##### Resultado da Padornização Inicial dos Conjuntos de Dados #####")
print(df_csv_clean)
print(df_json_clean)


print("\n##### Junção realizada com merge(): pode ser utilizado em auditoria de daos #####")
df_unificado = pd.merge(df_csv_clean, df_json_clean, on=['id', 'name'], how='outer')
print(df_unificado)


print("\n##### Finalmente, consolidando os dados num só conjunto #####")
df_final = df_csv_clean.set_index('id').combine_first(df_json_clean.set_index('id')).reset_index()


print(df_final)


df_final['balance'] = df_final['balance'].fillna(0.0)
df_final['limit'] = df_final['limit'].fillna(0.0)


import numpy as np

df_final['agency'] = df_final['agency'].replace(r'^\s*$', np.nan, regex=True)
df_final['agency'] = df_final['agency'].fillna(0).astype(int).astype(str).str.zfill(4)

print("\n##### CONJUNTO DE DADOS FINAL TRANSFORMADO #####")
print(df_final)



print("\n##### FINALIZANDO O PROJETO ETL COM PYTHON #####")
# Criar backup final dos dados em arquivo CSV
df_final.to_csv('backup_clientes_final.csv', index=False, encoding='utf-8')

# Converter o DataFrame para uma string JSON para envio via HTTP
json_para_api = df_final.to_json(orient='records', indent=4)


print(json_para_api)



