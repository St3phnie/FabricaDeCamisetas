print('Bem vindo a Fábrica de Camisetas da Stephanie Marrocos')

# Valor das peças
precos = {
    'MCS': 1.80,
    'MLS': 2.10,
    'MCE': 2.90,
    'MLE': 3.20
}

# Valor do frete
fretes = {
    '0': 0,
    '1': 100,
    '2': 200
}


def escolha_modelo():
    while True:
        modelo = input('Escolha o modelo (MCS/MLS/MCE/MLE): ').upper()
        if modelo in precos:
            return precos[modelo]
        else:
            print("Modelo Inválido. Tente novamente")


def num_camisetas():
    while True:
        try:
            num = int(input('Informe o número de camisetas: '))
            if num > 20000:
                print('Não aceitamos pedidos nessa quantidade')
                print('Por favor, informe o número de camisetas novamente.')
                continue
            elif num >= 2000:
                desconto = 0.12
            elif num >= 200:
                desconto = 0.07
            elif num >= 20:
                desconto = 0.05
            else:
                desconto = 0.00
            return num, desconto
        except ValueError:
            print('Valor inválido. Informe um número inteiro')


# Escolher o frete
def frete():
    while True:
        print('\nEscolha o tipo de frete: ')
        print('0 - Retirar pedido na fábrica - R$ 0.00')
        print('1 - Frete por transportadora - R$ 100.00')
        print('2 - Frete por Sedex - R$ 200.00')
        tipoDeFrete = input(
            'Escolha o tipo de frete: ')
        if tipoDeFrete in fretes:
            return fretes[tipoDeFrete]
        else:
            print('Opção de frete inválida. Tente novamente')


# Obter o valor do modelo
valorModelo = escolha_modelo()

# Obter o número de camisetas e desconto
num, desconto = num_camisetas()

# Obter valor do frete
valorFrete = frete()

# Calcular o valor total
valorTotalCamisetas = valorModelo * num
valorComDesconto = valorTotalCamisetas * (1 - desconto)
total = valorComDesconto + valorFrete

# Exibir o valor total a pagar
try:
    print(f'O valor total a pagar é: R$ {total:.2f}')
except Exception as e:
    print(f'Erro: {e}')
