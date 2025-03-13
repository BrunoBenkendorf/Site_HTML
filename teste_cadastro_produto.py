from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Função para digitar com atraso
def slow_typing(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)  # Espera entre os caracteres

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com o protocolo file://
# Certifique-se de que o caminho está apontando para um arquivo HTML específico
driver.get("file:///C:/Users/bruno/Documents/Teste_de_Sistema/templates/produto.html")

cod_input = driver.find_element(By.ID, "cod")
slow_typing(cod_input, "111", 0.1)

nome_input = driver.find_element(By.ID, "name")
slow_typing(nome_input, "Sabão", 0.1) 

cat_input = driver.find_element(By.ID, "categoria")
slow_typing(cat_input, "Limpeza", 0.1)

valor_input = driver.find_element(By.ID, "value")
slow_typing(valor_input, "10", 0.1)

qtd_input = driver.find_element(By.ID, "qtd")
slow_typing(qtd_input, "50", 0.1)

desc_input = driver.find_element(By.ID, "descricao")
slow_typing(desc_input, "usado pra lavar roupa", 0.1)

fornecedor_input = driver.find_element(By.ID, "fornecedor")
slow_typing(fornecedor_input, "Limpa Tudo", 0.1)

#Falta terminar...
# Clica no botão de Cadastrar
#submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#submit_button.click()

# Aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
time.sleep(20)

# Fecha o navegador
driver.quit()