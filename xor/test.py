from xor import xor

key = 123

with open('zen.txt', 'rb') as file:
    text = file.read()
    print(text)

encrypted = xor(text, key)
decrypted = xor(encrypted, key)
print(encrypted)
print(decrypted)
