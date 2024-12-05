""" 
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa que com erros de indicies inexistentes na lista
"""

import os

lista = []

while True:
    print("Selecione uma opção: ")
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")
    
    if opcao == "i":
        os.system('cls')
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == "a":
        apagar = int(input("Selecione um valor para apagar: "))
        os.system('cls')
        try:
            indice = apagar
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == "l":
        os.system('cls')
        for indice, valor in enumerate(lista):
            print(indice, valor)
    elif opcao == "s":
        os.system('cls')
        salvar = input("Deseja salvar sua lista? [s]im ou [n]ão: ")
        if salvar == 's':
            print("Lista salva com sucesso")
            for indice, valor in enumerate(lista):
                print(indice, valor)
            break
        elif salvar == 'n':
            print("Beleza, flw")
            break
    else:
        print("Opção Inválida")