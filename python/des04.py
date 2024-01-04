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
        return "Voce precisa digitar um Operador Valido"
    
calculo = calculadora('*', 10, 20)
print(calculo)

## Ser chamada por um usuario
operador = str(input('Digite o operador desejado (+ - / *)'))
x = float(input('Digite o primeiro numero:'))
y = float(input('Digite o segundo numero:'))

resultado = calculadora(operador, x, y)
print("Resultado:", resultado)