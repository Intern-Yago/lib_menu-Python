"""
Aqui será tratado apenas a manipulação de arquivos .txt
tendo apenas duas funções:
°criarArquivos(name) - Para a criação do arquivo digitado
°verificarExiste(name,perguntar=False) - Para a verificação da existência do arquivo no atua diretório

Quando importado ele imprime uma pergunta com o objetivo de saber qual arquivo desejas,
mas caso não queira criar um arquivo, o programa irá criar seu próprio arquivo chamado cadastros.txt
"""


def criarArquivo(name):
    """
    --> Criação do arquivo name no atual diretório

    :name: Nome do arquivo a ser criado
    :return: Retorna verdadeiro para caso consiga criar o arquivo, se não conseguir,
            será printado um except e o booleano False
    """
    name += '.txt'
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print(f'ERROR[Erro na criação do arquivo {name}]')
        return False
    else:
        print('Arquivo criado com sucesso')
        return True


def verificarExiste(name, perguntar=True):
    """
    -->Terá a verificação se o arquivo existe ou não neste diretório

    :name: Nome do arquivo que deseja fazer a verificação se existe ou não
    :perguntar: Caso não queria que o programa te pergunte se você deseja ou não criar, apenas coloque como falso
                Se ele não encontrar o arquivo, com o valor False o programa apenas criará sem a confirmação do usuário
    :return: Especifico para quando não se possue valor especificado e terá de usar o arquivo padrão "cadastros.txt"
    """
    try:
        a = open(name, 'rt')
        a.close()
    except (FileNotFoundError, FileExistsError):
        print(f'\033[31mO arquivo {name} não existe ou não foi encontrado\033[m')
        if perguntar:
            solicitar = input('Deseja criar?[S/N] ')[0].lower()
            while True:
                if solicitar == 'n':
                    while True:
                        print('\033[31;107mNÃO CRIAR ESTE ARQUIVO PODERÁ DAR FALHAS EM SUA PROGRAMAÇÃO\033[m')
                        sol = input('Tem certeza que não deseja criar?[S/N] ')[0].lower()
                        if sol == 's':
                            return False
                        elif sol == 'n':
                            print('Ok, então iremos criar')
                            criarArquivo(name)
                            return name

                elif solicitar == 's':
                    criarArquivo(name)
                    break
                else:
                    print('\033[31mERROR[Opção inválida]\033[m')
        else:
            criarArquivo(name)

    else:
        return name

"""nome = input('Diga o nome do arquivo: ')
sn = verificarExiste(nome)
if not sn:
    nome = 'cadastros.txt'"""
