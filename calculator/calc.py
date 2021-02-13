import argparse
import math


class OpParser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Calculator")
        self.parser.add_argument('-sqrt',
                                 '--square_root',
                                 type=float,
                                 help="float value to find its sq root")
        self.parser.add_argument('-fact',
                                 '--factorial',
                                 type=int,
                                 help="int value to find its factorial root")
        self.parser.add_argument('-pow',
                                 '--power',
                                 nargs=2,
                                 type=float,
                                 help="Enter 2 float values a, b to find the value of a^b")

        self.parse_op = self.parser.parse_args()


class CalcOperations:
    @staticmethod
    def sqrt(val: float):
        return math.sqrt(val)

    @staticmethod
    def fact(val: int):
        return math.factorial(val)

    @staticmethod
    def pow(base: float, exp: float):
        return math.pow(base, exp)


def main():
    parser = OpParser()
    args = parser.parse_op
    print(args)

    if args.square_root:
        val = args.square_root
        try:
            ans = CalcOperations.sqrt(val)
            print(f"sqrt({val}) = {ans}")
        except Exception as e:
            print(f"failed to calculate sqrt({val})", e)

    if args.factorial:
        val = args.factorial
        try:
            ans = CalcOperations.fact(val=val)
            print(f"factorial({val}) = {ans}")
        except Exception as e:
            print(f"failed to calculate factorial({val})", e)

    if args.power:
        base = args.power[0]
        exp = args.power[1]
        try:
            ans = CalcOperations.pow(base=base, exp=exp)
            print(f"pow({base}, {exp}) = {ans}")
        except Exception as e:
            print(f"failed to calculate pow({base}, {exp})", e)


if __name__ == "__main__":
    main()
