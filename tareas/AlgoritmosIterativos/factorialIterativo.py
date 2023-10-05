def factorial_recursivo(n):
    if n == 0:
        return 1  
    else:
        return n * factorial_recursivo(n - 1)

n = 5
resultado = factorial_recursivo(n)
print(f"El factorial de {n} es {resultado}")
