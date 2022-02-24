import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sort", action="store_true", default=False)

parser.add_argument("n_v", type=str, nargs='+')

args = parser.parse_args()
Dicts = dict()
for arg in args.n_v:
    s = arg.find("=")
    Dicts[arg[0:s]] = arg[s + 1:]
if args.sort:
    Dicts = dict(sorted(Dicts.items(), key=lambda x: x[0]))
for dic in Dicts:
    print("Key: " + dic + " Value: " + Dicts[dic])
