"""Calculadora com While"""

import time

while True:
    numero_1 = (input("Digite um número: "))
    numero_2 = (input("Digite outro número: "))
    print("""Selecione um operador: +*-/""")
    operador = (input())
    numeros_validos = None
    try:
        numero_float1 = float(numero_1)
        numero_float2 = float(numero_2)
        numeros_validos = True        
        
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos os números digitados são invalidos")
        continue
    
    
    operadores_validos = "+*-/"
    
    if operador not in operadores_validos:
        print("Operador Inválido")
        continue
    
    if len(operador) > 1:
        print("Digite apenas um operador ")
        continue
    
    print("Estamos realizando a conta...")
    time.sleep(2)
    
    
    if operador == "+" :
        soma = numero_float1 + numero_float2
        print(f"A soma dos números {numero_float1} e {numero_float2} é {soma}")
    elif operador == "*":
        mult = numero_float1 * numero_float2
        print(f"A multiplicação dos números {numero_float1} e {numero_float2} é {mult}")
    elif operador == "-":
        subs = numero_float1 - numero_float2
        print(f"A subtração dos números {numero_float1} e {numero_float2} é {subs}")
    elif operador == "/":
        div = numero_float1 / numero_float2
        print(f"A divisão dos números {numero_float1} e {numero_float2} é {div}")
    
    
    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    
    
    if sair is True:
        break
    
print("Muito obrigado por usar a Calculadora! ")
    
