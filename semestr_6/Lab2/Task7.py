import argparse
import os.path

parser = argparse.ArgumentParser()

parser.add_argument("--count", action="store_true", default=False)

parser.add_argument("--num", action="store_true", default=False)

parser.add_argument("--sort", action="store_true", default=False)

parser.add_argument("file", type=str, default="no_files")

args = parser.parse_args()
if not os.path.isfile(args.file):
    print("Error")
else:
    string = []
    with open(args.file) as file:
        for line in file:
            string.append(line)
    if args.sort:
        string.sort()
    if args.num:
        co = 0
        for i in range(len(string)):
            string[i] = f'{co} ' + string[i]
            co += 1
    if args.count:
        string.append("Количество строк: " + f'{len(string)}')
    for s in string:
        print(s, end='')

