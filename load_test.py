from polysub import *

# Load from files
with open('result.txt') as file:
    text = file.read()

with open('key.txt') as file:
    keys_string = file.read()

# Build objects and interpret
keys = keys_from_string(keys_string)
interpreted = interpret(text, keys)

# Print results
print("KEYS:")
print(default_string())
for key in keys:
    print(keystring(key))

print(f'\nSOURCE:\n{text}')
print(f'\n\nRESULT:\n{interpreted}')
