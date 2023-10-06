def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenamiento_burbuja_optimizado(arr):
    n = len(arr)
    for i in range(n):
        intercambios = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios = True
        if not intercambios:
            break

def main():
    print("Seleccione el método de ordenamiento:")
    print("1. Burbuja")
    print("2. Burbuja Optimizada")
    
    opcion = int(input("Ingrese su elección (1/2): "))
    
    if opcion not in [1, 2]:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
        return
    
    n = int(input("Ingrese el tamaño de la lista: "))
    arr = []
    for i in range(n):
        elemento = int(input(f"Ingrese el elemento {i+1}: "))
        arr.append(elemento)
    
    if opcion == 1:
        ordenamiento_burbuja(arr)
        print("Lista ordenada usando Burbuja:", arr)
    elif opcion == 2:
        ordenamiento_burbuja_optimizado(arr)
        print("Lista ordenada usando Burbuja Optimizada:", arr)

if __name__ == "__main__":
    main()
