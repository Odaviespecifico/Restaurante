import datetime
from Uteis import *
import csv
import random
editar = False

class estoque:
    def __init__(self):
        with open('estoque.csv',encoding='UTF-8') as estoque:
            self.itens_estoque = [] # Lista para armazenar o conteúdo do estoque
            for row in csv.DictReader(estoque,delimiter=';'):
                self.itens_estoque.append(row)
        self.fn = ('Código','Nome','Quantidade','Unidade','Preço','Validade','Quantidade mínima')
    def consultar(self):
        global editar
        if editar != True:
            print_ornamentado('Itens no estoque')
        for i in self.itens_estoque:
            mostrar_item(i)
        else:
                print('-'*20)
        self.mostrar_validade()
        self.estoque_baixo()

    def mostrar_validade(self):
        vencidos = False
        for i in self.itens_estoque:
            validade = i['Validade']
            ano,dia,mes = int(validade[6:]),int(validade[0:2]),int(validade[3:5])
            diferenca = (date(ano,mes,dia) - date.today()).days
            if diferenca < 0:
                print(f"{i['Nome']} {vermelho}venceu{branco}. A fiscalização pega!")
                vencidos = True
            elif diferenca <= 7:
                print(f"{i['Nome']} está {amarelo}perto de vencer{branco}. Tenha atenção!")
                vencidos = True
        else:
            if vencidos == False:
                print('Nenhum item crítico de validade. A fiscalização te ama ❤️')
            print('-'*20)
    
    def estoque_baixo(self):
        for i in self.itens_estoque:
            if float(i['Quantidade']) > float(i['Quantidade mínima']):
                pass
            elif float(i['Quantidade']) <= float(i['Quantidade mínima']):
                print(f"Quantidade baixa de {vermelho}{i['Nome']}{branco}. Você tem {azul}{i['Quantidade']} {i['Unidade']}{branco} e seu ponto crítico é {azul}{i['Quantidade mínima']} {i['Unidade']}{branco}")
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
        q_minima = input(f'Digite a quantidade mínima do item: (Não esqueça que a unidade é {unidade})')
        item = {"Código":cod,"Nome":nome,"Quantidade":quantidade,"Unidade":unidade,"Preço":preco,"Validade":validade,'Quantidade mínima':q_minima}
        self.itens_estoque.append(item)
        mostrar_item(item)
        print(verde,'Produto cadastrado com sucesso!',branco)
        writedict("estoque.csv",self.itens_estoque,self.fn)

    def editar(self):
        global editar
        editar = True
        print_ornamentado('Alterar produto')
        self.consultar()
        Escolha = input('Digite o código ou nome do item que deseja editar: ').capitalize()
        posicao = 0
        for i in self.itens_estoque:
            # print(i)
            if i["Código"] == Escolha or i["Nome"] == Escolha:
                mostrar_item(i,True)
                while True:
                    escolha = input(f"{rosa}Qual parte você quer editar? {branco}")
                    match escolha:
                        case "1":
                            self.itens_estoque[posicao]['Código'] = input("Digite o novo código do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case "2":
                            self.itens_estoque[posicao]['Nome'] = input("Digite o novo nome do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case "3":
                            self.itens_estoque[posicao]['Quantidade'] = input("Digite a nova quantidade do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case "4":
                            self.itens_estoque[posicao]['Unidade'] = input("Digite a nova unidade do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case "5":
                            self.itens_estoque[posicao]['Preço'] = input("Digite o novo preço do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case "6":
                            self.itens_estoque[posicao]['Validade'] = input("Digite a nova validade do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case "7":
                            self.itens_estoque[posicao]['Quantidade mínima'] = input("Digite a nova quantidade mínima do produto: ")
                            editou(self.itens_estoque[posicao])
                            break
                        case _:
                            print(f'{vermelho}Opção inválida!{branco}')
                            break
                break
            posicao += 1
        else:
            if posicao == 0:
                print(f'{vermelho}Item não encontrado!{branco}')
            if posicao > 0:
                print(f'{vermelho}Item não encontrado! Talvez você esteja colocando o nome todo em minúsculo!{branco}')

        writedict("estoque.csv",self.itens_estoque,self.fn)
        
    def remover(self):
        print_ornamentado('Remover produto')
        global editar
        editar = True
        self.consultar()
        Escolha = input('Digite o código ou nome do item que deseja remover: ')
        posição = 0
        for i in self.itens_estoque:
            if i["Código"] == Escolha or i["Nome"] == Escolha:
                mostrar_item(i)
                confirma = input(f'{vermelho}Você tem certeza que deseja remover o item {i["Nome"]}?\nDigite "s" para sim ou "n" para não: {branco}')
                if confirma == 's':
                    self.itens_estoque.pop(posição)
                    print(f'{vermelho}Produto removido com sucesso!{branco}')
                else:
                    print(f'{verde}Produto não removido!{branco}')
                    break
                break
            posição += 1
        else:
            print(f'{vermelho}Item não encontrado, talvez você esteja colocando o nome minúsculo!{branco}')

        writedict("estoque.csv",self.itens_estoque,self.fn)
                        
class cardapio:
    def __init__(self):
        self.cardapio = [] # O nosso cardápio
        self.estoque = [] # O nosso estoque
        with open("cardapio.csv",encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardapio.append(i)
        with open('estoque.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.estoque.append(i)
        
        self.fn = ('Nome','Preço','Descrição','Ingredientes') # Fieldnames do item
    
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
    
    def cadastrar(self): # Cadastro de produto
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
                self.cardapio.append({'Nome': nome, 'Preço': preço, 'Descrição': descrição, "Ingredientes": ingredientes})
                writedict("cardapio.csv",self.cardapio,self.fn)
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
        writedict("cardapio.csv",self.cardapio,self.fn)
    
    def remover(self):
        self.consultar()
        escolha = int(input("Digite o número do item que deseja remover: "))
        escolha2 = input(f"{vermelho}Tem certeza que deseja remover {self.cardapio[escolha-1]['Nome']}? (s/n): ")
        if escolha2 == 's':
            self.cardapio.pop(escolha-1)
            writedict("cardapio.csv",self.cardapio,self.fn)
            print(f"Item removido com sucesso!{branco}")
            self.consultar()
        else:
            print(f'{verde}Item não removido!')
            self.consultar()

class mesa:
    def __init__(self):
        self.mesas = []
        with open('mesa.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.mesas.append(i)
        self.fn = ('Número','Capacidade','Status','Pessoas','Pedido')

        self.pedidos = [] # Nossos pedidos. Armazenados de acordo com o self.fnp
        with open('pedido.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.pedidos.append(i)
        self.fnp = ('Mesa','Horário','Status','Itens') # Fieldnames do pedido
        
        self.estoque = []
        with open('estoque.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.estoque.append(i)
        self.fn_estoque = ('Código','Nome','Quantidade','Unidade','Preço','Validade','Quantidade mínima')
        self.cardapio = []
        with open('cardapio.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardapio.append(i)
        # Status -> 0 = Registrado | 1 = Fazendo | 2 = Feito
        
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

    def cadastrar(self):
        self.exibir(editar=True)
        print_ornamentado('Cadastrar mesa')
        numero = input("Digite o número da mesa: ")
        capacidade = input("Digite a capacidade da mesa: ")
        item = {"Número": numero,"Capacidade": capacidade,"Status": 0,"Pessoas": 0}
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
        m.apagar_pedido(mesa)
        writedict("mesa.csv",self.mesas,self.fn)
        print(f'{verde}Mesa {mesa+1} liberada com sucesso!{branco}')

    def ocupar(self,mesa='False'):
        self.exibir(editar=True)
        print_ornamentado('Adicionar clientes à mesa')
        while True: # Loop para definir o número da mesa e quantidade de pessoas
            if mesa == 'False':    
                mesa = int(input("Digite o número da mesa que deseja ocupar: "))
            if self.mesas[mesa-1]['Status'] == '2':
                print(f'{vermelho}A mesa {mesa} está ocupada, escolha outra!{branco}')
                continue
            if self.mesas[mesa-1]['Status'] == '1':
                print(f'{vermelho}A mesa {mesa} está reservada,{branco}',end=" ")
                escolha = input('Deseja alocar o cliente mesmo assim? (s/n): ')
                if escolha != 's':
                    continue
            pessoas = int(input(f"Digite o número de pessoas que deseja colocar na mesa {mesa}: "))
            if pessoas > int(self.mesas[int(mesa)-1]['Capacidade']):
                    print(f'{vermelho}A quantidade de pessoas é maior do que a capacidade da mesa. Talvez você consiga cadastrar em duas mesas!{branco}')
            else:
                break
        escolha = input('Você deseja fazer uma reserva ou ocupar a mesa? (r/o): ')
        if escolha == 'r':
            self.mesas[mesa-1]['Status'] = 1
        else:
            self.mesas[mesa-1]['Status'] = 2
        self.mesas[mesa-1]['Pessoas'] = pessoas
        writedict("mesa.csv",self.mesas,self.fn)
        print(f'{verde}Mesa {mesa} ocupada com sucesso!{branco}')
        self.exibir(editar=True)

    def pedido(self,mesa=-1,exibir=True):
        if exibir:
            self.exibir()
        if mesa == -1:
            escolha = int(input('De qual mesa é o pedido? '))
        else:
            escolha = mesa

        if self.mesas[escolha-1]['Status'] == '0': # Quando a mesa está sem clientes
            op = input(f'A mesa {azul}{escolha}{branco} não tem clientes cadastrados, deseja adicionar um cliente? (s/n): ')
            if op == 's':
                self.ocupar(escolha)
            else:
                c.consultar()
                pass
        if self.pedidos == []: # Verifica se é o primeiro pedido
            print('Primeiro pedido do dia!')
            self.pedidos.append({'Mesa': escolha-1,'Horário': datetime.datetime.now(),'Status': 'Registrado','Itens': []})
        else:
            self.pedidos.append({'Mesa': escolha-1,'Horário': datetime.datetime.now(),'Status': 'Registrado','Itens': []})
        c.consultar()
        pedidos = []
        pedido = 1
        
        while True: # Loop de adicionar pedido
            pedido = input('Digite o pedido da mesa, sendo um item por vez. Ao final, digite 0 para parar: ')
            if pedido == '0':
                break
            
            # Verificar se o item está presente no estoque
            ingredientes = eval(self.cardapio[int(pedido)-1]['Ingredientes'])  # Obtém os ingredientes do item do cardápio
            itens_remover = []  # Lista para armazenar os itens que serão removidos do estoque
            suficiente = True  # Variável para verificar se todos os ingredientes estão disponíveis
            
            for ingrediente in ingredientes:
                # Verifica se o ingrediente está presente no cardápio
                if ingrediente[0].upper() in self.cardapio[int(pedido)-1]['Ingredientes'].upper():
                    for i in self.estoque:
                        if i['Nome'] == ingrediente[0]:  # Verifica se o ingrediente está no estoque
                            # Verifica se a quantidade disponível no estoque é suficiente
                            if float(i['Quantidade']) < float(ingrediente[1].replace(',', '.')):
                                print(f'{vermelho}Não temos {ingrediente[0]} suficiente no estoque!{branco}')
                                suficiente = False  # Marca que não há ingredientes suficientes
                            else:
                                # Atualiza a quantidade do ingrediente no estoque
                                i['Quantidade'] = str(round(float(i['Quantidade']) - float(ingrediente[1].replace(',', '.'))))
                                itens_remover.append(i)  # Adiciona o item atualizado à lista de itens a serem removidos
            # Atualiza o estoque com os itens removidos
            
            if suficiente == True: # Se temos todos os ingredientes
                for i in itens_remover: # Loop para remover os itens
                    for j in self.estoque:
                        if i['Nome'] == j['Nome']:
                            self.estoque[self.estoque.index(j)] = i
                writedict('estoque.csv', self.estoque, self.fn_estoque)  # Salva as alterações no arquivo de estoque
                pedidos.append(int(pedido)-1)  # Adiciona o pedido à lista de pedidos
                print(f'{azul}Pedido da mesa {escolha}:{branco}', end=' ')
                for i in range(len(pedidos)):
                    # Exibe os nomes dos itens do pedido
                    print(f"{c.cardapio[int(pedidos[i-1])]['Nome']}", end=', ')
                else:
                    print()
                    
                # Atualiza o pedido da mesa e o registro de pedidos
                self.mesas[escolha-1]['Pedido'] = pedidos
                self.pedidos[-1]['Itens'] = pedidos
                writedict('mesa.csv', self.mesas, self.fn)  # Salva as alterações no arquivo de mesas
        writedict('pedido.csv', self.pedidos, self.fnp)  # Salva as alterações no arquivo de pedidos

    def mostrar_pedido(self,mesa=-1):
        if mesa == -1:
            self.exibir()
            mesa = int(input('De qual mesa você deseja ver o pedido? '))
        print(f'{azul}Pedido da mesa {mesa}:{branco}',end=' ')
        
        for i in eval(self.mesas[mesa-1]['Pedido']):
            print(c.cardapio[i]['Nome'],end=', ')
        else:
            print()

    def fila_de_pedidos(self):
        print_ornamentado('Fila de pedidos: ')
        for i in self.pedidos:
            print(azul,end='')
            print('-'*20)
            print(branco,end='')
            print(f'{rosa}Número de pedido{branco}: {self.pedidos.index(i)+1}')
            print(f"{rosa}Pedido da mesa{branco} {verde}{int(i['Mesa'])+1}{branco}")
            print(f'{rosa}Itens do pedido: {branco}',end='')
            for j in eval(self.mesas[int(i['Mesa'])]['Pedido']):
                print(c.cardapio[j]['Nome'],end=', ')
            else:
                print()
            print(f"{rosa}Status do pedido: {branco} {i['Status']}")
            print(f"{rosa}Dia e hora do pedido: {branco}{i['Horário'][:-7]}")
        else:
            print(azul,end='')
            print('-'*20)
            print(branco,end='')

    def status_pedido(self,mesa):
        while True:
            try:
                status = int(input("""Status: 
1 - Registrado
2 - Em preparo
3 - Concluído
4 - Entregue
Qual status deseja colocar? """))
                break
            except ValueError:
                print(f'{vermelho}Opção inválida!{branco}')
        match status:
            case 1:
                status = 'Registrado'
            case 2:
                status = 'Em preparo'
            case 3:
                status = 'Concluído'
            case 4:
                status = 'Entregue'
        self.pedidos[mesa-1]['Status'] = status
    
    def apagar_pedido(self,mesa=float('inf'),index=False): # Apaga o pedido da mesa pelo número da mesa (Do restaurante, não da lista)
        if index:
            pedido_apagar = int(input('Qual o número do pedido que você deseja apagar? '))
            self.pedidos.pop(pedido_apagar-1)
        if mesa == float('inf') and index == False:
            print(mesa)
            mesa = int(input('Digite o número da mesa que deseja apagar o pedido: '))-1
        
        for pedido in self.pedidos:
            if int(pedido['Mesa']) == int(mesa)-1:
                self.pedidos.pop(self.pedidos.index(pedido))
                writedict('pedido.csv',self.pedidos,self.fnp)
        return self.pedidos

class pagamento:
    def __init__(self):
        self.mesas = []
        self.cardapio = []
        self.estoque = []
        self.pedidos = []
        self.pagamentos = []
        self.pago = False
        self.fn = ["Número","Capacidade","Status","Pessoas","Pedido"]
        self.fnp = ('Mesa','Horário','Status','Itens')
        self.fn_pagamentos = ('Mesa','Horário','Itens','Valor','Meio')
        with open('mesa.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.mesas.append(i)
        with open("cardapio.csv",encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardapio.append(i)
        with open('estoque.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.estoque.append(i)
        with open('pedido.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.pedidos.append(i)
        with open('pagamentos.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.pagamentos.append(i)
    def conta_total(self,mesa=-1,firstpass=True):
        self.__init__()
        m.exibir()
        if mesa == -1:
            mesa = int(input("Digite a mesa que você deseja pedir a conta: "))
            #mesa = 1
        total = 0
        
        if self.mesas[mesa-1]['Pedido'] == '[]':
            i = input(f"{vermelho}A mesa não tem conta em aberto.{branco} Deseja cadastrar? (s/n): ")
            if i == 's':
                m.pedido(mesa)
                p.conta_total(mesa,False)
        else:
            for i in eval(self.mesas[mesa-1]['Pedido']):
                fill = '.'
                align = ">"
                dis = int(len({self.cardapio[int(i)-1]['Nome']}) - 30)
                print(f"{self.cardapio[int(i)-1]['Nome']:.<30}R$ {self.cardapio[int(i)-1]['Preço']:>}")
                total += float(self.cardapio[int(i)-1]['Preço'].replace(',','.'))
            print(f"{'Total:':.<30}{verde}R$ {total:>.2f}{branco}") 
            acrescimo = input(r'Deseja adicionar os 10% de serviço? (s/n): ')
            if acrescimo == 's':
                total = round(total*1.1,2)
            print(f"{'Total (Com acréscimo):':.<30}{verde}R$ {total:>.2f}{branco}") 
        if not self.pago:
            pagar = input('Deseja pagar a conta? (s/n): ')
            if pagar == 's':
                self.pagamento(mesa)


    def pagamento(self,mesa=-1):
        m.exibir()
        if mesa == -1:
            mesa = int(input("Digite a mesa que você deseja pagar a conta: "))
        if self.mesas[mesa-1]['Pedido'] == '[]':
            i = input(f"{vermelho}A mesa não tem conta em aberto.{branco} Deseja cadastrar? (s/n): ")
            if i == 's':
                m.pedido(mesa)
            else:
                exit()
        total = 0
        for i in eval(self.mesas[mesa-1]['Pedido']):
            fill = '.'
            align = ">"
            dis = int(len({self.cardapio[int(i)-1]['Nome']}) - 30)
            total += float(self.cardapio[int(i)-1]['Preço'].replace(',','.'))
        op = input(f"Você deseja dividir a conta no valor de R${verde}{total:.2f}{branco} entre as {self.mesas[mesa-1]['Pessoas']} pessoas da mesa {mesa}? (s/n): ").lower()
        pessoa = self.mesas[mesa-1]['Pessoas']
        valor_de_cada = (total/int(pessoa))
        if op == 's':
            print(f'Temos {azul}{pessoa}{branco} pessoas na mesa. O valor por pessoa fica R${verde}{valor_de_cada:.2f}{branco}')
            op2 = input('O pagamento vai ser em dinheiro ou pix/cartão? (d/c): ')
            if op2 == 'd':
                self.troco(valor_de_cada,mesa,True)
                meio = 'Dinheiro/pix'
            if op2 == 'c':
                for i in range(int(self.mesas[mesa-1]['Pessoas'])):
                    input(f'Aproxime a maquininha e cobre R${verde}{valor_de_cada:.2f}{branco} da pessoa {azul}{i+1}{branco}. Pressione enter quando o pagamento for feito. ')
                meio = 'Cartão'
        else:
            op2 = input('O pagamento vai ser em dinheiro ou pix/cartão? (d/c): ')
            if op2 == 'd': # Opção pagamento em dinheiro/pix
                self.troco(total,mesa,False)
                meio = 'Dinheiro/pix'
            if op2 == 'c': # Opção pagamento em cartão
                input(f'Aproxime a maquininha e cobre R${verde}{total:.2f}{branco} do cliente. Pressione enter quando o pagamento for feito. ')
                meio = 'Cartão'
        for pedido in self.pedidos:
            if int(pedido['Mesa']) == int(mesa)-1:
                self.pagamentos.append({'Mesa':pedido['Mesa'],'Horário':pedido['Horário'],'Itens':pedido['Itens'],'Valor':total,'Meio':meio})
                self.pagamentos[-1]['Valor'] = total
        writedict('pagamentos.csv',self.pagamentos,self.fn_pagamentos)
        self.mesas[mesa-1]['Status'] = 0
        self.mesas[mesa-1]['Pessoas'] = 0
        self.mesas[mesa-1]['Pedido'] = []
        self.pedidos = m.apagar_pedido(mesa)
        self.pago = True
        print(f'{verde}Pedido pago com sucesso!{branco}')
        m.livrar(mesa-1,False)
        writedict('mesa.csv',self.mesas,self.fn)
        writedict('pedido.csv',self.pedidos,self.fnp)
        
    def troco(self,valor,mesa,plural=False):
        if plural == True:
            for i in range(int(self.mesas[mesa-1]['Pessoas'])):
                print(f'Cobre {verde}R${valor:.2f}{branco} da pessoa {i+1}.')
                pago = float(input('Quanto foi pago? R$'))
                if pago > valor:
                    print(f'Você deve devolver {verde}R${(pago-valor):.2f}{branco} de troco.')
                if pago == valor:
                    print('Você não precisa dar troco.')
                if pago < valor:
                    print(f'{vermelho}O cliente não pagou o suficiente!{branco}')
                    print(f'Falta pagar {vermelho}R$ {(valor - pago):.2f}{branco}')
        if plural == False:
            print(f'Cobre {verde}R${valor:.2f}{branco} do cliente.')
            pago = float(input('Quanto foi pago? R$'))
            if pago > valor:
                print(f'Você deve devolver {verde}R${(valor - pago):.2f}{branco} de troco.')
            if pago == valor:
                print('Você não precisa dar troco.')
            if pago < valor:
                print(f'{vermelho}O cliente não pagou o suficiente{branco}')
                print(f'Ele ainda deve pagar {vermelho}R$ {(valor - pago):.2f}{branco}')

class relatorio:
    def __init__(self):
        self.pagamentos = []
        with open('pagamentos.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.pagamentos.append(i)
        self.cardapio = []
        with open('cardapio.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.cardapio.append(i)
        self.mesas = []
        with open('mesa.csv',encoding='UTF-8') as items:
            for i in csv.DictReader(items,delimiter=';'):
                self.mesas.append(i)

    def total(self,mostrar=True):
        self.Vendas = 0
        self.Valor_total = 0.0
        for pagamento in self.pagamentos:
            self.Vendas += 1
            self.Valor_total += float(pagamento['Valor'])
        if mostrar == True:
            print_ornamentado('Relatório de vendas')
            print(f"Foram feitas {self.Vendas} vendas hoje. O valor total arrecadado foi de R${verde}{self.Valor_total:.2f}{branco}")
        media_mesa = round(self.Valor_total/len(self.mesas),2)
        print(f"A média de valor dentre as {azul}{len(self.mesas)}{branco} mesas foi de R${verde}{self.Valor_total/len(self.mesas):.2f}{branco}")
        return self.Vendas,self.Valor_total
        
    def mais_vendidos(self):
        print_ornamentado('Mais vendidos')
        vendidos = []

        # Ler todos os itens dos pedidos e colocar todos em uma lista
        for pedidos in self.pagamentos:
            for i in eval(pedidos['Itens']):
                vendidos.append(i) 

        # Contar os valores individuais da lista para gerar uma lista com tuplas de pares Valor
        itens = set(vendidos) # Tranformar em conjunto para pegar os itens individuais
        vendidos_ordenado = []
        for i in itens: 
            vendidos_ordenado.append((i,vendidos.count(i))) # Coloca em vendidos uma tupla para cada item com ele e sua quantidade
        vendidos_ordenado.sort(key=lambda x: x[1],reverse=True)

        # Verificar cada primeiro item das tuplas e associar com o cardápio
        for i in vendidos_ordenado:
            item_atual = self.cardapio[i[0]-1]
            print(f"{item_atual['Nome']}: {i[1]} vendidos")
            print(f"Valor total: {verde}{i[1]*float(item_atual['Preço'].replace(',','.')):.2f}{branco}")
        

e = estoque()
c = cardapio()
m = mesa()
p = pagamento()
r = relatorio()

if __name__ == "__main__":
    r.mais_vendidos()
    pass