class Nonrecursive_Predictive_Parser:
    def __init__(self, tokens):
        self.input_tokens = tokens
        self.i = 0
        self.stack = ['Start']
        self.output_queue = []
        
        self.token = self.input_tokens[self.i]
        self.abstract_types = ['Identifier', 'Number', 'String']
        self.terminal = (self.token.tokenName if self.token.tokenName in self.abstract_types else self.token.value)
    
    def stack_update(self, stack, next_terminal):
        right_side = next_terminal.split('→')[1].strip().split()
        
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
        moved = False
        
        while self.stack:
            x = self.stack.pop()
            
            if self.terminal == x:
                self.moving_token()
            else:
                production = parse_table[x][self.terminal]
                self.output_queue.append(production)
                self.stack = self.stack_update(self.stack, production)

        return self.output_queue
