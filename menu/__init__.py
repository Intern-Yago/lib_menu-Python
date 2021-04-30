"""
Este pacote irá servir para a criação do menu com as opções que desejar e também fornecerá uma formatação para títulos

!----------------------------------------------------------------------------------------------------------------------!
! Após coletar os dados em menu, serão adicionados em uma lista na qual cada valor será printado com seu respectivo    !
! número.                                                                                                              !
! Usando a importação do módulo leiaIntFloat é possível captar se a opção digitada pelo usuário é válida,              !
! sendo realmente um número inteiro e com algumas funções é possível ver se a escolha feita está dentro ou             !
! não das opções que esteja dentro das opções.                                                                         !
!----------------------------------------------------------------------------------------------------------------------!

Caso de dúvida utilize help(leiaIntFloat)
Bibliotecas usadas:leiaIntFloat
"""
from menuArquivos_py import leiaIntFloat

def linha(quantidade=42):
    """
    Está função apenas serve para fornecer o print de linhas com a quantidade usada no programa
    """
    leiaIntFloat.leiaInt(quantidade, False)
    try:
        if leiaIntFloat.acerto == 1:
            global quantos
            quantos = quantidade
            print('-'*quantidade)
    except:
        pass
def titulos(msg, maiusculo = True):
    """
    :msg: Mensagem que passará por uma formatação e se tornará um "título"
    Ganhará linhas, ficará centralizado e terá sua estrutura atualizada para ficar em maiúscula
    :maiusculo: titulo em maiúsculo ou não
    :return: Não possue retorno apenas será printado a imagem com tal formato

    Está função centralizará a msg com as 42 linhas printadas
    """
    if maiusculo == True:
        mensagem = str(msg).upper()
        print('-' * 42)
        print(f'{mensagem}'.center(42))
        print('-' * 42)
    else:
        mensagem = str(msg)
        print('-' * 42)
        print(f'{mensagem}'.center(42))
        print('-' * 42)


def menu(msg, *lst):
    """
    menu(msg, *lst)
    -->Está função irá "desenha" o seu menu com as opções dadas

    :msg: Texto que irá passar pelo processo de formatar para título
    :*lst: Desempacotamento de dados que serão adicionados em uma lista para se tornarem nas futuras opções do menu
    :return:Será retornado a opção que o usuário escolheu

    Irá usar o módulo leiaIntFloat para verificar se realmente é um número inteiro e também irá ver se
    a escolha feita se encaixa na quantidade de opções
    """
    titulos(msg)
    lista = []
    for i, p in enumerate(lst):
        lista.append(p)
    for c, item in enumerate(lista):
        print(f'\033[93m{c + 1} -\033[m \033[34m{item}\033[m')
    print('-' * 42)
    escolha = leiaIntFloat.leiaInt('\033[92;1mOpção:\033[m ')
    print('')
    if escolha < 1 or escolha > len(lista):
        print('\033[31mERROR[Está opção não existe]\033[m')
    return escolha
