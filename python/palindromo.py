def palindromo(palavra):
    if palavra == palavra[::-1]:
        print('Essa palavra é um Palindromo')
    else:
        print('Essa palavra nao é um Palindromo')


teste = True
while teste:
    usuario_palavra = input("Digite uma palavra (ou se deseja encerrar o teste digite: sair): ")
    
    if usuario_palavra == "sair":
        teste = False
    else:
        palindromo(usuario_palavra)
    

    