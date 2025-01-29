from Parse_Tree import parse_tree

class Nonrecursive_Predictive_Parser:
    def __init__(self, tokens=None):
        self.input_tokens = tokens
        self.i = 0
        self.stack = ['Start']
        self.output_queue = []
        
        self.token = self.input_tokens[self.i]
        self.abstract_types = ['Identifier', 'Number', 'String']
        self.terminal = (self.token.tokenName if self.token.tokenName in self.abstract_types else self.token.value)
        self.non_terminals = ["S","N","M","T","V","Id","L","Z","Operation","P","O","W","Assign","Expression","K","Loop","Input","F","Output","H","C"]
        
        self.parse_Tree = parse_tree()
        self.parse_Tree.initialize_root('Start')
        
        
    def stack_update(self, stack, next_terminal):     # O(k)
        right_side = next_terminal.split('→')[1].strip().split()
        self.parse_Tree.build_tree(right_side, self.i, self.input_tokens, self.abstract_types, self.non_terminals)
        
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
            
    def parse(self, parse_table):   # O(n)
        while self.stack:
            x = self.stack.pop()
            
            if self.terminal == x:
                self.moving_token()
                    
            else:
                production = parse_table[x][self.terminal]
                self.output_queue.append(production)
                self.stack = self.stack_update(self.stack, production)

        # self.print_parse_tree()
        return self.output_queue

    def print_parse_tree(self):
        self.parse_Tree.print_parse_tree(self.parse_Tree.root)