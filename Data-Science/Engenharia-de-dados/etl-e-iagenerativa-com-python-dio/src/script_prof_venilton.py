import pandas as pd
import requests

import json


'''
############## EXTRACT ################
'''
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.ap


df = pd.read_csv('SDW2023.csv')

user_ids = df['UserID'].tolist()
print(user_ids)


def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users
    return response.json() if response.status_code ==



users = [user for id in user_ids if (user := get_user

print(json.dumps(users, indent=2))



'''
############## TRANSFORM ################


- OpenAI
Documentação Oficial da API OpenAI: https://platform.
 Informações sobre o Período Gratuito: https://help.o

Para gerar uma API Key:
    1. Crie uma conta na OpenAI
    2. Acesse a seção "API Keys"
    3. Clique em "Create API Key"

Link direto: https://platform.openai.com/account/api-
'''

import openai

# Substitua o texto TODO por sua API Key da OpenAI, e
openai_api_key = 'TODO'

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gp5-4",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {
            }
        ]
    )
    # Observar que a resposta do Chat é em JSON, port
    # acessar a chave 'Content', presente em 'choices
    # primeiro valor, lembrando de retirar as aspas d
    return completion.choices[0].message.content.stri


for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.
        "description": news
    })



'''
############## LOAD ################
'''
def update_userdata(user):
    response = requests.put(f"{sdw2023_api_url}/users
    return True if response.status_code == 200 else F


for user in users:
    sucess = update_user(user)
    print(f"User {user['name']} updated? {sucess}!")







