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
