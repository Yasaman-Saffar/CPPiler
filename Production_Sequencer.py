class Parse_tree_Node():
    def __init__(self, value, token_value=None):
        self.value = value
        self.children = []
        self.token_value = token_value
    
    def add_child(self, child):
        self.children.append(child)
        
class Nonrecursive_Predictive_Parser:
    def __init__(self, tokens):
        self.input_tokens = tokens
        self.i = 0
        self.stack = ['Start']
        self.output_queue = []
        
        self.token = self.input_tokens[self.i]
        self.abstract_types = ['Identifier', 'Number', 'String']
        self.terminal = (self.token.tokenName if self.token.tokenName in self.abstract_types else self.token.value)
        self.non_terminals = ["S","N","M","T","V","Id","L","Z","Operation","P","O","W","Assign","Expression","K","Loop","Input","F","Output","H","C"]
        
        self.parse_tree_root = Parse_tree_Node('Start')
        self.node_stack = [self.parse_tree_root]
        
    
    def stack_update(self, stack, next_terminal):
        right_side = next_terminal.split('→')[1].strip().split()
        self.parse_tree_builder(right_side)
        
        for symbol in reversed(right_side):
            if symbol != 'ε':
                stack.append(symbol)
        return stack
    
    def moving_token(self):
        self.i += 1 # Moving next token if terminal matches the token
        if self.i < len(self.input_tokens):
            self.token = self.input_tokens[self.i]
            self.skip()
            self.terminal = (self.token.tokenName if self.token.tokenName in self.abstract_types else self.token.value)
    
    def skip(self):
        while (self.token.value == '<' or self.token.value == 'iostream' or self.token.value == '>') and (self.i < len(self.input_tokens)):
            self.i += 1
            if self.i < len(self.input_tokens):
                self.token = self.input_tokens[self.i]
            
    def parse(self, parse_table):
        while self.stack:
            x = self.stack.pop()
            
            if self.terminal == x:
                self.moving_token()
<<<<<<< HEAD
                    
=======
>>>>>>> 9964f33897efc4cb2b7369f881dd7548e6235ded
            else:
                production = parse_table[x][self.terminal]
                self.output_queue.append(production)
                self.stack = self.stack_update(self.stack, production)

        return self.output_queue
    
    def parse_tree_builder(self, children):
        current_node = self.node_stack.pop()
        temp_list = []
        temp_i = self.i + 1
        
        for child in children:
            if child == self.terminal:
                new_node = Parse_tree_Node(child, self.token.value)
            else:
                new_node = Parse_tree_Node(child)
            
            current_node.add_child(new_node)
            temp_list.append(new_node)
        
        for element in reversed(temp_list):
            if element.value in self.non_terminals and element != 'ε':
                self.node_stack.append(element)

    # def print_parse_tree(self, node, level=0):
    #     if node.token_value is not None:
    #         print("  " * level + f"{node.value} ({node.token_value})") 
    #     else:
    #         print("  " * level + node.value) 
        
    #     for child in node.children:
    #         self.print_parse_tree(child, level + 1)
