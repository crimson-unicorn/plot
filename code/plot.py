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


def import_float_data(filepath):
	"""
	Import data file @filepath to plot. 
	"""
	data = []
	with open(filepath, "r") as f:
		for line in f:
			data.append(float(line.strip()))
	return data


def plot_multilines(data_arrays, tick_interval, xlabelrotation, color_array, linestyle_array, markerstyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath, need_legend=True, need_right_x_lim=True):
	"""
	Plot multiple lines (all encompassed in @data_arrays) in the same figure.
	x ticks have interval @tick_interval, and the tick labels are rotated at the angle @xlabelrotation.
	Each line has legend included in @legend_array which is located at @legend_loc, color style @color_array, line style @linestyle_array, and marker style @markerstyle_array.
	x and y labels are named by @xlabel_str and @ylabel_str.
	The resulting plot is saved in @savefilepath.
	"""
	fig, ax = plt.subplots()
	# create x-axes for all plots in @data_arrays and plot all of them
	for pos, line in enumerate(data_arrays):
		marker_style = dict(color=color_array[pos], linestyle=linestyle_array[pos], marker=markerstyle_array[pos], markevery=tick_interval)
		timeline = np.arange(1, len(line) + 1)
		draw_line = ax.plot(timeline, line, label=legend_array[pos], **marker_style)
	# set x-axis ticks to be every @tick_interval 
	ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
	# set x-axis smallest value to be 0
	if need_right_x_lim:
		ax.set_xlim(left=0, right=475)
	else:
		ax.set_xlim(left=0)
	# set y-axis smallest value to be 0
	ax.set_ylim(bottom=0)
	# tick appearance
	ax.tick_params(axis='x', labelrotation=xlabelrotation)
	# create legend for both lines
	if need_legend:
		ax.legend(loc=legend_loc, shadow=False)
	# set labels
	ax.set_xlabel(xlabel_str)
	ax.set_ylabel(ylabel_str)

	plt.savefig(savefilepath, format='pdf', bbox_inches='tight')


def plot_scatters(data_arrays, tick_interval, xlabelrotation, color_array, markerstyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath, need_legend, need_upper_y_lim=False):
	fig, ax = plt.subplots()
	# create x-axes for all plots in @data_arrays and plot all of them
	for pos, line in enumerate(data_arrays):
		scatter_style = dict(color=color_array[pos], s=10, marker=markerstyle_array[pos])
		timeline = np.arange(1, len(line) + 1)
		draw_line = ax.scatter(timeline, line, label=legend_array[pos], **scatter_style)
	# set x-axis ticks to be every @tick_interval 
	ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
	# set x-axis smallest value to be 0
	ax.set_xlim(left=0)
	# set y-axis smallest value to be 0
	if need_upper_y_lim:
		ax.set_ylim(bottom=0, top=100)
	else:
		ax.set_ylim(bottom=0)
	# tick appearance
	ax.tick_params(axis='x', labelrotation=xlabelrotation)
	# create legend for both lines
	if need_legend:
		ax.legend(loc=legend_loc, shadow=False)
	# set labels
	ax.set_xlabel(xlabel_str)
	ax.set_ylabel(ylabel_str)

	plt.savefig(savefilepath, format='pdf', bbox_inches='tight')


def plot_hist(data_arrays, color_array, legend_array, x_tick_array, xlabel_str, ylabel_str, savefilepath, with_legend):
	# the x locations for each group
	ind = np.arange(len(data_arrays[0]))
	width = 0.15 	# the width of the bars

	fig, ax = plt.subplots(figsize=(6, 2))
	hist1 = ax.bar(ind - 3*width/2, data_arrays[0], width, color=color_array[0], label=legend_array[0])
	hist2 = ax.bar(ind - width/2, data_arrays[1], width, color=color_array[1], label=legend_array[1])
	hist3 = ax.bar(ind + width/2, data_arrays[2], width, color=color_array[2], label=legend_array[2])
	hist4 = ax.bar(ind + 3*width/2, data_arrays[3], width, color=color_array[3], label=legend_array[3])

	# set labels
	ax.set_xlabel(xlabel_str)
	ax.set_ylabel(ylabel_str)
	ax.set_xticks(ind)
	ax.set_xticklabels(x_tick_array)
	if with_legend:
		ax.legend(loc=9, prop={'size': 6}, bbox_to_anchor=(0.5, -0.3), ncol = 4)

	plt.savefig(savefilepath, format='pdf', bbox_inches='tight')


def plot_perf(data_arrays, tick_interval, xlabelrotation, color_array, linestyle_array, markerstyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath, need_legend=True, need_right_x_lim=True, y_value_interval=2000):
	"""Plot CamFlow vs Unicorn performance data. i.e., the number of edges each system processes v.s. the time it takes.
	"""
	fig, ax = plt.subplots()
	# create y-axes for all plots in @data_arrays and plot all of them
	for pos, line in enumerate(data_arrays):
		marker_style = dict(color=color_array[pos], linestyle=linestyle_array[pos], marker=markerstyle_array[pos], markevery=tick_interval, markersize=0.5)
		y_value = list()
		for i in range(len(line)):
			y_value.append(y_value_interval * (i + 1))
		draw_line = ax.plot(line, y_value, label=legend_array[pos], **marker_style)
	# create legend for both lines
	if need_legend:
		ax.legend(loc=legend_loc, shadow=False)
	# tick appearance
	ax.tick_params(axis='x', labelrotation=xlabelrotation)
	# set labels
	ax.set_xlabel(xlabel_str)
	ax.set_ylabel(ylabel_str)

	plt.savefig(savefilepath, format='pdf', bbox_inches='tight')


def print_instruction():
	print(
		"Usage: python plot.py\n")


if __name__ == "__main__":
	
	if (len(sys.argv) < 1):
		print_instruction()
		sys.exit(1)

	camflow_perf_data = import_float_data("out.txt")
	unicorn_perf_data = import_float_data("stats.txt")
	data_arrays = [camflow_perf_data, unicorn_perf_data]
	plot_perf(data_arrays, 1, 0, ['#1f77b4', '#ff7f0e'], ['-', '-'], ['.', '.'], ['camflow', 'unicorn'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "graph.pdf")
	sys.exit(1)

	# plot the performance between streaming and analyzing
	stream_data = import_data("../data/stream-wget-attack-baseline-0.txt")
	# analyze_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-2000.txt")
	# data_arrays = [stream_data, analyze_data]
	# plot_multilines(data_arrays, 25, 45, ['--', '-'], ['.', '.'], ['stream', 'analyze'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/stream_analyze.pdf")

	# plot the performance with different hop counts
	hop1_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-1-w-450-i-3000.txt")
	hop2_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-2-w-450-i-3000.txt")
	hop3_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-3000.txt")
	hop4_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-4-w-450-i-3000.txt")
	hop5_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-5-w-450-i-3000.txt")
	data_arrays = [stream_data, hop1_data, hop2_data, hop3_data, hop4_data, hop5_data]
	plot_multilines(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], ['--', '-', '-', '-', '-', '-'], ['.', '|', 'x', '*', 'o', '^'], ['stream', 'Hop = 1', 'Hop = 2', 'Hop = 3 (Baseline)', 'Hop = 4', 'Hop = 5'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/hop.pdf")

	# plot the performance with various sketch sizes
	sketch1_data = import_data("../data/perf-wget-attack-baseline-0-s-500-h-3-w-450-i-3000.txt")
	sketch2_data = import_data("../data/perf-wget-attack-baseline-0-s-1000-h-3-w-450-i-3000.txt")
	sketch3_data = import_data("../data/perf-wget-attack-baseline-0-s-1500-h-3-w-450-i-3000.txt")
	sketch4_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-3000.txt")
	sketch5_data = import_data("../data/perf-wget-attack-baseline-0-s-3000-h-3-w-450-i-3000.txt")
	data_arrays = [stream_data, sketch1_data, sketch2_data, sketch3_data, sketch4_data, sketch5_data]
	plot_multilines(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#d62728', '#8c564b'], ['--', '-', '-', '-', '-', '-'], ['.', '|', 'x', 'o', '*', '^'], ['stream', '|S| = 500', '|S| = 1,000', '|S| = 1,500', '|S| = 2,000 (Baseline)', '|S| = 3,000'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/sketch.pdf")

	# plot the performance with various batch sizes
	batch1_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-1500.txt")
	batch2_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-2000.txt")
	batch3_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-3000.txt")
	batch4_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-5000.txt")
	batch5_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-10000.txt")
	data_arrays = [stream_data, batch1_data, batch2_data, batch3_data, batch4_data, batch5_data]
	plot_multilines(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#8c564b', '#9467bd'], ['--', '-', '-', '-', '-', '-'], ['.', '|', 'x', '*', 'o', '^'], ['stream', 'Batch = 1,500', 'Batch = 2,000', 'Batch = 3,000 (Baseline)', 'Batch = 5,000', 'Batch = 10,000'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/batch.pdf")

	# plot the performance with various window sizes
	window1_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-200-i-3000.txt")
	window2_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-450-i-3000.txt")
	window3_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-500-i-3000.txt")
	window4_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-1000-i-3000.txt")
	window5_data = import_data("../data/perf-wget-attack-baseline-0-s-2000-h-3-w-2000-i-3000.txt")
	data_arrays = [stream_data, window1_data, window2_data, window3_data, window4_data, window5_data]
	plot_multilines(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#d62728', '#2ca02c', '#9467bd', '#8c564b'], ['--', '-', '-', '-', '-', '-'], ['.', '|', '*', 'x', 'o', '^'], ['stream', 'Interval = 200', 'Interval = 450 (Baseline)', 'Interval = 500', 'Interval = 1,000', 'Interval = 2,000'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/interval.pdf")

	# plot the eval with various hop counts
	hop1_data = import_float_data("../data/hop-precision-perf.txt")
	hop2_data = import_float_data("../data/hop-recall-perf.txt")
	hop3_data = import_float_data("../data/hop-accuracy-perf.txt")
	hop4_data = import_float_data("../data/hop-f-measure-perf.txt")
	data_arrays = [hop1_data, hop2_data, hop3_data, hop4_data]
	plot_hist(data_arrays, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['Precision', 'Recall', 'Accuracy', 'F-Score'], ['1', '2', '3 (Baseline)', '4', '5'], 'Hops', 'Rate', "../plot/hop-eval.pdf", True)

	# plot the eval with various sketch sizes
	sketch1_data = import_float_data("../data/sketch-precision-perf.txt")
	sketch2_data = import_float_data("../data/sketch-recall-perf.txt")
	sketch3_data = import_float_data("../data/sketch-accuracy-perf.txt")
	sketch4_data = import_float_data("../data/sketch-f-measure-perf.txt")
	data_arrays = [sketch1_data, sketch2_data, sketch3_data, sketch4_data]
	plot_hist(data_arrays, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['Precision', 'Recall', 'Accuracy', 'F-Score'], ['500', '1000', '1500', '2000 (Baseline)', '3000'], 'Sketch Size', 'Rate', "../plot/sketch-eval.pdf", False)

	# plot the eval with various window sizes
	window1_data = import_float_data("../data/window-precision-perf.txt")
	window2_data = import_float_data("../data/window-recall-perf.txt")
	window3_data = import_float_data("../data/window-accuracy-perf.txt")
	window4_data = import_float_data("../data/window-f-measure-perf.txt")
	data_arrays = [window1_data, window2_data, window3_data, window4_data]
	plot_hist(data_arrays, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['Precision', 'Recall', 'Accuracy', 'F-Score'], ['200', '450 (Baseline)', '500', '1000', '2000'], 'Interval', 'Rate', "../plot/window-eval.pdf", False)

	# plot CPU usage for various hop counts
	hop1_data = import_float_data("../data/cpu-s-2000-h-1-w-450-i-3000.txt")
	hop2_data = import_float_data("../data/cpu-s-2000-h-2-w-450-i-3000.txt")
	hop3_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-3000.txt")
	hop4_data = import_float_data("../data/cpu-s-2000-h-4-w-450-i-3000.txt")
	hop5_data = import_float_data("../data/cpu-s-2000-h-5-w-450-i-3000.txt")
	data_arrays = [hop1_data, hop2_data, hop3_data, hop4_data, hop5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['Hop = 1', 'Hop = 2', 'Hop = 3 (Baseline)', 'Hop = 4', 'Hop = 5'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/cpu-hop.pdf", True, True)

	# plot Memory usage for various hop counts
	hop1_data = import_float_data("../data/mem-s-2000-h-1-w-450-i-3000.txt")
	hop2_data = import_float_data("../data/mem-s-2000-h-2-w-450-i-3000.txt")
	hop3_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-3000.txt")
	hop4_data = import_float_data("../data/mem-s-2000-h-4-w-450-i-3000.txt")
	hop5_data = import_float_data("../data/mem-s-2000-h-5-w-450-i-3000.txt")
	data_arrays = [hop1_data, hop2_data, hop3_data, hop4_data, hop5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['Hop = 1', 'Hop = 2', 'Hop = 3 (Baseline)', 'Hop = 4', 'Hop = 5'], 'upper left', 'Time (seconds)', 'Memory Usage (MB)', "../plot/mem-hop.pdf", True)

	# plot CPU usage for various sketch sizes
	sketch1_data = import_float_data("../data/cpu-s-500-h-3-w-450-i-3000.txt")
	sketch2_data = import_float_data("../data/cpu-s-1000-h-3-w-450-i-3000.txt")
	sketch3_data = import_float_data("../data/cpu-s-1500-h-3-w-450-i-3000.txt")
	sketch4_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-3000.txt")
	sketch5_data = import_float_data("../data/cpu-s-3000-h-3-w-450-i-3000.txt")
	data_arrays = [sketch1_data, sketch2_data, sketch3_data, sketch4_data, sketch5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['|S| = 500', '|S| = 1,000', '|S| = 1,500', '|S| = 2,000 (Baseline)', '|S| = 3,000'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/cpu-sketch.pdf", True, True)

	# plot Memory usage for various sketch sizes
	sketch1_data = import_float_data("../data/mem-s-500-h-3-w-450-i-3000.txt")
	sketch2_data = import_float_data("../data/mem-s-1000-h-3-w-450-i-3000.txt")
	sketch3_data = import_float_data("../data/mem-s-1500-h-3-w-450-i-3000.txt")
	sketch4_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-3000.txt")
	sketch5_data = import_float_data("../data/mem-s-3000-h-3-w-450-i-3000.txt")
	data_arrays = [sketch1_data, sketch2_data, sketch3_data, sketch4_data, sketch5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['|S| = 500', '|S| = 1,000', '|S| = 1,500', '|S| = 2,000 (Baseline)', '|S| = 3,000'], 'upper left', 'Time (seconds)', 'Memory Usage (MB)', "../plot/mem-sketch.pdf", True)

	# plot CPU usage for various batch sizes
	batch1_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-1500.txt")
	batch2_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-2000.txt")
	batch3_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-3000.txt")
	batch4_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-5000.txt")
	batch5_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-10000.txt")
	data_arrays = [batch1_data, batch2_data, batch3_data, batch4_data, batch5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['Batch = 1,500', 'Batch = 2,000', 'Batch = 3,000 (Baseline)', 'Batch = 5,000', 'Batch = 10,000'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/cpu-batch.pdf", True, True)

	# plot Memory usage for various batch sizes
	batch1_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-1500.txt")
	batch2_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-2000.txt")
	batch3_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-3000.txt")
	batch4_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-5000.txt")
	batch5_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-10000.txt")
	data_arrays = [batch1_data, batch2_data, batch3_data, batch4_data, batch5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['Batch = 1,500', 'Batch = 2,000', 'Batch = 3,000 (Baseline)', 'Batch = 5,000', 'Batch = 10,000'], 'upper left', 'Time (seconds)', 'Memory Usage (MB)', "../plot/mem-batch.pdf", True)

	# plot CPU usage for various intervals
	window1_data = import_float_data("../data/cpu-s-2000-h-3-w-200-i-3000.txt")
	window2_data = import_float_data("../data/cpu-s-2000-h-3-w-450-i-3000.txt")
	window3_data = import_float_data("../data/cpu-s-2000-h-3-w-500-i-3000.txt")
	window4_data = import_float_data("../data/cpu-s-2000-h-3-w-1000-i-3000.txt")
	window5_data = import_float_data("../data/cpu-s-2000-h-3-w-2000-i-3000.txt")
	data_arrays = [window1_data, window2_data, window3_data, window4_data, window5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['Interval = 200', 'Interval = 450 (Baseline)', 'Interval = 500', 'Interval = 1,000', 'Interval = 2,000'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/cpu-interval.pdf", True, True)

	# plot Memory usage for various intervals
	window1_data = import_float_data("../data/mem-s-2000-h-3-w-200-i-3000.txt")
	window2_data = import_float_data("../data/mem-s-2000-h-3-w-450-i-3000.txt")
	window3_data = import_float_data("../data/mem-s-2000-h-3-w-500-i-3000.txt")
	window4_data = import_float_data("../data/mem-s-2000-h-3-w-1000-i-3000.txt")
	window5_data = import_float_data("../data/mem-s-2000-h-3-w-2000-i-3000.txt")
	data_arrays = [window1_data, window2_data, window3_data, window4_data, window5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', 'o'], ['Interval = 200', 'Interval = 450 (Baseline)', 'Interval = 500', 'Interval = 1,000', 'Interval = 2,000'], 'upper left', 'Time (seconds)', 'Memory Usage (MB)', "../plot/mem-interval.pdf", True)







