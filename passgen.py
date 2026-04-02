import click
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('generate', help='Generate a password')
parser.add_argument('--length', default=16, help='Password length')
parser.add_argument('--count', default=1, help='Password count')
parser.add_argument('--no-symbols', default=False, help='If password has symbols')
parser.add_argument('--no-digits', default=False, help='If password has digits')
parser.parse_args()

@click.group()
def cli():
    pass

@click.command()
@click.option('--length', default=16, help='Password length')
@click.option('--count', default=1, help='Password count')
@click.option('--no-symbols', default=False, help='If password has symbols')
@click.option('--no-digits', default=False, help='If password has digits')
def generate(length, count, no_symbols, no_digits):
    import secrets
    import string
    
    alphabet = string.ascii_letters
    if not no_digits:
        alphabet += string.digits
    if not no_symbols:
        alphabet += string.punctuation
    
    for _ in range(count):
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        click.echo(password)

cli.add_command(generate)

if __name__ == '__main__':
    cli()