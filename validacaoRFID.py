from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

# desabilita os avisos
GPIO.setwarnings(False)
# configura os pinos GPIOs da rasp que serão utilizados como pinos de saída
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura.")

try:
    while True:  # loop
        # cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente
        id, texto = leitor.read()
        # condicional para verificar se o id do cartão é o mesmo do salvo no código
        if id == 712936067078:
            # pisca o led verde e informa a mensagem de "acesso liberado" se a condição for satisfeita
            GPIO.output(23, GPIO.HIGH)
            print("acesso liberado")
            sleep(3)
            GPIO.output(23, GPIO.LOW)
            sleep(1)
        else:
            # pisca o led vermelho e informa a mensagem de "acesso negado" se a condição não for satisfeita
            GPIO.output(22, GPIO.HIGH)
            print("acesso negado")
            sleep(3)
            GPIO.output(22, GPIO.LOW)
            sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()  # toda vez que interrompermos o programa com crtl C o pino vai ser limpado automaticmanete
