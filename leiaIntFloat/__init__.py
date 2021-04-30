"""
Este pacote será apenas a verificação se a mensagem passada um número inteiro ou quebrado
Tendo as funções:
°leiaInt(msg)
°leiaFloat(msg)
"""


def leiaInt(msg, pergunta=True):
    """
    -->Verificação de inteiro e retorno do valor convertido

    :msg: Número que sofrerá a verificação de inteiro
    :return: Caso o msg seja inteiro, será retornado ele já convertido, caso tenha tido erro de interrupção pelo usuário
            será retornado como 0
    """
    global acerto
    if pergunta==True:
        while True:
            n = input(msg).replace(' ', '')
            try:
                n = int(n)
            except Exception:
                print(f'\033[31mERROR["{n}" não é um real]\nPor favor digite um número válido\033[m')
            else:
                acerto=1
                return n
    else:
        n=msg
        try:
            n = int(n)
        except Exception:
            print(f'\033[31mERROR["{n}" não é um real]\nPor favor digite um número válido\033[m')
        else:
            acerto=1
            return n

def leiaFloat(msg):
    """
    -->Verificação de float e retorno do valor convertido

    :msg: Número que sofrerá a verificação de real
    :return: Caso o msg seja quebrado, será retornado ele já convertido, caso tenha tido erro de interrupção pelo usuário
            será retornado como 0
    """
    while True:
        r = input(msg).replace(' ', '')
        try:
            r = float(r)
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar')
            return 0
        except Exception:
            print(f'\033[31mERROR["{r}" não é um real]\nPor favor digite um número válido\033[m')
            continue
        else:
            return r
