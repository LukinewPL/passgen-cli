import argparse
import string
import secrets

parser = argparse.ArgumentParser()

parser.add_argument('--length', type=int, default=16)
parser.add_argument('--count', type=int, default=1)
parser.add_argument('--no-symbols', action='store_true')
parser.add_argument('--no-digits', action='store_true')

def create_alphabet(no_symbols, no_digits):
    alphabet = string.ascii_letters
    if not no_digits:
        alphabet += string.digits
    if not no_symbols:
        alphabet += string.punctuation
    
    return alphabet

def generate_password(length, alphabet):
    if length < 1:
         raise ValueError('Password length must be at least 1')
    if not alphabet:
        raise ValueError('Alphabet cannot be empty')

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_passwords(length, count, alphabet):
    if count < 1:
        raise ValueError('Password count must be at least 1')
    return [generate_password(length, alphabet) for _ in range(count)]

if __name__ == '__main__':
    args = parser.parse_args()

    alphabet = create_alphabet(args.no_symbols, args.no_digits)
    passwords = generate_passwords(args.length, args.count, alphabet)
    for password in passwords:
        print(password)