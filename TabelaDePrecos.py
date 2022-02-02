import os
from time import sleep


while True:
    os.system('cls')
    TitPreco = ('Tipo de Reparo', 'Preço', 'Desconto')

    print(''' Escolha um cliente:
            1 - Frubana
            2 - James Delivery
            3 - Pizza Hut''')

    resp = int(input('Digite a opção: '))

    cliente = [{'cliente': 'Frubana', 'desconto': 10}, {
        'cliente': 'James Delivery', 'desconto': 20}, {'cliente': 'Pizza Hut', 'desconto': 30}]

    os.system('cls')
    def loading():
        for i in range(len(cliente)):
            print('\tLendo clientes... ', end='')
            print(cliente[i]['cliente'], end='', flush=True)
            sleep(0.3)
            # Barra de carregamento
            for i in range(len(cliente), 101):
                sleep(0.01)
                print('\r{}%'.format(i), end='')
            os.system('cls')
        os.system('cls')
        
        
        
        
    loading()


    print(f'cliente: {cliente[resp-1]["cliente"]} tem desconto de {cliente[resp-1]["desconto"]}%')
    print('''Escolha um aparelho:
            1 - Galaxy S7
            2 - Moto G5s Plus''')

    respCel = int(input('Digite a opção: '))

    GalaxyS7 = ('Avaria na tampa traseira ', 274.24,
                'Avaria na tela com dano do aro metálico ', 1265.59)

    MotoG5sPlus = ('Avaria na tampa traseira ', 405.25,
                'Avaria na tela com dano do aro metálico ', 150.59)

    if respCel == 1:
        print('\nGalaxy S7')
        print(f'{TitPreco[0]:<50} {TitPreco[1]:>7} {TitPreco[2]:>12}\n')
        for pos in range(0, len(GalaxyS7)):
            if pos % 2 == 0:
                print(f'{GalaxyS7[pos]:.<50}', end=' ')
            else:
                print(
                    f'R$ {GalaxyS7[pos]:>7.2f}', end=' ')
                print(
                    f'R$ {GalaxyS7[pos]-GalaxyS7[pos]*cliente[resp-1]["desconto"]/100:>7.2f}')
    if respCel == 2:
        print('\nMoto G5s Plus')
        print(f'{TitPreco[0]:<50} {TitPreco[1]:>7} {TitPreco[2]:>12}\n')
        for pos in range(0, len(MotoG5sPlus)):
            if pos % 2 == 0:
                print(f'{MotoG5sPlus[pos]:.<50} ', end=' ')
            else:

                print(
                    f'R$ {MotoG5sPlus[pos]:>7.2f}', end=' ')
                print(
                    f'R$ {MotoG5sPlus[pos]-MotoG5sPlus[pos]*cliente[resp-1]["desconto"]/100:>7.2f}')

    print('\n')
    os.system('pause')
    

