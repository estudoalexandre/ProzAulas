def calc_media(numeros):
    media_string = numeros.split(", ")
    float_numeros = [float(numero) for numero in media_string]
    media = sum(float_numeros) / len(float_numeros)
    
    return media



teste = input("Insira seus numeros separados por , Ex: ('10, 9, 8, 10, 10'): ")
media_final =calc_media(teste)
print(f"{media_final}")