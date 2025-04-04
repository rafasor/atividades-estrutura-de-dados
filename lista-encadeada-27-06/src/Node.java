public class Node<T> {
    private T value;
    @SuppressWarnings("rawtypes")
    private Node next;

    public Node(T valor) {
        this.value = valor;
        this.next = null;
    }

    @SuppressWarnings("unchecked")
    public Node<T> getNext() {
        return this.next;
    }

    @SuppressWarnings("rawtypes")
    public void setNext(Node next) {
        this.next = next;
    }

    public T getValue() {
        return value;
    }

    @Override
    public String toString() {
        return this.value.toString();
    }

    public void setValue(T newValue) {
        throw new UnsupportedOperationException("Unimplemented method 'setValue'");
    }
}
