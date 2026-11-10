from neopixel import NeoPixel
from time import localtime, ticks_ms, sleep_ms
from ntptime import settime
from network import WLAN, STA_IF
from machine import Pin, reset

pixels = NeoPixel(Pin(2, Pin.OUT), 16)

binarios = {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "0101",
    6: "0110",
    7: "0111",
    8: "1000",
    9: "1001"
}

def conectar_wifi():
    wifi = WLAN(STA_IF)
    wifi.active(True)
    wifi.connect("Wokwi-GUEST", "")
    tentativas = 0
    while not wifi.isconnected() and tentativas < 20:
        sleep_ms(250)
        tentativas += 1
    return wifi.isconnected()

if conectar_wifi():
    try:
        settime()
    except:
        print("falhou")
else:
    reset()

def para_12h(hora):
    if hora == 0:
        return 12, "AM"
    elif hora == 12:
        return 12, "PM"
    elif hora > 12:
        return hora - 12, "PM"
    else:
        return hora, "AM"

def cor_do_periodo(hora):
    if 8 <= hora < 18:
        return (255, 255, 0)
    elif 18 <= hora < 19:
        return (255, 0, 0)
    elif hora >= 19 or hora < 6:
        return (255, 0, 255)
    else:
        return (255, 165, 0)

tAnt = ticks_ms()
sicronizacao = ticks_ms()

while True:
    agora = ticks_ms()
    if agora - sicronizacao >= 21600000:
        try:
            settime()
        except:
            pass
        sicronizacao = agora
    if agora - tAnt >= 1000:
        tempo_atual = localtime()
        hora = tempo_atual[3] - 3 #Horário de brasília
        minuto = tempo_atual[4]
        hora_ajustada, periodo = para_12h(hora)
        h_dezena = hora_ajustada // 10
        h_unidade = hora_ajustada % 10
        m_dezena = minuto // 10
        m_unidade = minuto % 10
        formatacao = [h_dezena, h_unidade, m_dezena, m_unidade]
        cor = cor_do_periodo(hora)
        contador = 0

        for i, num in enumerate(formatacao):
            bits = binarios[num]
            for posicao, bit in enumerate(bits):
                if i == 0 and posicao == 0:
                    pixels[contador] = cor if periodo == "PM" else (0, 0, 0)
                else:
                    pixels[contador] = cor if bit == "1" else (0, 0, 0)
                contador += 1

        pixels.write()
        tAnt = agora
        print(formatacao)
