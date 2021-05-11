from CadastroDePessoas.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar novas pessoas
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção para fechar o programa
        cabeçalho('Saindo do sistema... Até logo!', "azul")
        break
    else:
        print(f'{cor("vermelho")}ERRO! Digite uma opção válida{cor("branco")}')
    sleep(1)
