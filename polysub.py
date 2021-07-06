import random

def build_map():
    '''
    Build random 128 length arr of unique ascii table indeces
    '''
    table_len = 2 ** 7
    out = []
    options = list(range(0, table_len-1))
    start = options[:32]
    options = options[32:]
    while len(options) != 0:
        selection = options.pop(random.randint(0, len(options)-1))
        out.append(selection)

    built = start + out + [127]
    final = {}
    for ind, val in enumerate(built):
        final[ind] = val

    return final


def translate(s, key):
    '''
    Convert plaintext to ciphertext according to key
    '''
    out = ''
    for c in s:
        out += chr(key[ord(c)])
    return out


def interpret(s, key):
    '''
    Convert ciphertext to plaintext according to key
    '''
    out = ''
    key_list = list(key.keys())
    val_list = list(key.values())
    for c in s:
        o = ord(c)
        orig = chr(key_list[val_list.index(o)])
        out += orig

    return out


def keystring(key):
    '''
    Convert a dict mapping of chars into an ordered string
    '''
    out = ''
    for i in range(32, 127):
        out += chr(key[i])
    return out


def key_from_string(string):
    '''
    Convert a string into a dict mapping of chars
    '''
    for ind, c in enumerate(string):
        out[ind+31] = ord(c)
    out[127] = 127

    return out


def default_string():
    '''
    Get the string of normal chars in the ascii table.
    Used to visualize generated mappings.
    '''
    out = ''.join([chr(x) for x in range(32, 127)])
    return out


if __name__ == '__main__':
    with open('zen.txt') as file:
        text = file.read()

    key = build_map()

    print('')
    result = translate(text, key)

    rows = result.split('\n')
    orig_rows = text.split('\n')
    width = max([len(x) for x in orig_rows])
    for i in range(len(rows)):
        gap = ' ' * (width - len(orig_rows[i]))
        print(orig_rows[i], gap, end='\t')
        print(rows[i])

    print(f'\n\n{keystring(key)}')
    print(f'{default_string()}')
