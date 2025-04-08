from datetime import date
import csv

azul = '\033[34m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
branco = '\033[37m'
rosa = '\033[35m'


def print_ornamentado(texto):
    print(azul)
    print("="*30)
    print(f"{texto:^30}")	
    print("="*30)
    print(branco)

def validade_cor(validade):
    ano,dia,mes = int(validade[6:]),int(validade[0:2]),int(validade[3:5])
    # print(date(ano,mes,dia))
    # print(date.today())
    diferença = (date(ano,mes,dia) - date.today()).days
    # print(diferença)
    if diferença >= 3:
        return f"{azul}Validade:{branco} {verde}{validade}{branco}"
    elif diferença >= 0:
        return f"{azul}Validade:{branco} {amarelo}{validade}{branco}"
    else:
        return f"{azul}Validade:{branco} {vermelho}{validade}{branco}"

def mostrar_item(item,editar=False):
    if not editar:
        print('-'*20)
        print(f"{azul}Código do item:{branco} {item['Código']}")
        print(f"{azul}Nome do item:{branco} {item['Nome']}")
        print(f"{azul}Quantidade:{branco} {item['Quantidade']} {item['Unidade']}")
        print(f"{azul}preço:{branco} R$ {item['Preço']}")
        print(validade_cor(item['Validade']))
    else:
        print('-'*20)
        print(f"1 - {azul}Código do item:{branco} {item['Código']}")
        print(f"2 - {azul}Nome do item:{branco} {item['Nome']}")
        print(f"3 - {azul}Quantidade:{branco} {item['Quantidade']}")
        print(f"4 - {azul}Unidade:{branco} {item['Unidade']}")
        print(f"5 - {azul}preço:{branco} R$ {item['Preço']}")
        print("6 - ",validade_cor(item['Validade']))

def editou(item):
    editar = False
    mostrar_item(item)
    print(f'{verde}Produto alterado com sucesso!{branco}')

def writedict(file,data,fn):
    with open(str(file),"w",encoding="UTF-8",newline="") as estoque:
        writer = csv.DictWriter(estoque, fieldnames=fn, delimiter=';')
        writer.writeheader()
        writer.writerows(data)

def disponiveis(itens,ingredientes):
    global c
    print(azul,"-"*30)
    print("Itens disponíveis no estoque:")
    print('-'*30,branco)
    c = 1
    for i in itens:
        for j in ingredientes:
            if i["Nome"] in j[0]:
                print(f'{c} - {azul}{i["Nome"]}{branco} - {i["Quantidade"]} {i["Unidade"]} - R${i["Preço"]}')
                c += 1
                break
        else:
            print(f'{c} - {rosa}{i["Nome"]}{branco} - {i["Quantidade"]} {i["Unidade"]} - R${i["Preço"]}')
            c += 1
            
opções_geral = """Opções:
\033[35m1\033[37m - Estoque
\033[35m2\033[37m - Cozinha
\033[35m3\033[37m - Mesas e Pedidos
\033[35m4\033[37m - Pagamento
\033[35m5\033[37m - sair"""

opções_estoque = """Opções:
\033[35m1\033[37m - Consultar estoque
\033[35m2\033[37m - Cadastrar produto
\033[35m3\033[37m - atualizar produto
\033[35m4\033[37m - Remover produto
\033[35m5\033[37m - voltar ao menu principal"""

opções_cardapio = """Opções:
\033[35m1\033[37m - Consultar cardápio
\033[35m2\033[37m - Cadastrar produto
\033[35m3\033[37m - atualizar produto
\033[35m4\033[37m - Remover produto
\033[35m5\033[37m - voltar ao menu principal"""

opções_mesa = """Opções:
\033[35m1\033[37m - Mostrar mesas
\033[35m2\033[37m - Adicionar mesa
\033[35m3\033[37m - Adicionar pedido
\033[35m4\033[37m - Mostrar pedido
\033[35m5\033[37m - Ocupar mesa reservada
\033[35m6\033[37m - Liberar todas as mesas
\033[35m7\033[37m - voltar ao menu principal"""

opções_pagamento = """Opções:
\033[35m1\033[37m - Mostrar conta
\033[35m2\033[37m - Pagar conta
\033[35m3\033[37m - voltar ao menu principal"""
if __name__ == "__main__":
    print(validade_cor('02/04/2025'))