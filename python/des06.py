def name_idade():
    nome = str(input('Digite o seu nome completo: '))

    while True: 
        try:
            nascimento = int(input('Digite o seu ano de nascimento: '))
            if not(1922 <= nascimento <= 2021):
                print(f'Olá, ${nome} Voce precisa digitar um ano valido entre 1922 e 2021')
            else:
                idade = 2022 - nascimento
                print(f'Olá, ${nome}! Nesse ano de 2022 voce está completando ${idade} anos')
                break
        except ValueError:
            print('Erro: digite um ano de nascimento valido')
            
name_idade()