#Escriba una función recursiva para calcular la operación de la potencia.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)