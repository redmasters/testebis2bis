"""
Teste Ping-Ping
- Escreva uma função que receba a pontuação atual separada pelo
caractere ":" como único parâmentro, e retorne "Jogador A" ou
"Jogador B", dependendo de quem é a vez de sacar.
"""
import time

def pausa():
    time.sleep(0.3)
    return None

def saque():
    a = 0
    b = 0
    for a in range(1, 21):
        pausa()
        print("A", a, ":", b,  "B")
        if a > b:
            b += 1
            pausa()
            print("A", a, ":", b,  "B")

            
saque()


