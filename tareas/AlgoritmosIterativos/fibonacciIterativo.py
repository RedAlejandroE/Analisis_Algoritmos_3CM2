def fibonacci(n):
    
    a, b = 0, 1
    fibonacci_sequence = []
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

n = 20
resultado = fibonacci(n)
print(resultado)


numero_a_buscar = 3
if numero_a_buscar in resultado:
    posicion = resultado.index(numero_a_buscar)
    print(f"El número {numero_a_buscar} se encuentra en la posición {posicion + 1} del array.")
else:
    print(f"El número {numero_a_buscar} no se encuentra en el array.")


























""" def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursivo(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Llamamos a la función para obtener los primeros 10 números de Fibonacci
n = 10
resultado = fibonacci_recursivo(n)
print(resultado) """