import argparse
import os.path

parser = argparse.ArgumentParser()

parser.add_argument("--per-day", type=float, default=0, dest="day")

parser.add_argument("--per-week", type=float, default=0, dest="week")

parser.add_argument("--per-month", type=float, default=0, dest="month")

parser.add_argument("--per-year",  type=float, default=0, dest="year")

parser.add_argument("--get-by", choices=["day", "month", "year"], dest="get_by", type=str, default="day")

args = parser.parse_args()
sum = 0
if args.get_by == "day":
    sum += args.day + (args.week / 7)
    sum += args.month / 30 + args.year / 360
    print(sum)
elif args.get_by == "month":
    sum += args.day * 30 + args.week * (30 / 7)
    sum += args.month + args.year / 12
    print(sum)
elif args.get_by == "year":
    sum += args.day * 360 + args.week * (360 / 7)
    sum += args.month * 12 + args.year
    print(sum)

