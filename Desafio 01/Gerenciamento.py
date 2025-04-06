import datetime
from Uteis import *

class estoque:
    def __init__(self):
        with open("Desafio 01\estoque.txt",encoding='UTF-8') as items:
            self.content = eval(items.read())

    def consultar(self):
        print_ornamentado('Itens no estoque')
        for i in self.content:
            print('-'*10)
            print(f"Código do item: {i['Código']}")
            print(f"Nome do item: {i['Nome']}")
            print(f"Quantidade: {i['Quantidade']}{i['Unidade']}")
            print(f"preço: R${i['Preço']}")
            print(f"Validade: {i['Validade']}")
        else:
                print('-'*10)

    def cadastrar(self):
        print("Cadastrar produto")
        cod = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ") 
        quantidade = input("Digite a quantidade do produto: ")
        unidade = input("Digite a unidade de medida do produto: ")
        preço = input("Digite o preço do produto: ")
        validade = input("Digite a validade do produto: ")
        item = {"codigo":cod,"nome":nome,"quantidade":quantidade,"unidade":unidade,"preço":preço,"validade":validade}
        self.estoque_items.append(item)
        with open("Desafio 01\estoque.txt","w",encoding="UTF-8",newline="") as estoque:
            estoque.write(str(self.estoque_items))


if __name__ == '__main__':
    e = estoque()
    e.consultar()