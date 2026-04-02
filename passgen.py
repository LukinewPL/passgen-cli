import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--length', type=int, default=16)
parser.add_argument('--count', type=int, default=1)
parser.add_argument('--no-symbols', action='store_true')
parser.add_argument('--no-digits', action='store_true')

args = parser.parse_args()

def generate(length, count, no_symbols, no_digits):
    import secrets
    import string
    
    if length < 1:
        print('Password length must be at least 1')
        return
    if count < 1:
        print('Password count must be at least 1')
        return
    
    alphabet = string.ascii_letters
    if not no_digits:
        alphabet += string.digits
    if not no_symbols:
        alphabet += string.punctuation
    
    if not alphabet:
        print('No characters available to generate password')
        return
    
    for _ in range(count):
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        print(password)

if __name__ == '__main__':
    generate(args.length, args.count, args.no_symbols, args.no_digits)