import argparse
import struct

parser = argparse.ArgumentParser()

parser.add_argument("arg", type=str, nargs='*', default="no args")

args = parser.parse_args()
try:
    if args.arg == "no args":
        print("NO PARAMS")
    elif len(args.arg) > 2:
        print("TOO MANY PARAMS")
    elif len(args.arg) < 2:
        print("TOO FEW PARAMS")
    else:
        print(int(args.arg[0]) + int(args.arg[1]))
except Exception as exception:
    assert type(exception).__name__ == 'NameError'


