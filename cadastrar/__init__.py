"""
Este pacote especifica que não é ncessário criar um arquivo para ele, pois ele consegue criar um para si mesmo
Seu primeiro passo é a verificação se o arquivo escrito existe, caso não existir, será questionado e se quiser o
resultado será a criação deste arquivo

Aqui é onde ocorrerá o cadastro de cada novo integrante, os quais será adicionados no arquivo.txt com toda formatação  e
a listagem dos integrantes já cadastrados anteriormente

tendo as funções:
°cadastrar(nome='', idade=0, arquivo=manipulandoTXT.nome)
°listar(arquivo=manipulandoTXT.nome)

Bibliotecas usadas:
->manipulandoTXT

!-------------------------!
!OBS:A codificação é utf-8!
! Biblioteca ainda em Beta!
!-------------------------!
"""
print('\033[97;40mEste pacote possue um arquivo padrão para cadastro e a função cadastrar() irá '
      'criar o arquivo caso não exista\033[m')
from menuArquivos_py import manipulandoTXT

nome_arquivo = manipulandoTXT.nome

if manipulandoTXT.nome == 'cadastros.txt':
    manipulandoTXT.verificarExiste(manipulandoTXT.nome, False)


def cadastrar(nome='', idade=0, arquivo=manipulandoTXT.nome):
    """
    -->Função para executar o cadastro da pessoa nome com idade x no arquivo definido anteriormente

    :nome: Nome do integrante a ser cadastrado
    :idade: Idade do integrante
    :arquivo: Arquivo no qual os dados serão adicionados, por padrão receberá o valor que foi dito inicialmente,
    caso não teha sido digitado nenhum arquivo(ou não foi criado), será usado o cadastros.txt
    """
    with open(f'{arquivo}', 'a', encoding='UTF-8') as file:
        try:
            file.writelines(f'{nome.title(): <32}{idade} anos\n')
        except:
            print('\033[31mError[Não conseguimos adicionar o registro]\033[m')
        else:
            print('Registro adicionado com sucesso!')


def listar(arquivo=manipulandoTXT.nome):
    """
    -->A função listar executa a listagem/amostragem dos cadastros realizados no arquivo definido anteriomente
    Caso não tenha sido definido o arquivo será cadastros.txt

    :param arquivo: Arquivo no qual será mostrado os cadastros
    """
    manipulandoTXT.verificarExiste(arquivo)
    with open(f'{arquivo}', 'r', encoding='UTF-8') as leitor:
        print(leitor.read())
