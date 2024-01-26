def fatorial(n):
    fatorial = 1
    for i in range(n, 0, -1):
        fatorial *= i
    return fatorial

resultado = fatorial(5)
print(resultado)