import argparse
import pycpp
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('DLLname', metavar='DLL', type=str, help='The name of the dll to wrap')
parser.add_argument('Out', metavar='out', type=str, help='The output directory')

args = parser.parse_args()
pycpp.wrap(args.DLLname, args.Out)
