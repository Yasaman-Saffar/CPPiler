grammer = {
    "Start" : ["S N M"],
    "S" : ["#include S", "ε"],
    "N" : ["using namespace std ;", "ε"],
    "M" : ["int main(){T V}"],
    "T" : ["Id T","L T", "Loop T", "Input T", "Output T", "ε"],
    "V" : ["return Number;", "ε"],
    "Id" : ["int L", "float L"],
    "L": ["Identifier Assign Z"],
    "Z": [", Identifier Assign Z", ";"],
    "Operation": ["Number P", "Identifier P"],
    "P": ["O W P", "ε"],
    "O": ["+", "-", "*"],
    "W": ["Number", "Identifier"],
    "Assign": ["= Operation", "ε"],
    "Expression": ["Operation K Operation"],
    "K": ["==", ">=", "<=", "!="],
    "Loop": ["while(Expression){ T }"],
    "Input": ["cin >> Identifier F;"],
    "F": [">> Identifier F", "ε"],
    "Output": ["cout << C H;"],
    "H": ["<< C H", "ε"],
    "C": ["Number", "String", "Identifier"]
}

# Parse table using the grammar above
parse_table = {
   "Start": {
        "#include": "Start → S N M",
    },
   
    "S": {
        "#include": "S → #include S",
        "using": "S → ε",
    },
    
    "N": {
        "using": "N → using namespace std ;",
        "int": "N → ε",
    },
    
    "M": {
        "int": "M → int main ( ) { T V }",
    },
    
    "T": {
        "}" : "T → ε",
        "return" : "T → ε",
        "int" : "T → Id T",
        "float" : "T → Id T",
        "Identifier" : "T → L T",
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
        "=" : "Assign → = Operation",
        "," : "Assign → ε",
        ";" : "Assign → ε",
    },
    
    "Operation" : {
        "Number" : "Operation → Number P",
        "Identifier" : "Operation → Identifier P",
    },
    
    "Expression" : {
        "Number" : "Expression → Operation K Operation",
        "Identifier" : "Expression → Operation K Operation",
    },

    "Loop" : {
        "while" : "Loop → while ( Expression ) { T }",
    },
    
    "Input" : {
        "cin" : "Input → cin >> Identifier F ;",
    },
    
    "Output" : {
        "cout" : "Output → cout << C H ;",
    },

    "V" : {
        "}" : "V → ε",
        "return" : "V → return Number ;",
    },

    "L" : {
        "Identifier" : "L → Identifier Assign Z",
    },
    
    "Z" : {
        ";" : "Z → ;",
        "," : "Z → , Identifier Assign Z",
    },
    
    "P" : {
        ")" : "P → ε",
        ";" : "P → ε",
        "+" : "P → O W P",
        "-" : "P → O W P",
        "*" : "P → O W P",
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
        "Number" : "W → Number",
        "Identifier" : "W → Identifier",
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
        ";" : "F → ε",
        "Identifier" : "F → ε",
        "while" : "F → ε",
        "cin" : "F → ε",
        ">>" : "F → >> Identifier F",
        "cout" : "F → ε",
        "$" : "F → ε",
    },

    "H" : {
        "int" : "H → ε",
        "float" : "H → ε",
        "Identifier" : "H → ε",
        "while" : "H → ε",
        "cin" : "H → ε",
        "cout" : "H → ε",
        "<<" : "H → << C H",
        ";" : "H → ε",
        "$" : "H → ε",
    },

    "C" : {
        "Number" : "C → Number",
        "Identifier" : "C → Identifier",
        "String" : "C → String",
    },
}