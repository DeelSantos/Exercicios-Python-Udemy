"""
Iterando Strings com While
"""


nome = input("Digite seu nome: ")
contador = 0
tamanho_nome = len(nome)

while contador < tamanho_nome:
    
    letra = nome[contador]
    
    contador += 1
    if letra == "E":
        continue
    print(f"{letra}", end='*')
