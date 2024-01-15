from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib

mensagem = 'Olá, tudo bem?'
tels = ['31912345678', '31987654321']

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# espera o wpp carregar
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

# tempo grande para eviatar que o wpp te bloqueie. É necessario um tempo consideravel, compativel como de uma pessoa normal enviando mensagem
num = 300

# já estamos com o login feito no whatsapp web
for i in tels:

    numero = i
    print(i)

    texto = urllib.parse.quote(f"{mensagem}")
    print(texto)

    link = f"https://web.whatsapp.com/send?phone=55{numero}&text={texto}"

    navegador.get(link)

    # espera o wpp carregar
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    # uso do tempo
    time.sleep(num)

    navegador.find_element(By.CLASS_NAME,"epia9gcq").click()
    time.sleep(10)

