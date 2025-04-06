import datetime
from Uteis import *

class estoque:
    def __init__(self):
        with open("estoque.txt",encoding='UTF-8') as items:
            self.content = eval(items.read())

    def consultar(self):
        print_ornamentado('Itens no estoque')
        for i in self.content:
            print('-'*20)
            print(f"{azul}Código do item:{branco} {i['Código']}")
            print(f"{azul}Nome do item:{branco} {i['Nome']}")
            print(f"{azul}Quantidade:{branco} {i['Quantidade']} {i['Unidade']}")
            print(f"{azul}preço:{branco} R${i['Preço']}")
            print(validade_cor(i['Validade']))
        else:
                print('-'*20)

    def cadastrar(self):
        print("Cadastrar produto")
        cod = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ") 
        quantidade = input("Digite a quantidade do produto: ")
        unidade = input("Digite a unidade de medida do produto: ")
        preço = input("Digite o preço do produto: ")
        validade = input("Digite a validade do produto: ")
        item = {"Código":cod,"Nome":nome,"Quantidade":quantidade,"Unidade":unidade,"Preço":preço,"Validade":validade}
        self.content.append(item)
        with open("estoque.txt","w",encoding="UTF-8",newline="") as estoque:
            estoque.write(str(self.content))


if __name__ == '__main__':
    e = estoque()
    e.consultar()