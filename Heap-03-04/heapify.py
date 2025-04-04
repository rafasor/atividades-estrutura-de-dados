def max_heapify(arr, n, i):
    """Garante a propriedade do Heap Máximo no nó i."""
    largest = i  # Assume que o nó i é o maior
    left = 2 * i + 1  # Índice do filho esquerdo
    right = 2 * i + 2  # Índice do filho direito

    # Se o filho esquerdo for maior que o pai
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Se o filho direito for maior que o maior atual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior elemento não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        max_heapify(arr, n, largest)  # Aplica recursivamente

def build_max_heap(arr):
    """Transforma um array em um Heap Máximo."""
    n = len(arr)
    
    # Aplica MAX-HEAPIFY em todos os nós não-folha (de baixo para cima)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    """Ordena um array usando Heap Sort (baseado no Heap Máximo)."""
    n = len(arr)

    # Constrói o heap máximo
    build_max_heap(arr)

    # Extrai elementos um a um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move a raiz para o final
        max_heapify(arr, i, 0)  # Restaura a propriedade do heap

# Exemplo de uso
arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
print("Array original:", arr)

build_max_heap(arr)
print("Heap máximo:", arr)

heapsort(arr)
print("Array ordenado:", arr)
