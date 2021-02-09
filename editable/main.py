import os
import img2pdf
import argparse
from utils import *


def main():
	input_path = params.get('f')



if __name__ == "__main__":
	parser =  argparse.ArgumentParser(description = "tool name")
	parser.add_argument('-f', metavar = '-file', type=str, help='')
	params = vars(parser.parse_args())
	print(params)
	main()