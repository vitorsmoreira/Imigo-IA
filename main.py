from senha import CHAVE_API
import requests
import json


headers = {
    'Authorization': f'Bearer {CHAVE_API}',
    'Content-Type': 'application/json'
}
link = 'https://api.openai.com/v1/chat/completions'
id_modelo = 'gpt-3.5-turbo'
sistema = (
    'Suponha que você seja um robô que atua num aplicativo de pós-compra'
)
body_mensagem = {}

mensagem_cliente = input(
    'Fale-me seu problema; caso não o tenha, digite \'n\'\n'
)

while mensagem_cliente != 'n':
    body_mensagem = {
        'model': id_modelo,
        'messages': [
            {'role': 'system', 'content': sistema},
            {'role': 'user', 'content': mensagem_cliente}
        ]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisicao.json()
    mensagem = resposta['choices'][0]['message']['content']
    print(mensagem)

    pergunta = input('Se deseja continuar o diálogo, digite \'sim\'.\n')

    if pergunta.lower() == 'sim':
        mensagem_cliente = input('-> ')
    else:
        break
