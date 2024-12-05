"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa que com erros de indicies inexistentes na lista
"""

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_lista(lista):
    print("Lista salva com sucesso")
    for indice, valor in enumerate(lista):
        print(indice, valor)

lista = []

while True:
    print("Selecione uma opção: ")
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")
    
    if opcao == "i":
        limpar_tela()
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == "a":
        limpar_tela()
        try:
            indice = int(input("Digite o índice do item que deseja apagar: "))
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception as e:
            print(f'Erro desconhecido: {e}')
    elif opcao == "l":
        limpar_tela()
        for indice, valor in enumerate(lista):
            print(indice, valor)
    elif opcao == "s":
        limpar_tela()
        salvar = input("Deseja salvar sua lista? [s]im ou [n]ão: ")
        if salvar == 's':
            salvar_lista(lista)
            break
        elif salvar == 'n':
            print("Beleza, flw")
            confirmar_saida = input("Tem certeza que deseja sair? [s]im ou [n]ão: ")
            if confirmar_saida == 's':
                break
        