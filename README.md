# Automação Web com Whatsapp <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40px"/> 
 
### Este código em Python utiliza a biblioteca Selenium para automatizar o envio de mensagens pelo WhatsApp Web.

Aqui está um resumo do que o código faz:

1 - Importa as bibliotecas necessárias do Selenium e outras para manipulação de tempo (time) e manipulação de URLs (urllib).

2 - Define uma mensagem padrão (mensagem) e uma lista de números de telefone (tels) para os quais as mensagens serão enviadas.

3 - Inicia uma instância do navegador Chrome usando o WebDriver do Selenium.

4 - Navega até o site do WhatsApp Web (https://web.whatsapp.com/) e aguarda até que a página seja carregada completamente.

5 - Itera sobre os números de telefone na lista tels.

6 - Gera um link para enviar uma mensagem para o número de telefone específico, usando a função urllib.parse.quote para formatar a mensagem.

7 - Navega até o link gerado para abrir a conversa no WhatsApp Web.

8 - Aguarda até que a página da conversa seja carregada completamente.

9 - Aguarda um período de tempo (num) para simular uma pessoa enviando mensagem normalmente, a fim de evitar bloqueios.

10 - Localiza e clica no elemento HTML que representa o campo de entrada de mensagem (navegador.find_element(By.CLASS_NAME,"epia9gcq")).

11 - Aguarda um tempo adicional para garantir que o campo de entrada esteja pronto para receber texto.

12 - Fecha o navegador após enviar a mensagem para um número.

### Observação:
É importante observar que a automação de interações com serviços online, como o WhatsApp Web, pode violar os termos de serviço desses serviços. O uso de automação deve ser feito com responsabilidade e em conformidade com as políticas do serviço em questão. Além disso, o código pode precisar de ajustes para acompanhar eventuais alterações na estrutura HTML do WhatsApp Web.
