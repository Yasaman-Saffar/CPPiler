import sys
from Lexical_Analyzer import Tokenizer
from Production_Sequencer import Nonrecursive_Predictive_Parser
from Parse_table import parse_table

class main():
    def __init__(self):
        self.tokens = None
        
    def input(self):
        print('Please enter your c++ code \n(then press <Ctrl+Z + Enter> in a new line): ')
        code = sys.stdin.read()
        self.tokenizer_func(code)
        
    def tokenizer_func(self, code):
        tokenizer = Tokenizer(code)
        self.tokens = tokenizer.tokenize()
        self.NPP(self.tokens)
    
    def NPP(self, tokens):
        npp = Nonrecursive_Predictive_Parser(tokens)
        output_queue = npp.parse(parse_table)
        self.productions_output(output_queue)
        # self.print_parse_tree(npp)
        
    def productions_output(self, oq):
        print('\n--------------PRODUCTIONS----------------\n')
        for n in oq:
            print(n)
        print('\n----------------------------------------')
    
    # def print_parse_tree(self, npp):
    #     npp.print_parse_tree(npp.parse_tree_root)


if __name__ == '__main__':
    m = main()
    m.input()