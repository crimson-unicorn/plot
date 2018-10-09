import os, sys
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
import matplotlib.ticker as ticker
import numpy as np

def import_data(filepath):
	"""
	Import data file @filepath to plot. 
	"""
	data = []
	with open(filepath, "r") as f:
		for line in f:
			data.append(int(line.strip()))
	return data

def plot_stream_vs_analyze(stream_data, analyze_data):
	"""
	Plot the stream speed vs analyze speed graph.
	"""
	fig, ax = plt.subplots()
	# create x-axes for both plots
	stream_time_data = np.arange(1, len(stream_data) + 1)
	analyze_time_data = np.arange(1, len(analyze_data) + 1)
	# plot both lines
	stream_line, = ax.plot(stream_time_data, stream_data)
	analyze_line, = ax.plot(analyze_time_data, analyze_data)
	# set x-axis ticks to be every 10 seconds 
	ax.xaxis.set_major_locator(ticker.MultipleLocator(15))
	# set x-axis smallest value to be 0
	ax.set_xlim(left=0)
	# set y-axis smallest value to be 0
	ax.set_ylim(bottom=0)
	# tick appearance
	ax.tick_params(axis='x', labelrotation=45)
	# create legend for both lines
	ax.legend((stream_line, analyze_line), ('Stream', 'Analyze'), loc='lower right', shadow=False)
	# set labels
	ax.set_xlabel('Time (seconds)')
	ax.set_ylabel('Graph Size (# of Edges)')

	plt.savefig("../plot/stream_analyze.pdf", format='pdf', bbox_inches='tight')


def print_instruction():
	print(
		"Usage: python plot.py\n")

if __name__ == "__main__":
	
	if (len(sys.argv) < 1):
		print_instruction()
		sys.exit(1)

	stream_data = import_data("../data/stream-wget-attack-baseline-0.txt")
	analyze_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-2000.txt")
	plot_stream_vs_analyze(stream_data, analyze_data)
