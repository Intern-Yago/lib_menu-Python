import mysql.connector
from menuArquivos_py import leiaIntFloat


while True:
    user = input('Diga o usuário: ')
    senha = input('Diga a senha: ')
    print('')
    try:
        comeco = mysql.connector.connect(host='localhost',
                            user=user,password=senha)
        banco = mysql.connector.connect(host='localhost',
                            user=user,password=senha)
    except:
        print('ERROR[Coloque as opções corretamente]')
    else:
        break

cursor_comeco = comeco.cursor()
cursor = banco.cursor()

conectado = False
global bd
if banco.is_connected():
    conectado = True
    db_info=banco.get_server_info()
    print('Conectado ao sevidor MySQL versão',db_info)

    def CriarBD(nome_bd):
        global bd
        bd = nome_bd
        try:
            cursor_comeco.execute(f'create database {nome_bd};')
        except:
            print('Erro ao criar o banco')
        else:
            print('Banco criado com sucesso')

    def ListarBancos():
        cursor_comeco.execute('show databases;')
        bancos = cursor_comeco.fetchall()
        print(bancos)
        return bancos

    def conectarBD(banco_de_dados,mensagem=True):
        global bd

        bd = banco_de_dados
        while True:
            try:
                banco.connect(database = bd)
            except Exception as e:
                if e.__str__() == f"1049 (42000): Unknown database '{bd}'":
                    print('Error[Este banco não existe]')
                    while True:
                        escolha = leiaIntFloat.leiaInt(
                            '[ 1 ] - Criar\n[ 2 ] - Ver existentes\n[ 3 ] - Conectar com existente\nOpção: ')
                        if escolha == 2:
                            ListarBancos()
                        elif escolha == 1:
                            CriarBD(bd)
                            break
                        elif escolha == 3:
                            conectarBD(input('Diga o banco que deseja: '),False)
                            break
                        else:
                            print('Escolha errada! Tente novamente')
            else:
                if mensagem:
                    print(f'Conectado ao banco: {bd} com sucesso!')
                    break
                else:
                    break

    def ListarTabelas(mostrar = True):
        global bd
        while True:
            try:
                conectarBD(bd,False)
            except:
                bd = input('Diga o nome do seu banco de dados: ')
            else:
                cursor.execute('show tables;')
                tables = cursor.fetchall()
                if mostrar:
                    print(tables)
                return tables

    def FiltroLinha(tabela, coluna, valor,mostrar='*'):
        global bd
        while True:
            try:
                conectarBD(bd)
            except:
                bd = input('Diga o nome do seu banco de dados: ')
            else:
                cursor.execute(f'select {mostrar} from {tabela} where {coluna} = {valor};')
                linhas = cursor.fetchall()
                print(linhas)
                return linhas

    def ListarRegistros(tabela, filtro=False, mostrar='*'):
        global bd
        while True:
            try:
                conectarBD(bd)
            except:
                bd = input('Diga o nome do seu banco de dados: ')
            else:
                if not filtro:
                    cursor.execute(f'select * from {tabela};')
                    registros = cursor.fetchall()
                    print(registros)
                else:
                   registros = FiltroLinha(tabela, input('Where: '),
                                input('Valores dos registros específicos: '), mostrar)
                return registros

    def CriarRegistros(tabela, inserir=True):
        global dados
        global bd
        global nome_tabela
        nome_tabela = tabela
        while True:
            try:
                conectarBD(bd, False)
            except:
                bd = input('Diga o nome do seu banco de dados: ')
            else:
                while tabela not in ListarTabelas(False):
                    print('\033[31mERROR[Tabela inexistente]\033[m')
                    escolha = leiaIntFloat.leiaInt(
                        '[ 1 ] - Criar\n[ 2 ] - Ver existentes\n[ 3 ] - Conectar com existente'
                        '\nOpção: ')

            col = None
            cont = 0
            lista = []
            while col != 'EXIT':
                col = input('Digite seus registros[EXIT para sair]: ')
                if col != 'EXIT':
                    lista.append(col)
                    lista.append(',')
            for x, c in enumerate(lista):
                if cont == 0:
                    dados = c
                    cont += 1
                elif c == lista[-1]:
                    if x + 1 != len(lista):
                        dados += ', '
                else:
                    dados += c
            break
    def CriarTabelas(tabela):
        global bd
        global dados
        global nome_tabela
        nome_tabela = tabela
        while True:
            try:
                conectarBD(bd, False)
            except:
                bd = input('Diga o nome do seu banco de dados: ')
            else:
                while True:
                    if escolha == 1:
                        CriarTabelas(tabela)
                        break
                    elif escolha == 2:
                        ListarTabelas()
                    elif escolha == 3:
                        tabela = input('Diga sua tabela: ')
                        break
                    else:
                        print('\033[31mERROR[Escolha inválida]')
            col = None
            cont = 0
            lista = []
            while col != 'EXIT':
                col = input('Digite suas colunas[EXIT para sair]: ')
                if col != 'EXIT':
                    lista.append(col)
                    lista.append(',')
            for x, c in enumerate(lista):
                if cont == 0:
                    dados = c
                    cont += 1
                elif c == lista[-1]:
                    if x + 1 != len(lista):
                        dados += ', '
                else:
                    dados += c
            break
        cursor.execute(f"create table {nome_tabela}({dados});")
        cursor.fetchall()

    def ConectarTabela(tabela, mostrar = True):
        global bd
        cont = 0
        while True:
            try:
                if cont == 0:
                    conectarBD(bd)
                else:
                    conectarBD(bd,False)
                tabelas = ListarTabelas(False).__str__()
                if tabela in tabelas:
                    if mostrar:
                        print(f'Conectado com {bd}.{tabela}')
                else:
                    print('\nEsta tabela não existe no seu banco de dados')
                    while True:
                        escolha = leiaIntFloat.leiaInt(
                            '[ 1 ] - Criar\n[ 2 ] - Ver existentes\n[ 3 ] - Conectar com existente\nOpção: ')
                        if escolha == 2:
                            ListarTabelas()
                        elif escolha == 1:
                            CriarTabelas(tabela, False)
                            break
                        elif escolha == 3:
                            ConectarTabela(input('Diga a tabela que deseja: '), False)
                            break
                        else:
                            print('Escolha errada! Tente novamente')
                break
            except Exception as e:
                try:
                    type(bd)
                except:
                    bd = input('Diga o nome do seu banco de dados: ')
                else:
                    cont += 1
        return tabela


else:
    print('BUG FIND!!! CLOSE THE PROGRAM NOW !')