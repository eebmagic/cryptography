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


def translate(s, keys):
    '''
    Convert plaintext to ciphertext according to key
    '''
    out = ''
    for i, c in enumerate(s):
        out += chr(keys[i % len(keys)][ord(c)])
    return out


def interpret(s, keys):
    '''
    Convert ciphertext to plaintext according to key
    '''
    out = ''
    key_list = [list(key.keys()) for key in keys]
    val_list = [list(key.values()) for key in keys]
    for i, c in enumerate(s):
        o = ord(c)
        orig = chr(key_list[i % len(keys)][val_list[i % len(keys)].index(o)])
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


def keystrings(keys):
    '''
    Convert a list of dict mappings of chars into 
    one long conjoined ordered string.
    '''
    out = ''
    for key in keys:
        out += keystring(key)
    return out


def key_from_string(string):
    '''
    Convert a string into a dict mapping of chars.
    '''
    out = {i: i for i in range(32)}
    for ind, c in enumerate(string):
        out[ind+32] = ord(c)
    out[127] = 127

    return out


def keys_from_string(string):
    '''
    Convert a string into a list of dict mappings of chars.
    '''
    splits = []
    WIDTH = 95
    while len(string):
        selection = string[:WIDTH]
        validate_string(selection)
        splits.append(selection)
        string = string[WIDTH:]

    out = []
    for split in splits:
        out.append(key_from_string(split))

    return out


def validate_string(string):
    '''
    Validates that a string is a unique set of all ascii chars.
    '''
    assert len(string) == 95, "String must be 95 chars long"
    assert len(set(string)) == len(string), "String must only have chars appearing once"

    return True


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

    key_a = build_map()
    key_b = build_map()
    key_c = build_map()
    keys = [key_a, key_b, key_c]

    print(default_string())
    print(keystring(key_a))
    print(keystring(key_b))
    print(keystring(key_c))

    # Build and save result
    result = translate(text, keys)
    with open('result.txt', 'w') as file:
        file.write(result)
    with open('key.txt', 'w') as file:
        keys_string = keystrings(keys)
        file.write(keys_string)

    # Display translated text against original
    print('')
    rows = result.split('\n')
    orig_rows = text.split('\n')
    width = max([len(x) for x in orig_rows])
    for i in range(len(rows)):
        gap = ' ' * (width - len(orig_rows[i]))
        print(orig_rows[i], gap, end='\t')
        print(rows[i])

    backtrack = interpret(result, keys)
    print(f'\n\nREVERSE RESULT:\n{backtrack}')
    print(text == backtrack)
