
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

# desabilita os avisos
GPIO.setwarnings(False)

# cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()

# criacao da variavel que armazena o texto que será gravado na tag
texto = "12704331"  # altere para o texto que deseja gravar

# escreve a tag assim que ela for aproximada do leitor, e informa a conclusão
print("Aproxime a tag do leitor para gravar.")

leitor.write(texto)  # função que realiza a gravação do texto configurado
print("Concluído!")

sleep(5)  # aguarda 5 segundos

print("Aproxime a tag do leitor para leitura.")

while True:  # loop
    # cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente
    id, texto = leitor.read()
    # exibe as informações coletadas
    print("ID: {}\nTexto: {}".format(id, texto))
    sleep(3)  # aguarda 3 segundos para nova leitura
