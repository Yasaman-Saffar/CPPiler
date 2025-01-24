import hashlib
from Lexical_Analyzer import Tokenizer

def making_tokens():
    code = '''#include <iostream>
        using namespace std;
        int main(){
        int x;
        int s=0, t=10;
        while (t >= 0){
        cin>>x;
        t = t - 1;
        s = s + x;
        }
        cout<<"sum="<<s;
        return 0;
        }
    '''
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    return tokens

def sorted_tokenTable(tokens):
    priority = {'Reservedword' : 1, 'Identifier' : 2, 'Symbol' : 3, 'Number' : 4, 'String' : 5}
    sorted_tokens = sorted(tokens, key=lambda x: (priority[x.tokenName], x.value))  
    sorted_hash = [{"TokenName" : token.tokenName, "hashedValue": hashlib.sha256(token.value.encode()).hexdigest()} for token in sorted_tokens]
    return sorted_hash


# toks = making_tokens()
# hashed = sorted_tokenTable(toks)
# for t in hashed:
#     print(f"TokenName: {t['TokenName']}, Value: {t['hashedValue']}")