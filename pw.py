import argparse
from datetime import date
import random

parser = argparse.ArgumentParser()

parser.add_argument("--length", "--len",
                    help="Length of password", default=12, type=int)
parser.add_argument(
    "--save", "--s", help="enable save password", action="store_true")
parser.add_argument("--name", "--n", help="give name to this password",
                    type=str, default=date.today())

parser.add_argument("--no-char", '--nc',
                    help="disable special characters", action="store_true")


args = parser.parse_args()

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
chars = "~!@#$%^&*()_+[]{}|.<>/?"


selection = "" if args.no_char else chars

selection += "".join([alpha, alpha.lower(), nums])

pw = ""

while len(pw) < args.length:
    index = random.randint(0, len(selection) - 1)
    pw += selection[index]

if args.save:
    name = args.name
    file = open("password.txt", "a")
    file.write(f'{name}: {pw}\n')
    file.close()


print(pw)
