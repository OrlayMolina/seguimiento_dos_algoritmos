def treesort(data, key=None):
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def get_key(item):
        if key is not None:
            return key(item)
        elif isinstance(item, (list, tuple)) and len(item) > 1:
            return item[1]
        return item

    def get_term(item):
        if isinstance(item, (list, tuple)) and len(item) > 0:
            return str(item[0]).lower()
        return str(item).lower()
    
    def insert(root, data):
        if root is None:
            return Node(data)

        if key is not None:
            # Usar el comparador personalizado
            compare_result = key(data, root.data)
            if compare_result < 0:
                root.left = insert(root.left, data)
            else:
                root.right = insert(root.right, data)
        else:
            # Comparación predeterminada
            key_data = get_key(data)
            key_root = get_key(root.data)
            
            if key_data > key_root:
                root.left = insert(root.left, data)
            elif key_data < key_root:
                root.right = insert(root.right, data)
            else:
                term_data = get_term(data)
                term_root = get_term(root.data)
                
                if term_data < term_root:
                    root.left = insert(root.left, data)
                else:
                    root.right = insert(root.right, data)
        
        return root

    def in_order_traversal(root, result):
        if root:
            in_order_traversal(root.left, result)
            result.append(root.data)
            in_order_traversal(root.right, result)

    root = None
    for item in data:
        root = insert(root, item)

    result = []
    in_order_traversal(root, result)
    
    return result