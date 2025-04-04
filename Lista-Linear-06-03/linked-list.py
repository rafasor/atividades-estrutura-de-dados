class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        raise ValueError("Item não encontrado na lista")
    
    def remove_by_value(self, value):
        if self.head is None:
            raise ValueError("Lista vazia")
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        prev = None
        current = self.head
        while current:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError("Item não encontrado na lista")
    
    def insert_after(self, index, value):
        if index < 0 or index >= self.size():
            raise IndexError("Índice fora dos limites da lista")
        
        new_node = Node(value)
        current = self.head
        for _ in range(index):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def remove_at_index(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Índice fora dos limites da lista")
        
        if index == 0:
            self.head = self.head.next
            return
        
        prev = None
        current = self.head
        for _ in range(index):
            prev = current
            current = current.next
        
        prev.next = current.next
    
    def update_value(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next
        raise ValueError("Item não encontrado na lista")
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements



if __name__ == "__main__":
    # Criando a lista encadeada
    ll = LinkedList()

    # Verificando se a lista está vazia
    print("A lista está vazia?", ll.is_empty())  # True

    # Adicionando manualmente o primeiro nó
    ll.head = Node("A")
    
    # Inserindo elementos após um índice específico
    ll.insert_after(0, "B")
    ll.insert_after(1, "C")
    print("Lista após inserções:", ll.display())  # ['A', 'B', 'C']

    # Buscando um item
    try:
        node = ll.search("B")
        print(f"Item encontrado: {node.data}")  # B
    except ValueError as e:
        print(e)

    # Modificando um item
    ll.update_value("B", "D")
    print("Lista após atualização:", ll.display())  # ['A', 'D', 'C']

    # Removendo um item por valor
    ll.remove_by_value("A")
    print("Lista após remover A:", ll.display())  # ['D', 'C']

    # Removendo item pelo índice
    ll.remove_at_index(1)  # Remove 'C'
    print("Lista após remover índice 1:", ll.display())  # ['D']

    # Testando tamanho da lista
    print("Tamanho da lista:", ll.size())  # 1

    # Testando erro ao buscar um item inexistente
    try:
        ll.search("X")
    except ValueError as e:
        print(e)  # "Item não encontrado na lista"

    # Testando erro ao remover um item inexistente
    try:
        ll.remove_by_value("X")
    except ValueError as e:
        print(e)  # "Item não encontrado na lista"

