# PRODIGY_CS_01
A simple tool to encrypt/decrypt a text using the caesar cipher algorithm.

## Task
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

## Running the program
Encrypting a plaintext
```
python caesar.py -e <text> -k <key>
```

Example
```
python caesar.py -e "Hi Mom!" -k 13

Uv Zbz!
```

Decrypting a ciphertext
```
python caesar.py -d <text> -k <key>
```

Example
```
python caesar.py -d "Uv Zbz!" -k 13

Hi Mom!
```
