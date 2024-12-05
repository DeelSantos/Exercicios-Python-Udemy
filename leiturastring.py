frase = """O Python é uma linguagem de programação
multiparadigma.
Python foi criado por Guido Van Rossum.
""".lower()

i = 0

quantidade_de_vezes = 0
letra_que_mais_apareceu = ''

while i < len(frase):
    
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_atual = frase.count(letra_atual)

    if quantidade_de_vezes < qtd_atual:
        quantidade_de_vezes = qtd_atual
        letra_que_mais_apareceu = letra_atual
    
    i += 1 
    
    
print(f"A letra que mais apareceu foi '{letra_que_mais_apareceu}' e ela apareceu {quantidade_de_vezes}x")