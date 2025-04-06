from Gerenciamento import estoque,cardapio
from Uteis import *

e = estoque()
c = cardapio()
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
            pass
        case '4':
            pass
        case '5':
            break
        case _:
            print(f"{vermelho}Opção inválida{branco}")
            continue