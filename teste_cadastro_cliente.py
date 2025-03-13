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
driver.get("file:///C:/Users/bruno/Documents/Teste_de_Sistema/templates/index.html")

# Preenche o campo Nome
nome_input = driver.find_element(By.ID, "name")
slow_typing(nome_input, "João da Silva", 0.1)  # Digita lentamente, com 0.1 segundos de intervalo

# Preenche o campo CPF
cpf_input = driver.find_element(By.ID, "cpf")
slow_typing(cpf_input, "12345678912", 0.1)

# Preenche o campo Endereço
endereco_input = driver.find_element(By.ID, "address")
slow_typing(endereco_input, "Rua das Flores, 123", 0.1)

# Preenche o campo Telefone
telefone_input = driver.find_element(By.ID, "phone")
slow_typing(telefone_input, "11987654321", 0.1)

# Clica no botão de Cadastrar
#submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#submit_button.click()

# Aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
time.sleep(20)

# Fecha o navegador
driver.quit()
