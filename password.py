import json
import argparse

parser = argparse.ArgumentParser(description='Easy password.')
parser.add_argument('--key', type=str, help='name of password')

if __name__ == '__main__':
    args = parser.parse_args()
    name = args.key
    passwords = json.load(open('password.json'))
    print(passwords[name])

