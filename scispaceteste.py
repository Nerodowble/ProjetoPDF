from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicialização do driver do Chrome (certifique-se de que o chromedriver esteja no PATH)
driver = webdriver.Chrome()

# Abre o site
driver.get("https://typeset.io/")

# Espera um pouco para garantir que a página tenha carregado
time.sleep(3)

#Encontra botão de login
login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div/nav/div/button[1]")
login_btn.click()

time.sleep(2)

# Preenche o campo de login
login_input = driver.find_element(By.XPATH, "//*[(@id = 'mui-2')]")
login_input.send_keys("willianvidallima@outlook.com")

# Preenche o campo de senha
password_input = driver.find_element(By.XPATH, "//*[(@id = 'mui-3')]")
password_input.send_keys("1234567890")

# Clica no botão "Entrar"
login_button = driver.find_element(By.CLASS_NAME, "MuiButton-containedSecondary")
login_button.click()

# Aguarda o login ser concluído (você pode ajustar o tempo conforme necessário)
time.sleep(6)

library_btn = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div/nav/div/a/button")
library_btn.click()

time.sleep(10)

pdfs = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div[2]/section/div[2]/ul/div/li[1]/div[2]/p[1]")
pdfs.click()

time.sleep(10)

btn_close = driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div/div[1]/div[2]/button[1]")
btn_close.click()

#/html/body/div[1]/main/div/span/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/textarea[1]

time.sleep(10)

caixa_de_pergunta = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/span/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/textarea[1]")
caixa_de_pergunta.send_keys("Quero palavras chaves com TERMOS COMPOSTOS, ou seja, duas palavras.")
time.sleep(3)
btn_prosseguir = driver.find_element(By.CSS_SELECTOR, "button > .svg-inline--fa.fa-paper-plane-top.text-15.text-white")
btn_prosseguir.click()

time.sleep(3)

wait = WebDriverWait(driver, 15)  # Aguardar até 10 segundos no máximo
text_gpt_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/span/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]")))

# Capturar e imprimir o texto
text_gpt_text = text_gpt_element.text
print(text_gpt_text)

time.sleep(5)


# Fecha o navegador
driver.quit()
