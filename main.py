import sys
from Lexical_Analyzer import Tokenizer
from Production_Sequencer import Nonrecursive_Predictive_Parser
from Parse_table import parse_table

class main():
    def __init__(self):
        self.tokens = []
        
    def input(self):
        print('Please enter your c++ code \n(then press Ctrl+Z - Enter in a new line): ')
        code = sys.stdin.read()
        self.tokenizer_func(code)
        
    def tokenizer_func(self, code):
        tokenizer = Tokenizer(code)
        self.tokens = tokenizer.tokenize()
        self.NPP()
    
    def NPP(self):
        npp = Nonrecursive_Predictive_Parser(self.tokens)
        output_queue = npp.parse(parse_table)
        self.productions_output(output_queue)
        
    def productions_output(self, oq):
        for n in oq:
            print(n)


if __name__ == '__main__':
    m = main()
    m.input()