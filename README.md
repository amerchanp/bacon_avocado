# RETO 8

1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
```
#1.1 Cuadrado de un número (Reto 6 - punto 1)
cuadrado = lambda x: x ** 2

#1.2 Determinar si un número es par (Reto 6 - punto 2)
es_par = lambda x: x % 2 == 0

#1.3 Determinar si un número es positivo, negativo o cero (Reto 4 - punto 5)
es_positivo = lambda x: x > 0
es_negativo = lambda x: x < 0
es_cero = lambda x: x == 0
```

---


2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
```
#2.1 Suma de cuadrados del 1 al 100 (adaptación de Reto 6 - punto 1)
def suma_cuadrados(*args):
    return sum(x**2 for x in args)

#2.2 Suma de todos los números impares en un rango (Reto 6 - punto 2 adaptado)
def suma_impares(*args):
    return sum(x for x in args if x % 2 != 0)

#2.3 Mínimo o máximo entre varios números (útil en varios retos)
def minimo(*args):
    return min(args)

def maximo(*args):
    return max(args)
```
---

3. Escriba una función recursiva para calcular la operación de la potencia.
```
#Escriba una función recursiva para calcular la operación de la potencia.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
```
---

4. Utilice la siguiente plantilla de code para contar el tiempo (Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.)
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

```
import time

# Fibonacci recursivo
def fibonacci_rec(n):
    if n <= 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

# Fibonacci iterativo
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 30 

# Medir tiempo para la versión recursiva
start_time = time.time()
resultado_rec = fibonacci_rec(n)
end_time = time.time()
tiempo_rec = end_time - start_time

# Medir tiempo para la versión iterativa
start_time = time.time()
resultado_iter = fibonacci_iter(n)
end_time = time.time()
tiempo_iter = end_time - start_time

# Mostrar resultados
print(f"Fibonacci recursivo para n={n} = {resultado_rec}, tiempo: {tiempo_rec:.6f} segundos")
print(f"Fibonacci iterativo para n={n} = {resultado_iter}, tiempo: {tiempo_iter:.6f} segundos")

```
---

5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

![image](https://github.com/user-attachments/assets/a82695a0-4807-4099-b44b-f61a6c7ad776)

---

6. Ir a linkedin y crear perfil.

https://www.linkedin.com/in/alejandro-merchan-pulgarin-023646372/
