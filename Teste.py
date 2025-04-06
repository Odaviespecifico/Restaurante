import csv
itens = []
with open('estoque.csv',encoding='UTF-8') as estoque:
    for row in csv.DictReader(estoque,delimiter=';'):
        itens.append(row)
print(itens)