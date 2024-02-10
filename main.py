from colorama import Fore
import argparse

pyFLLW = f"{Fore.GREEN}pyFLLW {Fore.CYAN}>>"

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', nargs='?', help='Specify filename')
parser.add_argument('flags', nargs='*', help='Specify flags')
args = parser.parse_args()
filename = args.filename
flags = args.flags
print("Filename:", filename)
print("Flags:", flags)
