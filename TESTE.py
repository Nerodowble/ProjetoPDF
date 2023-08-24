from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import tempfile
import shutil

# Caminho da pasta onde estão os arquivos PDF
pdf_folder = r'C:\Users\willi\Desktop\leitorpdf\pdf'

# Lista todos os arquivos PDF na pasta
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Cria uma lista vazia para armazenar as respostas
responses = []

# Loop para processar cada arquivo PDF
for pdf_file in pdf_files:
    # Cria um diretório temporário para armazenar o perfil do navegador
    profile_dir = tempfile.mkdtemp()
    
    # Configuração para usar um perfil de navegador temporário (anônimo)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--user-data-dir={profile_dir}')
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)
    
    # Abre o site
    driver.get("https://www.chatpdf.com/")
    
    # Espera um pouco para garantir que a página tenha carregado
    time.sleep(4)
    
    # Clica no botão para abrir a janela de upload
    upload_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div/div[1]/div")
    upload_button.click()
    
    # Espera um pouco para a janela de upload abrir
    time.sleep(4)
    
    # Constrói o caminho completo para o arquivo PDF
    pdf_path = os.path.join(pdf_folder, pdf_file)
    
    # Digita o caminho completo do arquivo PDF
    upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    upload_input.send_keys(pdf_path)

    # Espera um pouco para a próxima página carregar
    time.sleep(10)
    
    # Digita a pergunta no campo de pergunta
    try:
        # Tenta encontrar o elemento usando o primeiro seletor
        question_input = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div[3]/div/textarea")
    except NoSuchElementException:
        # Se o primeiro seletor falhar, tenta encontrar o elemento usando um seletor diferente
        question_input = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Write your question...']")
    question_input.click()
    question_input.send_keys("Quero palavras chaves com TERMOS COMPOSTOS, ou seja, duas palavras.")
    time.sleep(3)
    
    # Clica no botão para enviar a pergunta
    enter_input = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div[3]/div/button")
    enter_input.click()
    
    # Espera um pouco para a resposta
    time.sleep(10)
    
    # Captura a resposta (lembre-se de que a resposta é dinâmica, então isso pode precisar ser ajustado)
    response = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div[2]/div/div/div/div/ul/div[3]").text
    print(f"Resposta para '{pdf_file}':", response)
    
    # Adiciona a resposta à lista
    responses.append(response)
    
    # Fecha a janela
    driver.quit()
    
    # Limpa o diretório temporário do perfil do navegador
    shutil.rmtree(profile_dir)

# Escreve as respostas em um arquivo de texto
with open('ListaDePalavras.txt', 'w', encoding='utf-8') as f:
    for response in responses:
        f.write(response + '\n')
