# for i in range(100):
#     print("Hello World")
    
    
    #Praticando
    
# celsius = int(input("Digite a temperatura em Graus: "))
# fahrenheit = (celsius * 9/5) + 32    
# print("A temperatura em Fahrenheit é:", fahrenheit)
    
    
def graus_fahrenheit(graus):
    fahrenheit = (graus * 9/5) + 32
    return f"A temperatura em Fahrenheit é: {fahrenheit}"

temperatura_celsius = int(input("Digite a temperatura: "))
temperatura_fahrenheit = graus_fahrenheit(temperatura_celsius)
print(f"A temperatura em Fahrenheit é de: {temperatura_fahrenheit}")
    
