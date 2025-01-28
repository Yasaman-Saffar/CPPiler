class Parse_tree_Node():
    def __init__(self, value, token_value=None):
        self.value = value
        self.children = []
        self.token_value = token_value
    
    def add_child(self, child):
        self.children.append(child)
        
class parse_tree():
    def __init__(self):
        self.root = None
        self.node_stack = []
    
    def initialize_root(self, root_value):
        self.root = Parse_tree_Node(root_value)
        self.node_stack = [self.root]
        return 
        
    def build_tree(self, children, current_index, token_stream, abstract_types, non_terminals):   # O(k) k is a small and constant number
        current_node = self.node_stack.pop()
        temp_list = []
        
        for child in children:
            if child in abstract_types:
                new_node = Parse_tree_Node(child, token_stream[current_index].value)
            else:
                new_node = Parse_tree_Node(child)
            
            current_node.add_child(new_node)
            temp_list.append(new_node)
            current_index += 1
        
        for element in reversed(temp_list):
            if element.value in non_terminals and element != 'ε':
                self.node_stack.append(element)

    def print_parse_tree(self, node, level=0):   # O(n)
        if node.token_value is not None:
            print("  " * level + f"{node.value} ({node.token_value})") 
        else:
            print("  " * level + node.value) 
        
        for child in node.children:
            self.print_parse_tree(child, level + 1)
