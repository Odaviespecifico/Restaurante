import csv
import datetime

class estoque:
    def __init__(self):
        self.estoque = "estoque.csv"
        
    def consultar():
        with open(r"C:\Users\UniFafire015\Documents\Davi Wanderley\python-basics\python-basics\Classes\Desafio 01\estoque.csv","r",encoding="UTF-8") as estoque:
            leitor = csv.reader(estoque,delimiter=";") #lê as linhas do estoque
            for linha in leitor:
                print(linha[])
                


print(estoque.consultar())