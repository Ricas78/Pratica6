from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

# desabilita os avisos
GPIO.setwarnings(False)

GPIO.stmode(GPIO, BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura.")

ID = {'712936067078'}

try:
    while True:  # loop
        id, texto = leitor.read()
        id = str(id)
        if id in ID:
            GPIO.output(23, GPIO.HIGH)
            print("acesso liberado")
            sleep(3)
            GPIO.output(23, GPIO.LOW)
            sleep(1)
        else:
            GPIO.output(22, GPIO.HIGH)
            print("acesso negado")
            sleep(3)
            GPIO.output(22, GPIO.LOW)
            sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()  # toda vez que interrompermos o programa com crtl C o pino vai ser limpado automaticmanete
