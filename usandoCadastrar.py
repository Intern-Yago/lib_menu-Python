"""
Exemplificação dos pacotes, subpacotes e módulos do menuArquivos_py
"""
from menuArquivos_py import cadastrar
from menuArquivos_py import menu
from menuArquivos_py.leiaIntFloat import leiaInt

while True:
    escolha = menu.menu('menu principal', 'Ver pessoas cadastradas', 'Novo Cadastro', 'Sair do programa')
    if escolha == 1:
        menu.titulos('pessoas cadastradas')
        cadastrar.listar()
    elif escolha == 2:
        menu.titulos('Cadastrando...')
        cadastrar.cadastrar(input('Diga o nome: '), leiaInt('Diga a idade: '))
    elif escolha == 3:
        print('\nObrigado por usar o programa\n<<<VOLTE SEMPRE!>>>')
        break
