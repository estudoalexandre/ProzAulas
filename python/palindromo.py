def palindromo(palavra):
    if palavra == palavra[::-1]:
        print('Essa palavra é um Palindromo')
    else:
        print('Essa palavra nao é um Palindromo')

usuario_palavra = input("Digite uma palavra: ")
palindromo(usuario_palavra)