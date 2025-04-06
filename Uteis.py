cores = {'azul': '\033[34m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'rosa': '\033[35m', 'branco': '\033[37m'}
def print_ornamentado(texto):
    print(f"{cores['azul']}")
    print("-"*len(texto))
    print(texto)
    print("-"*len(texto))
    print(f"{cores['branco']}")

opções_geral = """Opções:
\033[35m1\033[37m - Estoque
\033[35m2\033[37m - Cozinha
\033[35m3\033[37m - Pedidos
\033[35m4\033[37m - Pagamento
\033[35m5\033[37m - sair"""

opções_estoque = """Opções:
\033[35m1\033[37m - Consultar estoque
\033[35m2\033[37m - Cadastrar produto
\033[35m3\033[37m - atualizar produto
\033[35m4\033[37m - Remover produto
\033[35m5\033[37m - sair"""