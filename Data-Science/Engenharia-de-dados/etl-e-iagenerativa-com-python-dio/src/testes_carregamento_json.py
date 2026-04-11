import pandas as pd

import json


df_csv = pd.read_csv('data/dados-para-etl-e-iagenerativa-com-python.csv')
#print(df_csv)


# Modo: 1
with open('data/dados-para-etl-e-iagenerativa-com-python.json', 'r', encoding='utf-8') as arquivo:
    data_json1 = json.load(arquivo)
print(data_json1)


# Modo: 2
with open('data/dados-para-etl-e-iagenerativa-com-python.json') as arquivo:
    data_json2 = json.load(arquivo)
print(data_json2)

df_json2 = pd.json_normalize(data_json2)
print(df_json2)


# Modo 3: pd.read_json
with open('data/dados-para-etl-e-iagenerativa-com-python.json') as arquivo:
    df_json3 = pd.read_json(arquivo)
print(df_json3)


# Modo 4: pd.DataFrame
with open('data/dados-para-etl-e-iagenerativa-com-python.json') as arquivo:
    df_json4 = pd.DataFrame(arquivo)
print(df_json4)


# Salvar json identado em arquivo
with open('json_identado.json', 'w') as arquivo:
    json.dump(dados_json, arquivo, indent=4)




