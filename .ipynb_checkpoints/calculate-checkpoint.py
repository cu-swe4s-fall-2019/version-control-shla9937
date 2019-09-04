import argparse
import math_lib as ml

parser = argparse.ArgumentParser(description='do math')
parser.add_argument('first_number', type=int, help='First Number')
parser.add_argument('second_number', type=int, help='Second Number')
args = parser.parse_args()

if __name__ == '__main__':
    print(ml.add(args.first_number, args.second_number))
    print(ml.div(args.first_number, args.second_number))