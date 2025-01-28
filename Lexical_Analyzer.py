import re

class Token:
    def __init__(self, tName, value):
        self.tokenName = tName
        self.value = value
    
    def __str__(self):
        return f'Token<{self.tokenName}, {self.value}>'
        

class Tokenizer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
    
    def tokenize(self):   # Time complexity : O(n)
        expressions = [
            ('Reservedword', r'#include|\b(int|float|void|return|if|while|cin|cout|continue|break|using|iostream|namespace|std|main)\b'),
            ('Symbol', r'[\(\)\[\]\{\},:;]|==|!=|<=|>=|<<|>>|<|>|\+|-|\*|=|/|\|\|'),
            ('Identifier', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('Number', r'\d+(\.\d+)?'),  
            ('String', r'"([^"\\]|\\.)*"'),
            
            ('Skip', r'[ \t]+'), # Empty places
            ('MisMatch', r'.') # Invalid cases
        ]
        
        # Joining all expressions with '|'
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in expressions)  
        
        # Looking for tokens in the given code
        for match in re.finditer(token_regex, self.code): 
            kind = match.lastgroup
            value = match.group()
        
            # Identifying tokens that require manual processing
            if kind == 'Number':
                float(value) if '.' in value else int(value)
            elif kind == 'Skip' : 
                continue
            elif kind == 'MisMatch':
                raise SyntaxError(f'Invalid character : {value}')

            self.tokens.append(Token(kind, value))
        return self.tokens
