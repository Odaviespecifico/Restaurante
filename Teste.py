from datetime import date
if __name__ == '__main__':
    validade = '06/04/2025'
    ano,mes,dia = int(validade[6:]),int(validade[3:5]),int(validade[0:2])
    print((date(ano,mes,dia) - date.today()).days)