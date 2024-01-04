def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtracao")
        print("3: Multipliacao")
        print("4: Divisao")
        print("0: Sair")
        
        operacao = input('Escolha a operacao (0-4): ')
        
        if operacao == '0':
            print('Voce saiu da calculadora')
            break
        elif operacao in ('1', '2', '3', '4'):
            x = input('Digite o primeiro valor: ')
            y = input('Digite o segundo Valor')