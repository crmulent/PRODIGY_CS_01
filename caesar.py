import argparse
from src.encrypt import encrypt
from src.decrypt import decrypt

def main():
    parser = argparse.ArgumentParser(
        description='Caesar Cipher encrypt or decrypt a string to standard output.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', type=str, metavar='plaintext', help='text to encrypt')
    group.add_argument('-d', type=str, metavar='ciphertext', help='text to decrypt')
    parser.add_argument('-k', type=int, metavar='key', help='key used for shifting', required=True)

    args = parser.parse_args()

    if args.e:
        text = args.e
        encrypt(text, args.k)
    elif args.d:
        text = args.d
        decrypt(text, args.k)

if __name__ == "__main__":
    main()
