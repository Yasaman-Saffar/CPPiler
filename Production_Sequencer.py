from Parse_table import parse_table

def stack_update(stack, next_terminal):
    right_side = next_terminal.split('→')[1].strip().split()
    
    for symbol in reversed(right_side):
        if symbol != 'ε':
            stack.append(symbol)
    return stack

def Nonrecursive_Predictive_Parser(input_tokens, parser_table):
    stack = ['Start']
    
    abstract_types = ['Identifiers', 'Numbers', 'Strings']
    output_queue = []
    i = 0
    token = input_tokens[i]
    
    while stack:
        terminal = token.tokenName if token.tokenName in abstract_types else token.value
        x = stack.pop()
        
        if terminal == x:
            i += 1 # Moving to next token if terminal matches the token
            token = input_tokens[i]
            
            if token.value == '>' or token.value == '<' or token.value == 'iostream':
                i += 1
                continue

        next_terminal = parse_table[x][terminal]
            
                
        output_queue.append(next_terminal)
        stack = stack_update(stack, next_terminal)
        
        