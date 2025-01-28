from Parse_Tree import parse_tree

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
        
        self.parse_Tree = parse_tree(self.input_tokens,  self.abstract_types, self.non_terminals)
        self.parse_Tree.initialize_root('Start')
        
        
    def stack_update(self, stack, next_terminal):
        right_side = next_terminal.split('→')[1].strip().split()
        self.parse_Tree.build_tree(right_side, self.i)
        
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
                    
            else:
                production = parse_table[x][self.terminal]
                self.output_queue.append(production)
                self.stack = self.stack_update(self.stack, production)

        self.print_parse_tree()
        return self.output_queue

    def print_parse_tree(self):
        self.parse_Tree.print_parse_tree(self.parse_Tree.root)
    
    # def parse_tree_builder(self, children):
    #     current_node = self.node_stack.pop()
    #     temp_list = []
    #     temp_i = self.i
    #     temp_token = self.input_tokens
        
    #     for child in children:
    #         if child in self.abstract_types:
    #             new_node = Parse_tree_Node(child, temp_token[temp_i].value)
    #             print(temp_token[temp_i].value)
    #         else:
    #             new_node = Parse_tree_Node(child)
            
    #         current_node.add_child(new_node)
    #         temp_list.append(new_node)
    #         temp_i += 1
        
    #     for element in reversed(temp_list):
    #         if element.value in self.non_terminals and element != 'ε':
    #             self.node_stack.append(element)

    # def print_parse_tree(self, node, level=0):
    #     if node.token_value is not None:
    #         print("  " * level + f"{node.value} ({node.token_value})") 
    #     else:
    #         print("  " * level + node.value) 
        
    #     for child in node.children:
    #         self.print_parse_tree(child, level + 1)
