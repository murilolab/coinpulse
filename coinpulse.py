import requests
def  menu():
    print('='*30)
    print('          CoinPulse')
    print('='*30)
    print('1. Verificar cotação atual da moeda\n2. Sair')
    print('-'*30)
    while True:
            try:
                escolha = int(input('Escolha uma opção: '))
                while escolha!=1 and escolha!=2:
                    print('Opção invalida!')
                    print('='*30)
                    print('          CoinPulse')
                    print('='*30)
                    print('1. Verificar cotação atual da moeda\n2. Sair')
                    print('-'*30)
                    escolha = int(input('Escolha uma opção: '))
                break
            except ValueError:
                print('Opção inválida!')
                print('='*30)
                print('          CoinPulse')
                print('='*30)
                print('1. Verificar cotação atual da moeda\n2. Sair')
                print('-'*30)
    return escolha
def moeda_escolhida():
    moedas_validas=['USD','EUR','BTC','GBP','JPY','CAD','AUD','CHF','ETH']
    moeda = input('Qual moeda você deseja analisar? (USD/EUR/GBP/BTC/CAD/JPY/AUD/CHF/ETH): ').upper()
    while moeda not in moedas_validas:
        print('Moeda invalida!')
        moeda = input('Qual moeda você deseja analisar? (USD/EUR/GBP/BTC/CAD/JPY/AUD/CHF/ETH): ').upper()
    while True:
        try:
            valor_desejado= float(input('Qual valor máximo que você deseja pagar? '))
            while valor_desejado<0:
                valor_desejado= float(input('Qual valor máximo que você deseja pagar? '))
            break
        except ValueError:
            print('Opção inválida!')
    return moeda, valor_desejado
def buscar_preco(moeda,valor_desejado):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    resposta=requests.get(url)
    dados = resposta.json()
    chave = f"{moeda}BRL"
    preco_moeda = float(dados[chave]["bid"])
    print(f'Preço atutal da {moeda}: {preco_moeda:,.2f}')
    if preco_moeda<=valor_desejado:
        print(f'É um bom momento para comprar a moeda {moeda}!')
    else:
        print(f'Não é um bom momento para comprar a moeda {moeda}!')
    return preco_moeda
escolha = menu()
while escolha!= 2:
    moeda, valor_desejado=moeda_escolhida()
    print(f'Buscando informações sobre a moeda desejada {moeda} com o valor alvo {valor_desejado}...')
    buscar_preco(moeda,valor_desejado)
    escolha=menu()
print('Obrigado por usar o CoinPulse!')