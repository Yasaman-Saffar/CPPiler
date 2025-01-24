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
    
    def tokenize(self):
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
        
            # Identifying okens that require manual processing
            if kind == 'Number':
                float(value) if '.' in value else int(value)
            elif kind == 'Skip' : 
                continue
            elif kind == 'MisMatch':
                raise SyntaxError(f'Invalid character : {value}')

            self.tokens.append(Token(kind, value))
        return self.tokens
        

# code = '''#include <iostream>
#     using namespace std;
#     int main(){
#     int x;
#     int s=0, t=10;
#     while (t >= 0){
#     cin>>x;
#     t = t - 1;
#     s = s + x;
#     }
#     cout<<"sum="<<s;
#     return 0;
#     }
# '''
# tokenizer = Tokenizer(code)
# tokens = tokenizer.tokenize()
# for token in tokens:
#     print(token)