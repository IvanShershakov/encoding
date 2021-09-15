

def encrypt(s: str, key: dict) -> str:
    res_str = []
        
    for ch in s:
        res_str.append(key[ch])
    
    return ''.join(res_str)
    
def decrypt(s: str, key: dict) -> str:
    res_str = []
        
    for ch in s:
        for k, v in key.items():
            if ch in v:
                res_str.append(k)
    
    return ''.join(res_str)

def generate_key(shift: int) -> dict:
    key = dict()
    
    for i in range(ord('а'), ord('я')):
        key[chr(i)] = chr((i + shift) % 33 + ord('а'))
        
    key[' '] = '%'
    return key
    
END = False

KEY = generate_key(6)

while(not END):
    operation = input()
    
    if operation == 'decrypt':
        s = input()
        print(decrypt(s, KEY))
    elif operation == 'encrypt':
        s = input()
        print(encrypt(s, KEY))
    elif operation == '0':
        END = True
