#Deposito: todos os depósitos devem ser armazenados em uma variavel e exibidos no
#extrato

#Saque: permitir 3 saques diarios com limite de 500,00 por saque;
#se não tiver saldo informar o usuario;
#Todos os saques devem ser armazenados em uma variavel e exibidos no extrato

#Extrato: deve listar todos os depositos e saques;
#no fim da listagem exibir o saldo atual
#se estiver em branco exibir: Não foram realizadas movimentações.
#os valores devem ser exibidos R$ 1000.00


import datetime

menu = """
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
"""


saldo = 0
limite = float(500)
extratos_bancarios = {
    "Extrato de Deposito":[],
    "Extrato de Saques":[],
    "Extrato Geral":[]
}
numeros_saques = 0
LIMITE_SAQUES= 3
data =  datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S') #DATA atual e hora

while True:
    opcao = input(menu)

    if opcao.upper() == 'D':
        valor_deposito = float(input('Valor de deposito: R$ '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extratos_bancarios['Extrato de Deposito'].append(f'Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}')
            extratos_bancarios['Extrato Geral'].append(f'Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}')
        else:
            print('Você deve depositar acima de R$ 0')

    elif opcao.upper() == 'S':
        if numeros_saques < LIMITE_SAQUES:
            
            valor_saque = float(input('Valor de saque: R$ '))
            if valor_saque > 0:
                if valor_saque <= limite and valor_saque <= saldo:
                    extratos_bancarios['Extrato de Saques'].append(f'Data: {str(data)} - Saque: R$ {valor_saque:.2f}')
                    extratos_bancarios['Extrato Geral'].append(f'Data: {str(data)} - Saque: R$ {valor_saque:.2f}')
                    print('Saque Realizado com Sucesso!')
                    numeros_saques+=1
                else:
                    print(f'O limite de saque é de {limite:.2f}')
            else:
                print('Você deve informar um valor de saque valido!')
        else:
            print('VocÊ não pode efetuar o saque, pois atingiu o limite diario de 3 saques')

    elif opcao.upper() == 'E':
        while True:
            opcao_de_extrato = int(input("""
    [ 1 ] Extrato Geral
    [ 2 ] Extrato de Saques
    [ 3 ] Extrato de Depósitos
    [ 4 ] Sair
    """))

            if opcao_de_extrato == 1:
                for extrato_geral in extratos_bancarios['Extrato Geral']:
                    print(extrato_geral)


            if opcao_de_extrato == 2:
                for extrato_saque in extratos_bancarios['Extrato de Saques']:
                    print(extrato_saque)

            if opcao_de_extrato == 3:
                for extrato_deposito in extratos_bancarios['Extrato de Deposito']:
                    print(extrato_deposito)
            
            if opcao_de_extrato == 4:
                break
    elif opcao.upper()  ==  "Q":
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')
print('Tenha um bom dia!')