import datetime
from Uteis import *
import csv
import random
editar = False
class estoque:
    def __init__(self):
        with open('estoque.csv',encoding='UTF-8') as estoque:
            self.content = [] # Lista para armazenar o conteúdo do estoque
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
        nome = input("Digite o nome do produto: ").capitalize()
        quantidade = input("Digite a quantidade do produto: ")
        unidade = input("Digite a unidade de medida do produto: ")
        preco = input("Digite o preço do produto: ")
        validade = input("Digite a validade do produto: ")
        item = {"Código":cod,"Nome":nome,"Quantidade":quantidade,"Unidade":unidade,"Preço":preco,"Validade":validade}
        self.content.append(item)
        mostrar_item(item)
        print(verde,'produto cadastrado com sucesso',branco)
        writedict("estoque.csv",self.content,self.fn)

    def editar(self):
        global editar
        editar = True
        print_ornamentado('Alterar produto')
        self.consultar()
        Escolha = input('Digite o código ou nome do item que deseja editar: ').capitalize()
        posicao = 0
        for i in self.content:
            # print(i)
            if i["Código"] == Escolha or i["Nome"] == Escolha:
                mostrar_item(i,True)
                while True:
                    escolha = input(f"{rosa}Qual parte você quer editar? {branco}")
                    match escolha:
                        case "1":
                            self.content[posicao]['Código'] = input("Digite o novo código do produto: ")
                            editou(self.content[posicao])
                            break
                        case "2":
                            self.content[posicao]['Nome'] = input("Digite o novo nome do produto: ")
                            editou(self.content[posicao])
                            break
                        case "3":
                            self.content[posicao]['Quantidade'] = input("Digite a nova quantidade do produto: ")
                            editou(self.content[posicao])
                            break
                        case "4":
                            self.content[posicao]['Unidade'] = input("Digite a nova unidade do produto: ")
                            editou(self.content[posicao])
                            break
                        case "5":
                            self.content[posicao]['Preço'] = input("Digite o novo preço do produto: ")
                            editou(self.content[posicao])
                            break
                        case "6":
                            self.content[posicao]['Validade'] = input("Digite a nova validade do produto: ")
                            editou(self.content[posicao])
                            break
                        case _:
                            print(f'{vermelho}Opção inválida{branco}')
                            break
                break
            posicao += 1
        else:
            if posicao == 0:
                print(f'{vermelho}Item não encontrado!{branco}')
            if posicao > 0:
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
        self.cardapio = []
        self.estoque = []
        with open("cardápio.csv",encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardapio.append(i)
        with open('estoque.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.estoque.append(i)
        self.fn = ('Nome','Preço','Descrição','Ingredientes')
    def consultar(self):
        print_ornamentado('Itens no cardápio')
        c = 1
        for i in self.cardapio:
            print(azul,end="")
            if c == 1:
                print("-"*30)
            print(f"{branco}Item {c}:")
            print(f"{amarelo}{i['Nome']}{branco} - {verde}R$ {i['Preço']}")
            print(f"{rosa}{i['Descrição']}")
            print(azul,end="")
            print("-"*30)
            c += 1
        print(branco,end="")
    
    def cadastrar(self): #Cadastro de produto
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
                print(self.estoque)
                continue
            else:
                self.cardapio.append({'Nome': nome, 'Preço': preço, 'Descrição': descrição, "Ingredientes":ingredientes})
                writedict("cardápio.csv",self.cardapio,self.fn)
                break
    def atualizar(self):
        self.consultar()
        escolha = int(input("Digite o número do item que deseja alterar: "))
        if escolha <= len(self.cardapio):
            item = self.cardapio[escolha-1]
            print(azul,end="")
            print("-"*30)
            print(f"{amarelo}1 - {item['Nome']}{branco}")
            print(f"{verde}2 - R$ {item['Preço']}")
            print(f"{rosa}3 - {item['Descrição']}")
            print(branco,end="")
            print("4 -",end=" ")
            c = 1
            for j in eval(item['Ingredientes']):
                if c+1 < len(eval(item['Ingredientes'])):
                    print(j[0],end=", ")
                elif c == len(eval(item['Ingredientes'])):
                    print(j[0],end=".")
                else:
                    print(j[0],end=" e ")
                c += 1
            print()
            print(azul,end="")
            print("-"*30)
        else:
            print(f"{vermelho}Opção inválida{branco}")
        escolha2 = input("Digite o número do que deseja alterar: ")
        match escolha2:
            case "1":
                print(branco,end="")
                self.cardapio[escolha-1]['Nome'] = input("Digite o novo nome do produto: ") 
                self.consultar()
            case "2":
                print(branco,end="")
                self.cardapio[escolha-1]['Preço'] = input("Digite o novo preço do produto: ") 
                self.consultar()
            case "3":
                print(branco,end="")
                self.cardapio[escolha-1]['Descrição'] = input("Digite a nova descrição do produto: ") 
                self.consultar()
            case "4":
                ingredientes = []
                c = 1
                disponiveis(self.estoque,ingredientes)
                while True:
                    escolha3 = input("Digite o nome ou número do item que deseja adicionar a receita: ")
                    for i in self.estoque:
                        if i["Nome"] == escolha3:
                            quantidade = input(f"Digite a quantidade de {i['Nome']} que deseja adicionar: ")
                            print(f'{verde}Produto adicionado com sucesso!{branco}')
                            ingredientes.append((i["Nome"], quantidade))
                            break
                        try:
                            if int(escolha3) <= c:
                                quantidade = input(f"Digite a quantidade de {self.estoque[int(escolha3)-1]['Nome']} que deseja adicionar: ")
                                ingredientes.append((self.estoque[int(escolha3)-1]['Nome'], quantidade))
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
                        print(f'{escolha=}')
                        print(self.cardapio)
                        continue
                    else:
                        for i in self.cardapio:
                            print(f'A linha é: {i}')
                            print(escolha)
                        self.cardapio[int(escolha-1)]['Ingredientes'] = ingredientes
                        break
        writedict("cardápio.csv",self.cardapio,self.fn)
    def remover(self):
        self.consultar()
        escolha = int(input("Digite o número do item que deseja remover: "))
        escolha2 = input(f"{vermelho}Certeza que deseja remover {self.cardapio[escolha-1]['Nome']}? s/n")
        if escolha2 == 's':
            self.cardapio.pop(escolha-1)
            writedict("cardápio.csv",self.cardapio,self.fn)
            print(f"Item removido com sucesso{branco}")
            self.consultar()
        else:
            print(f'{verde}Item não removido')
            self.consultar()

class mesa:
    def __init__(self):
        self.mesas = []
        with open('mesa.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.mesas.append(i)
        self.fn = ('Número','Capacidade','Status','Pessoas','Pedido')
        
        # Status -> 0 = livre 1 = reservada 2 = ocupada
        
    def exibir(self,colunas=5,editar=False):
        self.__init__()
        if editar != True:
            print_ornamentado('Mesas')
        for i in range(len(self.mesas)):
            if self.mesas[i]['Status'] == '0':
                print(f'{verde}{i+1:2}{branco}', end=" ")
            if self.mesas[i]['Status'] == '1':
                print(f'{amarelo}{i+1:2}{branco}', end=" ")
            if self.mesas[i]['Status'] == '2':
                print(f'{vermelho}{i+1:2}{branco}', end=" ")
            if (i+1) % colunas == 0 and i != 0:
                print()

    def cadatrar(self):
        self.exibir(editar=True)
        print_ornamentado('Cadastrar mesa')
        numero = input("Digite o número da mesa: ")
        capacidade = input("Digite a capacidade da mesa: ")
        item = {"Número":numero,"Capacidade":capacidade,"Status":0,"Pessoas":0}
        self.mesas.append(item)
        writedict("mesa.csv",self.mesas,self.fn)
        print(f'{verde}Mesa cadastrada com sucesso!{branco}')
        self.exibir(editar=True)

    def livrar(self,mesa,exibir=True):
        if exibir:
            self.exibir(editar=True)
        self.mesas[mesa-1]['Status'] = 0
        self.mesas[mesa-1]['Pessoas'] = 0
        self.mesas[mesa-1]['Pedido'] = []
        writedict("mesa.csv",self.mesas,self.fn)
        print(f'{verde}Mesa {mesa+1} liberada com sucesso!{branco}')

    def ocupar(self,mesa='False'):
        self.exibir(editar=True)
        print_ornamentado('Adicionar clientes a mesa')
        while True: #Loop para definir o número da mesa e quantidade de pessoas
            if mesa == 'False':    
                mesa = int(input("Digite o número da mesa que deseja ocupar: "))
            if self.mesas[mesa-1]['Status'] == '2':
                print(f'{vermelho}A mesa {mesa} está ocupada, escolha outra!{branco}')
                continue
            if self.mesas[mesa-1]['Status'] == '1':
                print(f'{vermelho}A mesa {mesa} está reservada,{branco}',end=" ")
                escolha = input('Deseja alocar o cliente mesmo assim? s/n ')
                if escolha != 's':
                    continue
            pessoas = int(input(f"Digite o número de pessoas que deseja colocar na mesa {mesa}: "))
            if pessoas > int(self.mesas[int(mesa)-1]['Capacidade']):
                    print(f'{vermelho}A quantidade de pessoas é maior do que a capacidade da mesa. Talvez você consiga cadastrar em duas mesas!{branco}')
            else:
                break
        escolha = input('Você deseja fazer uma reserva ou ocupar a mesa? r/o: ')
        if escolha == 'r':
            self.mesas[mesa-1]['Status'] = 1
        else:
            self.mesas[mesa-1]['Status'] = 2
        self.mesas[mesa-1]['Pessoas'] = pessoas
        writedict("mesa.csv",self.mesas,self.fn)
        print(f'{verde}Mesa {mesa} ocupada com sucesso!{branco}')
        self.exibir(editar=True)

    def pedido(self,mesa=-1):
        self.exibir()
        if mesa == -1:
            escolha = int(input('De qual mesa é o pedido? '))
        else:
            escolha = mesa
        if self.mesas[escolha-1]['Status'] == '0':
            op = input(f'A mesa {azul}{escolha}{branco} não tem clientes cadastrados, deseja adicionar um cliente? s/n: ')
            if op == 's':
                self.ocupar(escolha)
            else:
                c.consultar()
                pass
        c.consultar()
        pedidos = []
        pedido = 1
        
        while True:
            pedido = input('Digite o pedido da mesa, um item por vez, digite 0 para parar:')
            if pedido == '0':
                break
            pedidos.append(int(pedido)-1)
            print(f'{azul}Pedido da mesa {escolha-1}:{branco}',end=' ')
            for i in range(len(pedidos)):
                print(f"{c.cardapio[int(pedidos[i-1])]['Nome']}",end=', ')
            else:
                print()
            self.mesas[escolha-1]['Pedido'] = pedidos
            writedict('mesa.csv',self.mesas,self.fn)
            
    def mostrar_pedido(self):
        self.exibir()
        mesa = int(input('De qual mesa deseja ver o pedido? '))
        print(f'{azul}Pedido da mesa {mesa}:{branco}',end=' ')
        for i in eval(self.mesas[mesa-1]['Pedido']):
            print(c.cardapio[i]['Nome'],end=', ')
        else:
            print()

class pagamento:
    def __init__(self):
        self.mesas = []
        self.cardápio = []
        self.estoque = []
        self.fn = ["Número","Capacidade","Status","Pessoas","Pedido"]
        with open('mesa.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.mesas.append(i)
        with open("cardápio.csv",encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardápio.append(i)
        with open('estoque.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.estoque.append(i)
                
    def conta_total(self,mesa=-1):
        self.__init__()
        m.exibir()
        if mesa == -1:
            mesa = int(input("Digite a mesa que você deseja a conta: "))
            #mesa = 1
        total = 0
        if self.mesas[mesa-1]['Pedido'] == '[]':
            i = input(f"{vermelho}A mesa não tem conta.{branco} Deseja cadastrar? s/n")
            if i == 's':
                m.pedido(mesa)
                p.conta_total(mesa)
        else:
            for i in eval(self.mesas[mesa-1]['Pedido']):
                fill = '.'
                aling = ">"
                dis = int(len({self.cardápio[int(i)-1]['Nome']}) - 30)
                print(f"{self.cardápio[int(i)-1]['Nome']:.<30}R$ {self.cardápio[int(i)-1]['Preço']:>}")
                total += float(self.cardápio[int(i)-1]['Preço'].replace(',','.'))
            print(f"{'Total:':.<30}{verde}R$ {total:>}{branco}")
            acrescimo = input(r'Deseja adicionar os 10% de serviço? s/n')
            if acrescimo == 's':
                total = round(total*1.1,2)
            print(f"{'Total (Com acréscimo):':.<30}{verde}R$ {total:>}{branco}")
        pagar = input('Deseja pagar a conta? s/n: ')
        if pagar == 's':
            self.pagamento(mesa)

    def pagamento(self,mesa=-1):
        m.exibir()
        if mesa == -1:
            mesa = int(input("Digite a mesa que você deseja pagar a conta: "))
        if self.mesas[mesa-1]['Pedido'] == '[]':
            i = input(f"{vermelho}A mesa não tem conta.{branco} Deseja cadastrar? s/n")
            if i == 's':
                m.pedido(mesa)
            else:
                exit()
        total = 0
        for i in eval(self.mesas[mesa-1]['Pedido']):
            fill = '.'
            aling = ">"
            dis = int(len({self.cardápio[int(i)-1]['Nome']}) - 30)
            total += float(self.cardápio[int(i)-1]['Preço'].replace(',','.'))
        op = input(f"Você deseja dividir a conta no valor de R${verde}{total}{branco} entre as {self.mesas[mesa-1]['Pessoas']} pessoas da mesa {mesa}? s/n: ").lower()
        pessoa = self.mesas[mesa-1]['Pessoas']
        valor_de_cada = (total/int(pessoa))
        if op == 's':
            print(f'Temos {azul}{pessoa}{branco} pessoas na mesa. O valor por pessoa fica R${verde}{valor_de_cada:.2f}{branco}')
            op2 = input('O pagamento vai ser em pix/cartão ou dinheiro? p/d: ')
            if op2 == 'd':
                self.troco(valor_de_cada,mesa,True)
            if op2 == 'p':
                for i in range(self.mesas[mesa-1]['Pessoas']):
                    input(f'Aproxime a maquininha e cobre R${verde}{valor_de_cada:.2f}{branco} da pessoa {azul}{i+1}{branco}. Precione enter quando o pagamento for feito')
        else:
            op2 = input('O pagamento vai ser em pix/cartão ou dinheiro? p/d:')
            if op2 == 'd':
                self.troco(valor_de_cada,mesa,False)
            if op2 == 'p':
                input(f'Aproxime a maquininha e cobre R${verde}{valor_de_cada}{branco} do cliente. Precione enter quando o pagamento for feito')
                    
        self.mesas[mesa-1]['Status'] = 0
        self.mesas[mesa-1]['Pessoas'] = 0
        self.mesas[mesa-1]['Pedido'] = []
        print(f'{verde}Pedido pago com sucesso.{branco}')
        m.livrar(mesa-1,False)
        writedict('mesa.csv',self.mesas,self.fn)
        
    def troco(self,valor,mesa,plural=False):
        if plural == True:
            for i in range(int(self.mesas[mesa-1]['Pessoas'])):
                print(f'Cobre {verde}R${valor}{branco} da pessoa {i+1}.')
                pago = float(input('Quanto foi pago? R$'))
                if pago > valor:
                    print(f'Você deve devolver {verde}R${pago-valor:.2f}{branco} de troco.')
                if pago == valor:
                    print('Você não precisa dar troco.')
                if pago < valor:
                    print(f'{vermelho}O cliente não pagou o suficiente{branco}')
                    print(f'Ele ainda deve pagar {vermelho}R$ {valor - pago}{branco}')
        if plural == False:
            print(f'Cobre {verde}R${valor}{branco} do cliente.')
            pago = float(input('Quanto foi pago? R$'))
            if pago > valor:
                print(f'Você deve devolver {verde}R${valor-pago}{branco} de troco.')
            if pago == valor:
                print('Você não precisa dar troco.')
            if pago < valor:
                print(f'{vermelho}O cliente não pagou o suficiente{branco}')
                print(f'Ele ainda deve pagar {vermelho}R$ {valor - pago}{branco}')

c = cardapio()
m = mesa()
p = pagamento()
if __name__ == '__main__':
    p.pagamento()