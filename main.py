from Gerenciamento import estoque,cardapio,mesa
from Uteis import *

e = estoque()
c = cardapio()
m = mesa()
print_ornamentado('Gerenciamento de restaurantes')
while True:
    print(opções_geral)
    op = input("Digite a opção desejada: ")
    match op:
        case '1':
            print_ornamentado('Estoque')
            while True:
                print(opções_estoque)
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
        case '2':
            print_ornamentado('Cozinha')
            while True:
                print(opções_cardapio)
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
        case '3':
            print_ornamentado("Mesas e pedidos")
            while True:
                print(opções_mesa)
                op = input("Digite a opção desejada: ")
                match op:
                    case '1':
                        m.exibir()
                    case '2':
                        m.cadatrar()
                    case '3':
                        m.pedido()
                    case '4':
                        m.mostrar_pedido()
                    case '5':
                        m.ocupar()
                    case '6':
                        for i in range(len(m.mesas)):
                            m.livrar(i-1,False)
                    case '7':
                        break
                    case _:
                        print(f"{vermelho}Opção inválida{branco}")
        case '4':
            pass
        case '5':
            break
        case _:
            print(f"{vermelho}Opção inválida{branco}")
            continue