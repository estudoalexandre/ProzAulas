def count_char(char):
    contador_vogais = 0
    contador_consoantes = 0
    
    for i in char:
        if i.isalpha():
            if i.upper() in ["A", "B", "C", "D", "E"]:
                contador_vogais += 1
            else:
                contador_consoantes += 1
    return contador_vogais, contador_consoantes

usuario_palavra = input("Digite sua palavra: ")
vogais, consoantes = count_char(usuario_palavra)

print(f"Sua palavra '{usuario_palavra}' e nela contém {vogais} e {consoantes}")
