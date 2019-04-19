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


def plot_multilines_x(x_arrays, data_arrays, tick_interval, xlabelrotation, color_array, linestyle_array, markerstyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath, need_legend=True, need_right_x_lim=True, linewidth=0.5):
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
		marker_style = dict(color=color_array[pos], linestyle=linestyle_array[pos], linewidth=linewidth)
		draw_line = ax.plot(x_arrays[pos], line, label=legend_array[pos], **marker_style)
	# set x-axis ticks to be every @tick_interval 
	ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
	# set x-axis smallest value to be 0
	if need_right_x_lim:
		ax.set_xlim(left=0)
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

def plot_scatters_legend_out(data_arrays, tick_interval, xlabelrotation, color_array, markerstyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath, need_legend, need_upper_y_lim=False):
	"""
	Same as plot_scatters except legend_loc param is used as "ncol" and legend is located outside the plot box.
	"""
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
		ax.legend(loc=9, prop={'size': 6}, bbox_to_anchor=(0.5, -0.2), ncol = legend_loc)
	# set labels
	ax.set_xlabel(xlabel_str)
	ax.set_ylabel(ylabel_str)

	plt.savefig(savefilepath, format='pdf', bbox_inches='tight')


def plot_scatters_x(x_arrays, data_arrays, tick_interval, xlabelrotation, color_array, markerstyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath, need_legend, need_upper_y_lim=False):
	fig, ax = plt.subplots()
	# create x-axes for all plots in @data_arrays and plot all of them
	for pos, line in enumerate(data_arrays):
		scatter_style = dict(color=color_array[pos], s=10, marker=markerstyle_array[pos])
		x_array = x_arrays[pos]
		draw_line = ax.scatter(x_array, line, label=legend_array[pos], **scatter_style)
	# set x-axis ticks to be every @tick_interval 
	ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
	# set x-axis smallest value to be 0
	ax.set_xlim(left=0)
	# set y-axis smallest value to be 0
	if need_upper_y_lim:
		ax.set_ylim(bottom=0)
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

	# CamFlow data generation speed vs. Unicorn data processing speed w.r.t. window size
	x1_data = import_float_data("../data/perf_speed_camflow/ts-camflow-s-2000-h-3-w-1000-i-6000.txt")
	x2_data = import_float_data("../data/perf_speed_window_unicorn/perf-wget-s-2000-h-3-w-500-i-6000.txt")
	x3_data = import_float_data("../data/perf_speed_window_unicorn/perf-wget-s-2000-h-3-w-1000-i-6000.txt")
	x4_data = import_float_data("../data/perf_speed_window_unicorn/perf-wget-s-2000-h-3-w-3000-i-6000.txt")
	x5_data = import_float_data("../data/perf_speed_window_unicorn/perf-wget-s-2000-h-3-w-5500-i-6000.txt")
	x_arrays = [x1_data, x2_data, x3_data, x4_data, x5_data]
	y1_data = import_float_data("../data/perf_speed_camflow/edge-1000-6000.txt")
	y2_data = import_float_data("../data/perf_speed_window_unicorn/edge-500-6000.txt")
	y3_data = import_float_data("../data/perf_speed_window_unicorn/edge-1000-6000.txt")
	y4_data = import_float_data("../data/perf_speed_window_unicorn/edge-3000-6000.txt")
	y5_data = import_float_data("../data/perf_speed_window_unicorn/edge-5500-6000.txt")
	y_arrays = [y1_data, y2_data, y3_data, y4_data, y5_data]
	plot_multilines_x(x_arrays, y_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['--', '-', '-', '-', '-'], ['.', '.', '.', '.', '.'], ['CamFlow', 'Window = 500', 'Window = 1,000', 'Window = 3,000', 'Window = 5,500'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/perf-speed-camflow-window.pdf")
	
	# CamFlow data generation speed vs. Unicorn data processing speed w.r.t. interval size
	x1_data = import_float_data("../data/perf_speed_camflow/ts-camflow-s-2000-h-3-w-1000-i-6000.txt")
	x2_data = import_float_data("../data/perf_speed_interval_unicorn/perf-wget-s-2000-h-3-w-3000-i-1000.txt")
	x3_data = import_float_data("../data/perf_speed_interval_unicorn/perf-wget-s-2000-h-3-w-3000-i-3000.txt")
	x4_data = import_float_data("../data/perf_speed_interval_unicorn/perf-wget-s-2000-h-3-w-3000-i-6000.txt")
	x5_data = import_float_data("../data/perf_speed_interval_unicorn/perf-wget-s-2000-h-3-w-3000-i-10000.txt")
	x_arrays = [x1_data, x2_data, x3_data, x4_data, x5_data]
	y1_data = import_float_data("../data/perf_speed_camflow/edge-1000-6000.txt")
	y2_data = import_float_data("../data/perf_speed_interval_unicorn/edge-3000-1000.txt")
	y3_data = import_float_data("../data/perf_speed_interval_unicorn/edge-3000-3000.txt")
	y4_data = import_float_data("../data/perf_speed_interval_unicorn/edge-3000-6000.txt")
	y5_data = import_float_data("../data/perf_speed_interval_unicorn/edge-3000-10000.txt")
	y_arrays = [y1_data, y2_data, y3_data, y4_data, y5_data]
	plot_multilines_x(x_arrays, y_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['--', '-', '-', '-', '-'], ['.', '.', '.', '.', '.'], ['CamFlow', 'Interval = 1,000', 'Interval = 3,000', 'Interval = 6,000', 'Interval = 10,000'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/perf-speed-camflow-interval.pdf")
	
	# CamFlow data generation speed vs. Unicorn data processing speed w.r.t. hop size
	x1_data = import_float_data("../data/perf_speed_camflow/ts-camflow-s-2000-h-3-w-1000-i-6000.txt")
	x2_data = import_float_data("../data/perf_speed_hop_unicorn/perf-wget-s-2000-h-1-w-3000-i-6000.txt")
	x3_data = import_float_data("../data/perf_speed_hop_unicorn/perf-wget-s-2000-h-2-w-3000-i-6000.txt")
	x4_data = import_float_data("../data/perf_speed_hop_unicorn/perf-wget-s-2000-h-3-w-3000-i-6000.txt")
	x5_data = import_float_data("../data/perf_speed_hop_unicorn/perf-wget-s-2000-h-4-w-3000-i-6000.txt")
	x6_data = import_float_data("../data/perf_speed_hop_unicorn/perf-wget-s-2000-h-5-w-3000-i-6000.txt")
	x_arrays = [x1_data, x2_data, x3_data, x4_data, x5_data, x6_data]
	y1_data = import_float_data("../data/perf_speed_camflow/edge-1000-6000.txt")
	y2_data = import_float_data("../data/perf_speed_hop_unicorn/edge-3000-6000.txt")
	y_arrays = [y1_data, y2_data, y2_data, y2_data, y2_data, y2_data]
	plot_multilines_x(x_arrays, y_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], ['--', '-', '-', '-', '-', '-'], ['.', '.', '.', '.', '.', '.'], ['CamFlow', 'Hop = 1', 'Hop = 2', 'Hop = 3', 'Hop = 4', 'Hop = 5'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/perf-speed-camflow-hop.pdf")

	# CamFlow data generation speed vs. Unicorn data processing speed w.r.t. sketch size
	x1_data = import_float_data("../data/perf_speed_camflow/ts-camflow-s-2000-h-3-w-1000-i-6000.txt")
	x2_data = import_float_data("../data/perf_speed_sketch_unicorn/perf-wget-s-500-h-3-w-3000-i-6000.txt")
	x3_data = import_float_data("../data/perf_speed_sketch_unicorn/perf-wget-s-1000-h-3-w-3000-i-6000.txt")
	x4_data = import_float_data("../data/perf_speed_sketch_unicorn/perf-wget-s-2000-h-3-w-3000-i-6000.txt")
	x5_data = import_float_data("../data/perf_speed_sketch_unicorn/perf-wget-s-5000-h-3-w-3000-i-6000.txt")
	x6_data = import_float_data("../data/perf_speed_sketch_unicorn/perf-wget-s-10000-h-3-w-3000-i-6000.txt")
	x_arrays = [x1_data, x2_data, x3_data, x4_data, x5_data, x6_data]
	y1_data = import_float_data("../data/perf_speed_camflow/edge-1000-6000.txt")
	y2_data = import_float_data("../data/perf_speed_sketch_unicorn/edge-3000-6000.txt")
	y_arrays = [y1_data, y2_data, y2_data, y2_data, y2_data, y2_data]
	plot_multilines_x(x_arrays, y_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], ['--', '-', '-', '-', '-', '-'], ['.', '.', '.', '.', '.', '.'], ['CamFlow', 'Sketch = 500', 'Sketch = 1,000', 'Sketch = 2,000', 'Sketch = 5,000', 'Sketch = 10,000'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/perf-speed-camflow-sketch.pdf")
	
	# Unicorn CPU usage for various intervals
	interval1_data = import_float_data("../data/perf_cpu_interval_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-1000.txt")
	interval2_data = import_float_data("../data/perf_cpu_interval_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-3000.txt")
	interval3_data = import_float_data("../data/perf_cpu_interval_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-6000.txt")
	interval4_data = import_float_data("../data/perf_cpu_interval_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-10000.txt")
	data_arrays = [interval1_data, interval2_data, interval3_data, interval4_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['.', '|', 'x', '*'], ['Interval = 1,000', 'Interval = 3,000', 'Interval = 6,000', 'Interval = 10,000'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/perf-cpu-camflow-interval.pdf", True, True)
	
	# Unicorn memory usage for various intervals
	interval1_data = import_float_data("../data/perf_mem_interval_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-1000.txt")
	interval2_data = import_float_data("../data/perf_mem_interval_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-3000.txt")
	interval3_data = import_float_data("../data/perf_mem_interval_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-6000.txt")
	interval4_data = import_float_data("../data/perf_mem_interval_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-10000.txt")
	data_arrays = [interval1_data, interval2_data, interval3_data, interval4_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['.', '|', 'x', '*'], ['Interval = 1,000', 'Interval = 3,000', 'Interval = 6,000', 'Interval = 10,000'], 'lower right', 'Time (seconds)', 'Memory Usage (MB)', "../plot/perf-mem-camflow-interval.pdf", True)

	# Unicorn CPU usage for various windows
	window1_data = import_float_data("../data/perf_cpu_window_unicorn/perf-wget-cpu-s-2000-h-3-w-500-i-6000.txt")
	window2_data = import_float_data("../data/perf_cpu_window_unicorn/perf-wget-cpu-s-2000-h-3-w-1000-i-6000.txt")
	window3_data = import_float_data("../data/perf_cpu_window_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-6000.txt")
	window4_data = import_float_data("../data/perf_cpu_window_unicorn/perf-wget-cpu-s-2000-h-3-w-5500-i-6000.txt")
	data_arrays = [window1_data, window2_data, window3_data, window4_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['.', '|', 'x', '*'], ['Window = 500', 'Window = 1,000', 'Window = 3,000', 'Window = 5,500'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/perf-cpu-camflow-window.pdf", True, True)
	
	# Unicorn Memory usage for various windows
	window1_data = import_float_data("../data/perf_mem_window_unicorn/perf-wget-mem-s-2000-h-3-w-500-i-6000.txt")
	window2_data = import_float_data("../data/perf_mem_window_unicorn/perf-wget-mem-s-2000-h-3-w-1000-i-6000.txt")
	window3_data = import_float_data("../data/perf_mem_window_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-6000.txt")
	window4_data = import_float_data("../data/perf_mem_window_unicorn/perf-wget-mem-s-2000-h-3-w-5500-i-6000.txt")
	data_arrays = [window1_data, window2_data, window3_data, window4_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['.', '|', 'x', '*'], ['Window = 500', 'Window = 1,000', 'Window = 3,000', 'Window = 5,500'], 'lower right', 'Time (seconds)', 'Memory Usage (MB)', "../plot/perf-mem-camflow-window.pdf", True)

	# Unicorn CPU usage for various hops
	hop1_data = import_float_data("../data/perf_cpu_hop_unicorn/perf-wget-cpu-s-2000-h-1-w-3000-i-6000.txt")
	hop2_data = import_float_data("../data/perf_cpu_hop_unicorn/perf-wget-cpu-s-2000-h-2-w-3000-i-6000.txt")
	hop3_data = import_float_data("../data/perf_cpu_hop_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-6000.txt")
	hop4_data = import_float_data("../data/perf_cpu_hop_unicorn/perf-wget-cpu-s-2000-h-4-w-3000-i-6000.txt")
	hop5_data = import_float_data("../data/perf_cpu_hop_unicorn/perf-wget-cpu-s-2000-h-5-w-3000-i-6000.txt")
	data_arrays = [hop1_data, hop2_data, hop3_data, hop4_data, hop5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', '8'], ['Hop = 1', 'Hop = 2', 'Hop = 3', 'Hop = 4', 'Hop = 5'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/perf-cpu-camflow-hop.pdf", True, True)
	
	# Unicorn memory usage for various hops
	hop1_data = import_float_data("../data/perf_mem_hop_unicorn/perf-wget-mem-s-2000-h-1-w-3000-i-6000.txt")
	hop2_data = import_float_data("../data/perf_mem_hop_unicorn/perf-wget-mem-s-2000-h-2-w-3000-i-6000.txt")
	hop3_data = import_float_data("../data/perf_mem_hop_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-6000.txt")
	hop4_data = import_float_data("../data/perf_mem_hop_unicorn/perf-wget-mem-s-2000-h-4-w-3000-i-6000.txt")
	hop5_data = import_float_data("../data/perf_mem_hop_unicorn/perf-wget-mem-s-2000-h-5-w-3000-i-6000.txt")
	data_arrays = [hop1_data, hop2_data, hop3_data, hop4_data, hop5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', '8'], ['Hop = 1', 'Hop = 2', 'Hop = 3', 'Hop = 4', 'Hop = 5'], 'lower right', 'Time (seconds)', 'Memory Usage (MB)', "../plot/perf-mem-camflow-hop.pdf", True)

	# Unicorn CPU usage for various sketch sizes
	sketch1_data = import_float_data("../data/perf_cpu_sketch_unicorn/perf-wget-cpu-s-500-h-3-w-3000-i-6000.txt")
	sketch2_data = import_float_data("../data/perf_cpu_sketch_unicorn/perf-wget-cpu-s-1000-h-3-w-3000-i-6000.txt")
	sketch3_data = import_float_data("../data/perf_cpu_sketch_unicorn/perf-wget-cpu-s-2000-h-3-w-3000-i-6000.txt")
	sketch4_data = import_float_data("../data/perf_cpu_sketch_unicorn/perf-wget-cpu-s-5000-h-3-w-3000-i-6000.txt")
	sketch5_data = import_float_data("../data/perf_cpu_sketch_unicorn/perf-wget-cpu-s-10000-h-3-w-3000-i-6000.txt")
	data_arrays = [sketch1_data, sketch2_data, sketch3_data, sketch4_data, sketch5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', '8'], ['Sketch = 500', 'Sketch = 1,000', 'Sketch = 2,000', 'Sketch = 5,000', 'Sketch = 10,000'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/perf-cpu-camflow-sketch.pdf", True, True)
	
	# Unicorn memory usage for various sketch sizes
	sketch1_data = import_float_data("../data/perf_mem_sketch_unicorn/perf-wget-mem-s-500-h-3-w-3000-i-6000.txt")
	sketch2_data = import_float_data("../data/perf_mem_sketch_unicorn/perf-wget-mem-s-1000-h-3-w-3000-i-6000.txt")
	sketch3_data = import_float_data("../data/perf_mem_sketch_unicorn/perf-wget-mem-s-2000-h-3-w-3000-i-6000.txt")
	sketch4_data = import_float_data("../data/perf_mem_sketch_unicorn/perf-wget-mem-s-5000-h-3-w-3000-i-6000.txt")
	sketch5_data = import_float_data("../data/perf_mem_sketch_unicorn/perf-wget-mem-s-10000-h-3-w-3000-i-6000.txt")
	data_arrays = [sketch1_data, sketch2_data, sketch3_data, sketch4_data, sketch5_data]
	plot_scatters(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ['.', '|', 'x', '*', '8'], ['Sketch = 500', 'Sketch = 1,000', 'Sketch = 2,000', 'Sketch = 5,000', 'Sketch = 10,000'], 'upper right', 'Time (seconds)', 'Memory Usage (MB)', "../plot/perf-mem-camflow-sketch.pdf", True)

	# Unicorn CPU usage for an hour-long extended dataset
	extended_data = import_float_data("../data/perf_cpu_extended_unicorn/perf-extended-cpu-s-2000-h-3-w-5500-i-6000.txt")
	data_array = [extended_data]
	plot_scatters(data_array, 150, 45, ['#1f77b4'], ['.'], ['Extended Data'], 'upper right', 'Time (seconds)', '% CPU Usage', "../plot/perf-cpu-camflow-extended.pdf", True, True)

	# Unicorn memory usage for an hour-long extended dataset
	extended_data = import_float_data("../data/perf_mem_extended_unicorn/perf-extended-mem-s-2000-h-3-w-5500-i-6000.txt")
	data_array = [extended_data]
	plot_scatters(data_array, 150, 45, ['#1f77b4'], ['.'], ['Extended Data'], 'lower right', 'Time (seconds)', 'Memory Usage (MB)', "../plot/perf-mem-camflow-extended.pdf", True)

	# Unicorn CPU usage for each vCPU and on average (for a single parameter setting as shown below)
	average_data = import_float_data("../data/perf_per_cpu/perf-wget-cpu-s-2000-h-3-w-3000-i-6000.txt")
	cpu0_data = import_float_data("../data/perf_per_cpu/cpu-0.txt")
	cpu1_data = import_float_data("../data/perf_per_cpu/cpu-1.txt")
	cpu2_data = import_float_data("../data/perf_per_cpu/cpu-2.txt")
	cpu3_data = import_float_data("../data/perf_per_cpu/cpu-3.txt")
	cpu4_data = import_float_data("../data/perf_per_cpu/cpu-4.txt")
	cpu5_data = import_float_data("../data/perf_per_cpu/cpu-5.txt")
	cpu6_data = import_float_data("../data/perf_per_cpu/cpu-6.txt")
	cpu7_data = import_float_data("../data/perf_per_cpu/cpu-7.txt")
	data_arrays = [average_data, cpu0_data, cpu1_data, cpu2_data, cpu3_data, cpu4_data, cpu5_data, cpu6_data, cpu7_data]
	plot_scatters_legend_out(data_arrays, 25, 45, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#cb416b', '#380282', '#01153e'], ['.', '|', 'x', '*', '8', 's', 'p', 'P', '1'], ['Average CPU', 'vCPU 0', 'vCPU 1', 'vCPU 2', 'vCPU 3', 'vCPU 4', 'vCPU 5', 'vCPU 6', 'vCPU 7'], 9, 'Time (seconds)', '% CPU Usage', "../plot/perf_per_cpu.pdf", True, True)

	# Unicorn detection performance for various sketch sizes
	x_data = ['500', '1,000', '2,000', '3,000', '10,000']
	accuracy_data = import_float_data("../data/param_sketch_camflow_subset/param_sketch_accuracy.txt")
	precision_data = import_float_data("../data/param_sketch_camflow_subset/param_sketch_precision.txt")
	recall_data = import_float_data("../data/param_sketch_camflow_subset/param_sketch_recall.txt")
	f_score_data = import_float_data("../data/param_sketch_camflow_subset/param_sketch_f_score.txt")
	y_arrays = [accuracy_data, precision_data, recall_data, f_score_data]
	plot_hist(y_arrays, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['Accuracy', 'Precision', 'Recall', 'F-Score'], x_data, 'Sketch Size', 'Rate', "../plot/param-camflow-subset-sketch.pdf", True)

	# Unicorn detection performance for various hops
	x_data = ['1', '2', '3', '4', '5']
	accuracy_data = import_float_data("../data/param_hop_camflow_subset/param_hop_accuracy.txt")
	precision_data = import_float_data("../data/param_hop_camflow_subset/param_hop_precision.txt")
	recall_data = import_float_data("../data/param_hop_camflow_subset/param_hop_recall.txt")
	f_score_data = import_float_data("../data/param_hop_camflow_subset/param_hop_f_score.txt")
	y_arrays = [accuracy_data, precision_data, recall_data, f_score_data]
	plot_hist(y_arrays, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['Accuracy', 'Precision', 'Recall', 'F-Score'], x_data, 'Hop', 'Rate', "../plot/param-camflow-subset-hop.pdf", True)

	# Unicorn detection performance for various hops
	x_data = ['500', '1,000', '3,000', '5,000']
	accuracy_data = import_float_data("../data/param_window_camflow_subset/param_window_accuracy.txt")
	precision_data = import_float_data("../data/param_window_camflow_subset/param_window_precision.txt")
	recall_data = import_float_data("../data/param_window_camflow_subset/param_window_recall.txt")
	f_score_data = import_float_data("../data/param_window_camflow_subset/param_window_f_score.txt")
	y_arrays = [accuracy_data, precision_data, recall_data, f_score_data]
	plot_hist(y_arrays, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ['Accuracy', 'Precision', 'Recall', 'F-Score'], x_data, 'Window Size', 'Rate', "../plot/param-camflow-subset-window.pdf", True)

