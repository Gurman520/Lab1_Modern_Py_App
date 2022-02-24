import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file_in", type=str)

parser.add_argument("file_out", type=str)

parser.add_argument("--upper", action="store_true", default=False)

parser.add_argument("--lines", type=int, default=90000)

args = parser.parse_args()
f_out = open(args.file_out, 'w')
with open(args.file_in) as f_in:
    count = 0
    for line in f_in:
        if count < args.lines:
            if args.upper:
                line = line.upper()
            f_out.write(line)
            count += 1
f_out.close()
