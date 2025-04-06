import datetime
from Uteis import *
import csv
editar = False
class estoque:
    def __init__(self):
        with open('estoque.csv',encoding='UTF-8') as estoque:
            self.content = []
            for row in csv.DictReader(estoque,delimiter=';'):
                self.content.append(row)
        self.fn = ('Código','Nome','Quantidade','Unidade','Preço','Validade')
    def consultar(self):
        global editar
        if editar != True:
            print_ornamentado('Itens no estoque')
        for i in self.content:
            mostrar_item(i)
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
        writedict("estoque.csv",self.content,self.fn)

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
                            break
                        case "2":
                            self.content[posição]['Nome'] = input("Digite o novo nome do produto: ")
                            editou(self.content[posição])
                            break
                        case "3":
                            self.content[posição]['Quantidade'] = input("Digite a nova quantidade do produto: ")
                            editou(self.content[posição])
                            break
                        case "4":
                            self.content[posição]['Unidade'] = input("Digite a nova unidade do produto: ")
                            editou(self.content[posição])
                            break
                        case "5":
                            self.content[posição]['Preço'] = input("Digite o novo preço do produto: ")
                            editou(self.content[posição])
                            break
                        case "6":
                            self.content[posição]['Validade'] = input("Digite a nova validade do produto: ")
                            editou(self.content[posição])
                            break
                        case _:
                            print(f'{vermelho}Opção inválida{branco}')
                            break
                break
            posição += 1
        else:
            if posição == 0:
                print(f'{vermelho}Item não encontrado!{branco}')
            if posição > 0:
                print(f'{vermelho}Item não encontrado, talvez você esteja colocando o nome minúsculo!{branco}')

        writedict("estoque.csv",self.content,self.fn)
        
    def remover(self):
        print_ornamentado('Remover produto')
        global editar
        editar = True
        self.consultar()
        Escolha = input('Digite o código ou nome do item que deseja remover: ')
        posição = 0
        for i in self.content:
            if i["Código"] == Escolha or i["Nome"] == Escolha:
                mostrar_item(i)
                confirma = input(f'{vermelho}Você tem certeza que deseja remover o item {i["Nome"]}?\nDigite "s" para sim ou "n" para não: {branco}')
                if confirma == 's':
                    self.content.pop(posição)
                    print(f'{vermelho}Produto removido com sucesso!{branco}')
                else:
                    print(f'{verde}Produto não removido!{branco}')
                    break
                break
            posição += 1
        else:
            print(f'{vermelho}Item não encontrado, talvez você esteja colocando o nome minúsculo!{branco}')

        writedict("estoque.csv",self.content,self.fn)
                        
class cardapio:
    def __init__(self):
        self.cardápio = []
        self.estoque = []
        with open("cardápio.csv",encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardápio.append(i)
        with open('estoque.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.estoque.append(i)
        self.fn = ('Nome','Preço','Descrição','Ingredientes')
        print(self.cardápio)
        print(self.estoque)
    def consultar(self):
        print_ornamentado('Itens no cardápio')
        print(self.cardápio)
        c = 1
        for i in self.cardápio:
            print(azul,end="")
            print("-"*30)
            print(f"Item {c}:")
            print(f"{amarelo}{i['Nome']}{branco} - {verde}R$ {i['Preço']}")
            print(f"{rosa}{i['Descrição']}")
            print(azul,end="")
            print("-"*30)
            print(branco)
            c += 1
    
    def cadastrar(self):
        print_ornamentado('Cadastrar produto')
        nome = input("Digite o nome do produto: ") 
        preço = input("Digite o preço do produto: ")
        descrição = input("Digite a descrição do produto: ")
        ingredientes = []
        c = 1
        disponiveis(self.estoque,ingredientes)
        while True:
            escolha = input("Digite o nome ou número do item que deseja adicionar a receita: ")
            for i in self.estoque:
                if i["Nome"] == escolha:
                    quantidade = input(f"Digite a quantidade de {i['Nome']} que deseja adicionar: ")
                    print(f'{verde}Produto adicionado com sucesso!{branco}')
                    ingredientes.append((i["Nome"], quantidade))
                    break
                try:
                    if int(escolha) <= c:
                        quantidade = input(f"Digite a quantidade de {self.estoque[int(escolha)-1]['Nome']} que deseja adicionar: ")
                        ingredientes.append((self.estoque[int(escolha)-1]['Nome'], quantidade))
                        print(f'{verde}Produto adicionado com sucesso!{branco}')
                        break
                except:
                    pass
                c += 1
            else:
                print(f'{vermelho}Item não encontrado!{branco}')
            
            continue_ = input("Deseja adicionar mais ingredientes? (s/n): ")
            if continue_ == 's':
                disponiveis(self.estoque,ingredientes)
                continue
            else:
                self.cardápio.append({'Nome': nome, 'Preço': preço, 'Descrição': descrição, "Ingredientes":ingredientes})
                writedict("cardápio.csv",self.cardápio,self.fn)
                break
                
if __name__ == '__main__':
    e = estoque()
    c = cardapio()
    c.consultar()