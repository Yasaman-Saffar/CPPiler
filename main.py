import sys
from Lexical_Analyzer import Tokenizer
from Production_Sequencer import Nonrecursive_Predictive_Parser
from Parse_table import parse_table
from Search_In_Tree import Search_in_tree

class main():
    def __init__(self):
        self.tokens = None
        self.npp = None
        self.pt = None
        self.sit = Search_in_tree()
        
    def input(self):
        print('Please enter your c++ code \n(then press <Ctrl+Z + Enter> in a new line): ')
        code = sys.stdin.read()
        self.tokenizer_func(code)
        
    def tokenizer_func(self, code):
        tokenizer = Tokenizer(code)
        self.tokens = tokenizer.tokenize()
        self.npp = Nonrecursive_Predictive_Parser(self.tokens)
        self.pt = self.npp.parse_Tree
        
        self.NPP()
    
    def NPP(self):
        output_queue = self.npp.parse(parse_table)
        self.productions_output(output_queue)
        # self.search_identifier('y')
        
    def productions_output(self, oq):
        print('\n--------------PRODUCTIONS----------------\n')
        for n in oq:
            print(n)
        print('\n----------------------------------------')
        
    # def search_identifier(self, id):
    #     definition = self.sit.get_full_definition(id, self.pt.root)
    #     print(definition)
    

if __name__ == '__main__':
    m = main()
    m.input()