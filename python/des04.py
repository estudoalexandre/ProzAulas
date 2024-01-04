# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(operacao, x, y):
    if operacao == '+':
       return x + y
    elif operacao == '-':
       return x - y
    elif operacao == '*':
       return x * y
    elif operacao == '/':
       return x / y
    else:
        return 0
    
calculo = calculadora('', 10, 20)
print(calculo)

## Ser chamada por um usuario
operador = str(input('Digite o operador desejado (+ - / *)'))
x = float(input('Digite o primeiro numero:'))
y = float(input('Digite o segundo numero:'))

resultado = calculadora(operador, x, y)
print("Resultado:", resultado)