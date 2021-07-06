
def compress(s):
    '''
    Takes a string and removes the header bit.
    NOTE: since all ascii chars are only defined in 7 bits,
    the 8th bit can be dropped.
    Zero-bits are used to fill the remainder of the last byte.
    '''
    # out = b''
    # for char in s:
    #     out += char.to_bytes(2, 'lower')
    # return out

    # return bytes(s, 'ascii')
    # return ''.join('{:02x}'.format(ord(c)) for c in s)

    bins = [bin(ord(x)) for x in s]
    small = ''
    for b in bins:
        small += b[3:]
    return small


if __name__ == '__main__':
    text = 'Hello, World!'
    out = compress(text)
    print(out)
    print(type(out[0]))
    print(len(text))
    print(f'Original total bits: {len(text) * 8}')
    print(f'Estimated final total bits: {len(text) * 7}')
    print(len(out))