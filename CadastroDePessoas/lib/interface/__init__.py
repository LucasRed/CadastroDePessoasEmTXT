def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print(f'{cor("vermelho")}Houve um erro de tipo, por favor digite um valor Inteiro!{cor("branco")}')
        except Exception as erro:
            print(f'{cor("vermelho")}Houve um erro de {erro}, por favor digite um valor Inteiro!{cor("branco")}')


def cor(escolha):
    c = {'branco': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
    return c[escolha]


def linha(tam=42, c="roxo"):
    return f'{cor(c)}-{cor("branco")}' * tam


def cabeçalho(txt, c='branco'):
    print(linha())
    print(f'{cor(c)}{txt.center(42)}{cor("branco")}')
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL', 'azul')
    c = 1
    for item in lista:
        print(f'{cor("verde")}{c} - {cor("ciano")}{item}{cor("branco")}')
        c += 1
    print(linha())
    opc = leiaInt(f'{cor("amarelo")}Sua opção: {cor("branco")}')
    return opc
