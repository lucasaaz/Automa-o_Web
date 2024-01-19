import time
import urllib
import pyautogui
import webbrowser

mensagem = 'Olá, tudo bem?'
tels = ['31912345678', '31987654321']

# abrindo pagina do wpp
webbrowser.open('https://web.whatsapp.com/')
time.sleep(30)  

for i in tels:

    # pegando numero do celular
    numero = i
    print(i)

    # formatando mensagem
    texto = urllib.parse.quote(f"{mensagem}")
    print(texto)

    try:

        # link para abrir mensagem com a pessoa
        link = f"https://web.whatsapp.com/send?phone=55{numero}&text={texto}"
        webbrowser.open(link)
        time.sleep(10)
        botao = pyautogui.locateCenterOnScreen('botao.png')
        time.sleep(2)
        pyautogui.click(botao[0],botao[1])
        time.sleep(2)
        pyautogui.hotkey('ctrl','w')
        time.sleep(2)

    except:
        
        print(f'Não foi possível enviar mensagem para {numero}')