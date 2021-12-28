
def xor(text: str, key: int):
    out = ''
    for char in text:
        if type(char) == str:
            char = ord(char)

        result = key ^ char
        result = list(bin(result))
        result = ''.join(result)
        result = chr(int(result, 2))
        out += result
    return out

if __name__ == '__main__':
    key = 232
    # text = 'this is the original text'
    text = '~!@#$%^&*()_+{}|:"<>?`1234567890-=[]\\;\',./qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

    encrypted = xor(text, key)
    decrypted = xor(encrypted, key)
    matches = (text == decrypted)

    print(f' Original: {text}')
    print(f'Encrypted: {encrypted}')
    print(f'Decrypted: {decrypted}')
    print(f'  Matches: {matches}')
