"""In crimson-unicorn (https://github.com/crimson-unicorn) repoistories, `parsers/camflow/parse.py` generates a `ts.txt` file.
This file records the time it takes for Unicorn to generate 2000 edges for a specific experiment.
Since the timing information is an approximation, we run this program to clean it up.
We make sure later timestamps, if shown as smaller values than previous largest timestamps,
we modify the timestamps to the largest timestamp available.

e.g.,
>>> Original data:
1
2
4
9
5
5
7
12
<<< Cleaned up data:
1
2
4
9
9
9
9
12
"""
from __future__ import print_function
import os, sys, argparse

def clean_up(ifp, ofp):
	out = open(ofp, 'w')
	current = 0.0
	with open(ifp, 'r') as f:
		for line in f:
			try:
				data = float(line.strip())
			except Exception as e:
				print("Dirty value: {}".format(e))
				raise RuntimeError("encountered a dirty value")
			if data > current:
				current = data
			elif data < current:
				data = current
			out.write(str(data) + '\n')
	out.close()
	f.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Clean up CamFlow Performance Numbers.')
	parser.add_argument('-i', '--input', help='input data file path', required=True)
	parser.add_argument('-o', '--output', help='output data file path',  required=True)
	args = parser.parse_args()

	clean_up(args.input, args.output)
