import datetime
from Uteis import *
editar = False
class estoque:
    def __init__(self):
        with open("estoque.txt",encoding='UTF-8') as items:
            self.content = eval(items.read())

    def consultar(self):
        global editar
        if editar != True:
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
        print_ornamentado('Cadastrar produto')
        cod = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ") 
        quantidade = input("Digite a quantidade do produto: ")
        unidade = input("Digite a unidade de medida do produto: ")
        preço = input("Digite o preço do produto: ")
        validade = input("Digite a validade do produto: ")
        item = {"Código":cod,"Nome":nome,"Quantidade":quantidade,"Unidade":unidade,"Preço":preço,"Validade":validade}
        self.content.append(item)
        mostrar_item(item)
        print(verde,'produto cadastrado com sucesso',branco)
        with open("estoque.txt","w",encoding="UTF-8",newline="") as estoque:
            estoque.write(str(self.content))
        
    def editar(self):
        global editar
        editar = True
        print_ornamentado('Alterar produto')
        self.consultar()
        Escolha = input('Digite o código ou nome do item que deseja editar: ')
        posição = 0
        for i in self.content:
            # print(i)
            if i["Código"] == Escolha or i["Nome"] == Escolha:
                mostrar_item(i,True)
                while True:
                    escolha = input(f"{rosa}Qual parte você quer editar? {branco}")
                    match escolha:
                        case "1":
                            self.content[posição]['Código'] = input("Digite o novo código do produto: ")
                            editou(self.content[posição])
                        case "2":
                            self.content[posição]['Nome'] = input("Digite o novo nome do produto: ")
                            editou(self.content[posição])
                        case "3":
                            self.content[posição]['Quantidade'] = input("Digite a nova quantidade do produto: ")
                            editou(self.content[posição])
                        case "4":
                            self.content[posição]['Unidade'] = input("Digite a nova unidade do produto: ")
                            editou(self.content[posição])
                        case "5":
                            self.content[posição]['Preço'] = input("Digite o novo preço do produto: ")
                            editou(self.content[posição])
                        case "6":
                            self.content[posição]['Validade'] = input("Digite a nova validade do produto: ")
                            editou(self.content[posição])
                        case _:
                            print(f'{vermelho}Opção inválida{branco}')
                break
            posição += 1
        else:
            if posição == 0:
                print(f'{vermelho}Item não encontrado!{branco}')
            if posição > 0:
                print(f'{vermelho}Item não encontrado, talvez você esteja colocando o nome minúsculo!{branco}')

        with open("estoque.txt","w",encoding="UTF-8",newline="") as estoque:
            estoque.write(str(self.content))
        
            
                        
                        

if __name__ == '__main__':
    e = estoque()
    e.editar()