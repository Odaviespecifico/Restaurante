from Gerenciamento import estoque,cardapio,mesa,pagamento
from Uteis import *

e = estoque()
c = cardapio()
m = mesa()
p = pagamento()
print_ornamentado('Gerenciamento de restaurantes')
while True: #Menu
    print(opcoes_geral)
    op = input("Digite a opção desejada: ")
    match op:
        case '1': #Estoque
            print_ornamentado('Estoque')
            while True:
                print(opcoes_estoque)
                op = input("Digite a opção desejada: ")
                match op:
                    case '1':
                        e.consultar()
                    case '2':
                        e.cadastrar()
                    case '3':
                        e.editar()
                    case '4':
                        e.remover()
                    case '5':
                        break
                    case _:
                        print(f'{vermelho}Opção inválida{branco}')
                        continue
            print_ornamentado("Menu principal")
        case '2': #Cozinha
            print_ornamentado('Cozinha')
            while True:
                print(opcoes_cardapio)
                op = input("Digite a opção desejada: ")
                match op:
                    case '1':
                        c.consultar()
                    case '2':
                        c.cadastrar()
                    case '3':
                        c.atualizar()
                    case '4':
                        c.remover()
                    case '5':
                        break
                    case _:
                        print(f"{vermelho}Opção inválida{branco}")
        case '3': #Mesas
            print_ornamentado("Mesas e pedidos")
            while True:
                print(opcoes_mesa)
                op = input("Digite a opção desejada: ")
                match op:
                    case '1':
                        m.exibir()
                    case '2':
                        m.cadastrar()
                    case '3':
                        m.ocupar()
                    case '4':
                        for i in range(len(m.mesas)):
                            m.livrar(i-1,False)
                    case '5':
                        break
                        
                    case _:
                        print(f"{vermelho}Opção inválida{branco}")
        case '4': #Pedidos
            while True:
                print(opcoes_pedido)
                op = input("Digite a opção desejada: ")
                match op:
                    case '1':
                        m.exibir()
                        mesa = int(input('Qual mesa você deseja alterar o pedido? '))
                        m.mostrar_pedido(mesa)
                        m.pedido(mesa,False)
                    case '2':
                        m.fila_de_pedidos()
                    case '3': #TBWW
                        m.fila_de_pedidos()
                        pedido = int(input('Qual a mesa do pedido você quer alterar? '))
                        m.pedido
                    case '4':
                        m.exibir()
                        mesa = int(input('Qual mesa você deseja alterar o status pedido? '))
                        m.mostrar_pedido(mesa)
                        m.status_pedido(mesa)
                    case '5':
                        break
                    case _:
                        print(f"{vermelho}Opção inválida{branco}")
        case '5': #Pagamento
            print_ornamentado('Pagamento')
            while True:
                print(opcoes_pagamento)
                op = input('Digite a opção desejada: ')
                match op:
                    case '1':
                        p.conta_total()
                    case '2':
                        p.pagamento()
                    case '3':
                        break
                    case _:
                        print(f'{vermelho}Opção inválida{branco}')
        case '6': #Sair
            break
        case _:
            print(f"{vermelho}Opção inválida{branco}")
            continue