import os
import requests

# Caminho da pasta onde estão os arquivos PDF
pdf_folder = r'C:\Users\willi\Desktop\leitorpdf\pdf'

# Lista todos os arquivos PDF na pasta
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Cria uma lista vazia para armazenar as respostas
responses = []

# Define o cabeçalho com a chave de API
headers = {
    'x-api-key': 'sec_Vf7VkWAYTeuBWL7FvsbVCeSeyowY6AGI'
}

# Loop para processar cada arquivo PDF
for pdf_file in pdf_files:
    # Constrói o caminho completo para o arquivo PDF
    pdf_path = os.path.join(pdf_folder, pdf_file)
    
    # Faz o upload do arquivo PDF para o ChatPDF via API
    files = [
        ('file', ('file', open(pdf_path, 'rb'), 'application/octet-stream'))
    ]
    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)
    
    # Verifica se o upload foi bem-sucedido
    if response.status_code == 200:
        # Obtém o ID da fonte do arquivo PDF carregado
        source_id = response.json()['sourceId']
        
        # Define a pergunta a ser feita
        question = "Quero palavras chaves com TERMOS COMPOSTOS, ou seja, duas palavras."
        
        # Envia a pergunta via API
        data = {
            'sourceId': source_id,
            'messages': [
                {
                    'role': 'user',
                    'content': question
                }
            ]
        }
        response = requests.post(
            'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)
        
        # Verifica se a pergunta foi enviada com sucesso
        if response.status_code == 200:
            # Obtém a resposta da API
            response_text = response.json()['content']
            # Adiciona a resposta à lista de respostas
            responses.append(response_text)
            print(f"Resposta para '{pdf_file}':", response_text)
            
            # Exclui o arquivo PDF do ChatPDF via API
            data = {
                'sources': [source_id]
            }
            response = requests.post(
                'https://api.chatpdf.com/v1/sources/delete', headers=headers, json=data)
            
            # Verifica se a exclusão foi bem-sucedida
            if response.status_code == 200:
                print(f"Arquivo PDF '{pdf_file}' excluído com sucesso")
            else:
                print(f"Erro ao excluir arquivo PDF '{pdf_file}':", response.text)
        else:
            print(f"Erro ao enviar pergunta para '{pdf_file}':", response.text)
    else:
        print(f"Erro ao fazer upload de '{pdf_file}':", response.text)

# Escreve as respostas em um arquivo de texto
with open('ListaDePalavras.txt', 'w', encoding='utf-8') as f:
    for response in responses:
        f.write(response + '\n')
