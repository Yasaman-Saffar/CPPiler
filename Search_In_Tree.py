from collections import deque

class Search_in_tree:
    def __init__(self):
        self.identifier_found = False
        self.identifier = None
        self.definition = ''
    
    def initialize_identifier(self, id):
        self.identifier = id
    
    def find_identifier_bfs(self, identifier, root): # O(n)
        queue = deque([(root, [])])
        
        while queue:
            current_node, path = queue.popleft()
            
            if current_node.value == 'Identifier' and current_node.token_value == identifier:
                return path + [current_node]
            
            for child in current_node.children:
                queue.append((child, path + [current_node]))
        return None

    def reconstruct_code_from_subtree(self, node):   # O(m)
        if not self.identifier_found:
            if node.value == ',' or node.value == 'Number':
                if node.value == 'Number':
                    self.definition += f'{str(node.token_value)} '
                    self.identifier_found = True
            if node.token_value:
                if node.token_value == self.identifier:
                    self.definition += f'{str(node.token_value)} '
            if node.value == '=':
                self.definition += f'{str(node.value)} '
        
        for child in node.children:
            child_definition = self.reconstruct_code_from_subtree(child)
            if child_definition:
                self.definition += child_definition
                
    def find_type(self, path): # O(m)
        for p in path:
            if p.value == 'Id':
                for child in p.children:
                    if child.value in ['int', 'float']:
                        self.definition += f'{str(child.value)} '
        parent_node = path[-2]
        self.reconstruct_code_from_subtree(parent_node)
        
    def get_full_definition(self, identifier, root):
        self.initialize_identifier(identifier)
        path = self.find_identifier_bfs(identifier, root)
        if not path:
            return f'Identifier "{identifier}" not found.'
        
        self.find_type(path)
        return self.definition