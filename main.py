from Gerenciamento import estoque
from Uteis import *

e = estoque()
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
                        pass
                    case '5':
                        break
                    case _:
                        print(f"{cores['vermelho']}Opção inválida{cores['branco']}")
                        continue
            print("Menu principal")
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            break
        case _:
            print(f"{cores['vermelho']}Opção inválida{cores['branco']}")
            continue