# Cryptogrophy Implementations

This is a collection of some simple implementations I've done from working through **Applied Cryptography by Bruce Schnieier**:
https://www.schneier.com/books/applied-cryptography/


---

## Polysub - Polyalphabetic Substitution Cypher

Similar to a [simple substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher), but uses multiple cipher keys. To encrypt a text a process of *"rolling"* through the ciphers for each character in the original text is used.
To decrypt simply use the same process for decrypting a simple substitution cipher, making sure to *"roll"* through the ciphers in the same order and starting position.

#### Implementation Notes
For simplicity I'm ignoring special characters and only building ciphers to include characters that appear on a standard ascii keyboard (see *default_string()*).
This allows easier storing for ciphers as plaintext to make this process a little easier to follow along with.
