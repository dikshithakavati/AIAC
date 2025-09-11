class Node:
    """
    Node class for Binary Search Tree.
    Each node contains a value, and references to left and right child nodes.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation with insert, search, and inorder traversal methods.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the BST.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            # If value == node.value, do not insert duplicates
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        """
        Searches for a value in the BST.
        Returns True if found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder_traversal(self):
        """
        Returns a list of all values in the BST in sorted (inorder) order.
        """
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result

# --- Testing ---
if __name__ == "__main__":
    bst = BST()
    nums = [7, 3, 9, 1, 5, 8, 10]
    for n in nums:
        bst.insert(n)

    print("Inorder Traversal:", bst.inorder_traversal())  # Should be sorted: [1, 3, 5, 7, 8, 9, 10]
    print("Search 5:", bst.search(5))  # True
    print("Search 11:", bst.search(11))  # False