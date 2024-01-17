# for i in range(100):
#     print("Hello World")
    
    
    #Praticando
    
# celsius = int(input("Digite a temperatura em Graus: "))
# fahrenheit = (celsius * 9/5) + 32    
# print("A temperatura em Fahrenheit é:", fahrenheit)
    
    
# def graus_fahrenheit(graus):
#     fahrenheit = (graus * 9/5) + 32
#     return f"A temperatura em Fahrenheit é: {fahrenheit}"

# temperatura_celsius = int(input("Digite a temperatura: "))
# temperatura_fahrenheit = graus_fahrenheit(temperatura_celsius)
# print(f"A temperatura em Fahrenheit é de: {temperatura_fahrenheit}\n")


# def lista_compras():
#     lista = []
#     print('Após terminar sua lista, apenas digite: "sair"')
#     while True:
#         item = input("Digite um item para adicionar a lista de compras: ")
#         if item == "sair":
#             break
#         else:
#             lista.append(item)
#     return lista


# lista_de_compras = lista_compras()
# print("Lista de compras: ")
# for item in lista_de_compras:
#     print("Produto:" + " - " + item)
            
    


def salario_hora():
    salario = float(input("Insirá o salario Mensal: "))
    hora = float(input("Insira suas horas mensais: "))
    
    return salario / hora


resultado = salario_hora()
print(f"Salário por hora: R${resultado:.2f}")