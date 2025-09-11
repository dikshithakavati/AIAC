class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    def push(self, item):
        """Add an item to the top of the stack.
        Args:
            item: The item to be added.
        """
        self._items.append(item)
    def pop(self):
        """Remove and return the top item from the stack.
        Returns:
            The item at the top of the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        """Return the top item without removing it.
        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    def is_empty(self):
        """Check if the stack is empty.
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0
if __name__ == "__main__":
    # Sample test cases for Stack operations
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek())  # 30
    print("Pop:", stack.pop())    # 30
    print("Peek after pop:", stack.peek())  # 20
    print("Is stack empty?", stack.is_empty())  # False
    stack.pop()
    stack.pop()
    print("Is stack empty after popping all?", stack.is_empty())  # True
    # Uncommenting the next line will raise an IndexError
    # stack.pop()