"""Time a Function"""
import argparse
import timeit
import aoc

parser = argparse.ArgumentParser()
parser.add_argument("--fun", type=str, required=True)
parser.add_argument("--inp", type=str, required=True)
parser.add_argument("--num", type=int, default=1000)
args, optional_args = parser.parse_known_args()

with open(args.inp, encoding="utf-8") as f:
    inp = f.read()

print(timeit.timeit(lambda: getattr(aoc, args.fun)(inp, *optional_args), number=args.num))
