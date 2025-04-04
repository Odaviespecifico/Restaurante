import csv
import datetime

class estoque:
    def __init__(self):
        self.estoque = "estoque.csv"
        
    def consultar():
        with open(r"C:\Users\Davi\Documents\Progamação\Restaurante\Desafio 01\estoque.csv","r",encoding="UTF-8") as estoque:
            leitor = csv.reader(estoque,delimiter=";") #lê as linhas do estoque
            for linha in leitor:
                # try:
                #     linha[1]
                #     continue
                # except:
                #     pass
                #Código; nome; quantidade; unidade de medida; preço unitário; validade
                #print(linha)
                cod, nome, quantidade, unidade, preço, validade = linha[0],linha[1],linha[2],linha[3],linha[4],linha[5]
                print('-'*10)
                print(f'Código do item: {cod}')
                print(f'Nome do item:{nome}')
                print(f'Quantidade:{quantidade}{unidade}')
                print(f'preço: R${preço}')
                print(f'Validade:{validade}')
            else:
                print('-'*10)
    def cadastrar():
        
        print("Cadastrar produto")
        cod = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ") 
        quantidade = input("Digite a quantidade do produto: ")
        unidade = input("Digite a unidade de medida do produto: ")
        preço = input("Digite o preço do produto: ")
        validade = input("Digite a validade do produto: ")
        with open(r"Desafio 01\estoque.csv","a",encoding="UTF-8",newline="") as estoque:
            escrever = csv.writer(estoque,delimiter=";")
            # escrever.writerow([cod,nome,quantidade,unidade,preço,validade])
            # escrever.writerow('')
            #estoque.write('\n')
            escrever.writerow([cod,nome,quantidade,unidade,preço,validade])
    


#print(estoque.consultar())
estoque.cadastrar()