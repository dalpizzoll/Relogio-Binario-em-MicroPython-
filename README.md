# ⏰ Relógio Binário BCD com NeoPixel (MicroPython)

Este projeto implementa um relógio binário codificado em decimal (**BCD - Binary-Coded Decimal**) utilizando **MicroPython** e um anel/fita de **16 LEDs NeoPixel (WS2812B)** acoplado a um microcontrolador (ESP32/ESP8266), com suporte para o simulador **Wokwi**.

---

## 📌 Como Funciona a Visualização BCD

O horário (Horas e Minutos) no formato **12 horas** é dividido em 4 dígitos. Cada dígito é representado por um grupo de **4 LEDs** (4 bits):

$$\text{Horário: HH:MM} \longrightarrow [H_{\text{dezena}}] \quad [H_{\text{unidade}}] \quad [M_{\text{dezena}}] \quad [M_{\text{unidade}}]$$

| Posição dos LEDs | Parâmetro | Descrição / Bits |
| :--- | :--- | :--- |
| **LED 0** | **PM Indicator** | Acende se for **PM**, apaga se for **AM** *(Bit MSB da dezena de hora)* |
| **LEDs 1 a 3** | **Dezena de Hora** | Representação binária da dezena da hora (0 ou 1) |
| **LEDs 4 a 7** | **Unidade de Hora** | Representação binária da unidade da hora (0 a 9) |
| **LEDs 8 a 11** | **Dezena de Minuto** | Representação binária da dezena do minuto (0 a 5) |
| **LEDs 12 a 15** | **Unidade de Minuto** | Representação binária da unidade do minuto (0 a 9) |

---

## 🎨 Cores Conforme o Turno do Dia

A iluminação dos LEDs varia automaticamente conforme a hora do dia para facilitar a leitura visual:

| Intervalo de Horário | Período do Dia | Cor RGB |
| :--- | :--- | :--- |
| **06:00 – 07:59** | Amanhecer / Manhã | 🟠 Laranja `(255, 165, 0)` |
| **08:00 – 17:59** | Dia | 🟡 Amarelo `(255, 255, 0)` |
| **18:00 – 18:59** | Entardecer / Pôr do Sol | 🔴 Vermelho `(255, 0, 0)` |
| **19:00 – 05:59** | Noite | 🟣 Magenta `(255, 0, 255)` |

---

## 🛠️ Hardware Necessário e Pinagem

- **Microcontrolador:** ESP32 ou ESP8266.
- **Display:** Anel ou fita de 16 LEDs NeoPixel WS2812B.
- **Conexão:**
  - **DIN (Data In):** GPIO 2
  - **VCC:** 5V / 3.3V
  - **GND:** GND

---

## 🚀 Como Executar

1. **No Simulador Wokwi:**
   - Adicione um ESP32 e um anel NeoPixel de 16 LEDs no circuito.
   - Conecte o pino de dados do NeoPixel ao `GPIO 2`.
   - Cole o código no arquivo `main.py` e inicie a simulação (o Wokwi conecta automaticamente à rede `Wokwi-GUEST`).

2. **Em Hardware Real:**
   - Altere a linha `wifi.connect("Wokwi-GUEST", "")` colocando o SSID e a senha da sua rede Wi-Fi local.
   - Carregue o código no microcontrolador via **Thonny IDE** ou **VS Code (Pymakr)**.

---

## 📂 Estrutura do Código

```text
├── main.py       # Script principal (Wi-Fi, NTP, Lógica BCD e Controle do NeoPixel)
├── diagram.json  # Diagrama do projeto
└── README.md     # Documentação do projeto
