grammer = {
    "Start" : ["S N M"],
    "S" : ["#include S", "ε"],
    "N" : ["using namespace std", "ε"],
    "M" : ["int main(){T V}"],
    "T" : ["Id T","L T", "Loop T", "Input T", "Output T", "ε"],
    "V" : ["return 0", "ε"],
    "Id" : ["int L", "float L"],
    "L": ["identifier Assign Z"],
    "Z": [", identifier Assign Z", ";"],
    "Operation": ["number P", "identifier P"],
    "P": ["O W P", "ε"],
    "O": ["+", "-", "*"],
    "W": ["number", "identifier"],
    "Assign": ["= Operation", "ε"],
    "Expression": ["Operation K Operation"],
    "K": ["==", ">=", "<=", "!="],
    "Loop": ["while(Expression){ T }"],
    "Input": ["cin >> identifier F;"],
    "F": [">> identifier F", "ε"],
    "Output": ["cout << C H;"],
    "H": ["<< C H", "ε"],
    "C": ["number", "string", "identifier"]
}

parse_table = {
   "Start": {
        "#include": "Start → S N M",
    },
   
    "S": {
        "#include": "S → #include S",
        "using": "S → ε",
    },
    
    "N": {
        "using": "N → using namespace std;",
        "int": "N → ε",
    },
    
    "M": {
        "int": "M → int main() {T V}",
    },
    
    "T": {
        "}" : "T → ε",
        "return" : "T → ε",
        "int" : "T → Id T",
        "float" : "T → Id T",
        "number" : "T → Operation T",
        "identifier" : "T → L T",
        "while" : "T → Loop T",
        "cin" : "T → Input T",
        "cout" : "T → Output T",
        "$" : "T → ε",
    },
    
    "Id" : {
        "int" : "Id → int L",
        "float" : "Id → float L",
    },
    
    "Assign" : {
        "identifier" : "Assign → identifier = Operation Q",
    },
    
    "Operation" : {
        "number" : "Operation → number P",
        "identifier" : "Operation → identifier P",
    },
    
    "Expresion" : {
        "number" : "Expresion → Operation K Operation",
        "identifier" : "Expresion → Operation K Operation",
    },

    "Loop" : {
        "while" : "Loop → while(Expression){ T }",
    },
    
    "Input" : {
        "cin" : "Input → cin>>identifier F;",
    },
    
    "Output" : {
        "cout" : "Output → cout<<CH;",
    },

    "V" : {
        "}" : "V → ε",
        "return" : "V → return 0;",
    },

    "L" : {
        "identifier" : "L → identifier Assign Z",
    },
    
    "Z" : {
        ";" : "Z → ;",
        "," : "Z → , identifier Assign Z",
    },
    
    "P" : {
        ")" : "P → ε",
        "+" : "P → OWP",
        "-" : "P → OWP",
        "*" : "P → OWP",
        "," : "P → ε",
        "==" : "P → ε",
        ">=" : "P → ε",
        "<=" : "P → ε",
        "!=" : "P → ε",
    },
    
    "O" : {
        "+" : "O → +",
        "-" : "O → -",
        "*" : "O → *",
    },
    
    "W" : {
        "number" : "W → number",
        "identifier" : "W → identifier",
        "<<" : "H → ε",
    },

    "K" : {
        "==" : "K → ==",
        ">=" : "K → >=",
        "<=" : "K → <=",
        "!=" : "K → !="
    },
    
    "F" : {
        "int" : "F → ε",
        "float" : "F → ε",
        "identifier" : "F → ε",
        "while" : "F → ε",
        "cin" : "F → ε",
        ">>" : "F → >>identifier F",
        "cout" : "F → ε",
        "$" : "F → ε",
    },

    "H" : {
        "int" : "H → ε",
        "float" : "H → ε",
        "identifier" : "H → ε",
        "while" : "H → ε",
        "cin" : "H → ε",
        "cout" : "H → ε",
        "<<" : "H → <<CH",
        "$" : "H → ε",
    },

    "C" : {
        "number" : "C → number",
        "identifier" : "C → identifier",
        "string" : "C → string",
    },
}

def Nonrecursive_Predictive_Parser(input_tokens, parser_table):
    start_symbol = "Start"
    stack = [start_symbol]
    i = 0
    
    while stack:
        x = stack.pop()