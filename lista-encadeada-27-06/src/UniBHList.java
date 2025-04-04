public class UniBHList<T extends Comparable<T>> {
    private Node<T> firstNode;
    private int totalElements;

    public void insertAtBeginning(T value) {
        Node<T> newNode = new Node<>(value);
        newNode.setNext(firstNode);
        firstNode = newNode;
        totalElements++;
    }

    public void insertAtEnd(T value) {
        Node<T> newNode = new Node<>(value);
        if (firstNode == null) {
            firstNode = newNode;
        } else {
            Node<T> current = firstNode;
            while (current.getNext() != null) {
                current = current.getNext();
            }
            current.setNext(newNode);
        }
        totalElements++;
    }

    public boolean search(T value) {
        Node<T> current = firstNode;
        while (current != null) {
            if (current.getValue().equals(value)) return true;
            current = current.getNext();
        }
        throw new RuntimeException("Item não encontrado na lista.");
    }

    public void removeByValue(T value) {
        if (firstNode == null) throw new RuntimeException("Lista vazia.");
        if (firstNode.getValue().equals(value)) {
            firstNode = firstNode.getNext();
            totalElements--;
            return;
        }
        Node<T> current = firstNode;
        while (current.getNext() != null && !current.getNext().getValue().equals(value)) {
            current = current.getNext();
        }
        if (current.getNext() == null) throw new RuntimeException("Item não encontrado na lista.");
        current.setNext(current.getNext().getNext());
        totalElements--;
    }

    public boolean isEmpty() {
        return totalElements == 0;
    }

    public void insertAfter(int index, T value) {
        if (index < 0 || index >= totalElements) throw new RuntimeException("Índice fora dos limites.");
        Node<T> newNode = new Node<>(value);
        Node<T> current = firstNode;
        for (int i = 0; i < index; i++) {
            current = current.getNext();
        }
        newNode.setNext(current.getNext());
        current.setNext(newNode);
        totalElements++;
    }

    public void removeAt(int index) {
        if (index < 0 || index >= totalElements) throw new RuntimeException("Índice fora dos limites.");
        if (index == 0) {
            firstNode = firstNode.getNext();
        } else {
            Node<T> current = firstNode;
            for (int i = 0; i < index - 1; i++) {
                current = current.getNext();
            }
            current.setNext(current.getNext().getNext());
        }
        totalElements--;
    }

    public int size() {
        return totalElements;
    }

    public void modifyElement(T oldValue, T newValue) {
        Node<T> current = firstNode;
        while (current != null) {
            if (current.getValue().equals(oldValue)) {
                current.setValue(newValue);
                return;
            }
            current = current.getNext();
        }
        throw new RuntimeException("Elemento não encontrado na lista.");
    }

    public void removeAtBeginning() {
        throw new UnsupportedOperationException("Unimplemented method 'removeAtBeginning'");
    }
}
