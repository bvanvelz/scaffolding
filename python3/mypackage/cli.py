import argparse
from datetime import datetime
import sys

VERSION = 1.0

def process_args(args):
	parser = argparse.ArgumentParser(description='CLI scaffolding.')
	parser.add_argument('--version', action='version', version=str(VERSION))
	parser.add_argument('-f', '--flag', action='store_true',
		                help='flag desc')
	parser.add_argument('args', metavar='N', type=int, nargs=1,
	                    help='args desc')
	parser.add_argument('--option', dest='option1_dest',
		                help='option1 desc')

	return parser.parse_args(args)

def get_datestr():
	return datetime.now().strftime('%Y-%m-%d')

def main(args):
	print("Command line args: {}".format(args))

	print("Current datestr: {}".format(get_datestr()))

if __name__ == "__main__":
	args = process_args(sys.argv[1:])
	main(args)