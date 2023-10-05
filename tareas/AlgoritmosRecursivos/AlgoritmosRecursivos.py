#Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = 7
resultado = fibonacci(numero)
print(f"El término {numero} de la serie de Fibonacci es {resultado}")

#Torres de Hanoi
def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de torre {origen} a torre {destino}")
        return
    torres_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de torre {origen} a torre {destino}")
    torres_hanoi(n - 1, auxiliar, destino, origen)

num_discos = 3
torres_hanoi(num_discos, 'A', 'C', 'B')



