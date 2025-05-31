def medio_transporte(distancia):
    if distancia <= 1000:
        return "pie"
    elif distancia <= 10000:
        return "bicicleta"
    elif distancia <= 30000:
        return "colectivo"
    elif distancia <= 100000:
        return "auto"
    else:
        return "avión"

def mayor_numero(lista_numeros):
    mayor = lista_numeros[0]
    for num in lista_numeros:
        if num > mayor:
            mayor = num
    return mayor

# Pruebas

distancia = 12000
print("Medio de transporte para", distancia, "metros:", medio_transporte(distancia))

numeros = [4, 15, 9, 20, 3]
print("El número mayor es:", mayor_numero(numeros))
