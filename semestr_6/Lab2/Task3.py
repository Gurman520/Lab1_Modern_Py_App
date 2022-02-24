import argparse

parser = argparse.ArgumentParser()

parser.add_argument("args_s", type=str, nargs='*', default="no args")

args = parser.parse_args()
if "no args" in args.args_s:
    print("no args")
else:
    for arg in args.args_s:
        print(arg)
