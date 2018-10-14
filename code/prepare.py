import csv
import sys

def best_results(filepath):
	data = open(filepath, 'r')
	reader = csv.reader(data)

	best_f_measure = None
	best_precision = None
	best_recall = None
	best_accuracy = None
	final_metric = None
	final_std = None
	for row in reader:
		metric = row[0]
		std = row[1]
		precision = row[6]
		recall = row[7]
		accuracy = row[8]
		f_measure = row[9]
		if f_measure == 'None' or precision == 'None' or recall == 'None' or accuracy == 'None':
			continue
		else:
			precision = float(row[6])
			recall = float(row[7])
			accuracy = float(row[8])
			f_measure = float(row[9])
		if best_f_measure == None or float(f_measure) > best_f_measure:
			best_f_measure = f_measure
			best_precision = precision
			best_recall = recall
			best_accuracy = accuracy
			final_metric = metric
			final_std = std
		elif f_measure == best_f_measure:
			if accuracy > best_accuracy:
				best_f_measure = f_measure
				best_precision = precision
				best_recall = recall
				best_accuracy = accuracy
				final_metric = metric
				final_std = std
			elif accuracy == best_accuracy:
				if precision > best_precision:
					best_f_measure = f_measure
					best_precision = precision
					best_recall = recall
					best_accuracy = accuracy
					final_metric = metric
					final_std = std
				elif precision == best_precision:
					if recall > best_recall:
						best_f_measure = f_measure
						best_precision = precision
						best_recall = recall
						best_accuracy = accuracy
						final_metric = metric
						final_std = std
					elif recall == best_recall:
						if metric == 'mean' and final_metric == 'max':
							best_f_measure = f_measure
							best_precision = precision
							best_recall = recall
							best_accuracy = accuracy
							final_metric = metric
							final_std = std
						elif metric == final_metric == 'mean':
							if std > final_std:
								best_f_measure = f_measure
								best_precision = precision
								best_recall = recall
								best_accuracy = accuracy
								final_metric = metric
								final_std = std
	return best_f_measure, best_precision, best_recall, best_accuracy, final_metric, final_std

if __name__ == "__main__":
	if (len(sys.argv) < 1):
		print("""
			Usage: python prepare.py
		"""
		)
		sys.exit(1)
	sketch_f_measure_perf = open("../data/sketch-f-measure-perf.txt", "a+")
	sketch_precision_perf = open("../data/sketch-precision-perf.txt", "a+")
	sketch_recall_perf = open("../data/sketch-recall-perf.txt", "a+")
	sketch_accuracy_perf = open("../data/sketch-accuracy-perf.txt", "a+")

	best_f_measure_500, best_precision_500, best_recall_500, best_accuracy_500, _, _ = best_results("../data/stats-s-500-h-3-w-450-i-10000.csv")
	best_f_measure_1000, best_precision_1000, best_recall_1000, best_accuracy_1000, _, _ = best_results("../data/stats-s-1000-h-3-w-450-i-10000.csv")
	best_f_measure_1500, best_precision_1500, best_recall_1500, best_accuracy_1500, _, _ = best_results("../data/stats-s-1500-h-3-w-450-i-10000.csv")
	best_f_measure_2000, best_precision_2000, best_recall_2000, best_accuracy_2000, _, _ = best_results("../data/stats-s-2000-h-3-w-450-i-10000.csv")
	best_f_measure_3000, best_precision_3000, best_recall_3000, best_accuracy_3000, _, _ = best_results("../data/stats-s-3000-h-3-w-450-i-10000.csv")

	sketch_f_measure_perf.write(str(best_f_measure_500) + '\n')
	sketch_f_measure_perf.write(str(best_f_measure_1000) + '\n')
	sketch_f_measure_perf.write(str(best_f_measure_1500) + '\n')
	sketch_f_measure_perf.write(str(best_f_measure_2000) + '\n')
	sketch_f_measure_perf.write(str(best_f_measure_3000) + '\n')

	sketch_precision_perf.write(str(best_precision_500) + '\n')
	sketch_precision_perf.write(str(best_precision_1000) + '\n')
	sketch_precision_perf.write(str(best_precision_1500) + '\n')
	sketch_precision_perf.write(str(best_precision_2000) + '\n')
	sketch_precision_perf.write(str(best_precision_3000) + '\n')

	sketch_recall_perf.write(str(best_recall_500) + '\n')
	sketch_recall_perf.write(str(best_recall_1000) + '\n')
	sketch_recall_perf.write(str(best_recall_1500) + '\n')
	sketch_recall_perf.write(str(best_recall_2000) + '\n')
	sketch_recall_perf.write(str(best_recall_3000) + '\n')

	sketch_accuracy_perf.write(str(best_accuracy_500) + '\n')
	sketch_accuracy_perf.write(str(best_accuracy_1000) + '\n')
	sketch_accuracy_perf.write(str(best_accuracy_1500) + '\n')
	sketch_accuracy_perf.write(str(best_accuracy_2000) + '\n')
	sketch_accuracy_perf.write(str(best_accuracy_3000) + '\n')

	sketch_f_measure_perf.close()
	sketch_precision_perf.close()
	sketch_recall_perf.close()
	sketch_accuracy_perf.close()

	window_f_measure_perf = open("../data/window-f-measure-perf.txt", "a+")
	window_precision_perf = open("../data/window-precision-perf.txt", "a+")
	window_recall_perf = open("../data/window-recall-perf.txt", "a+")
	window_accuracy_perf = open("../data/window-accuracy-perf.txt", "a+")

	best_f_measure_200, best_precision_200, best_recall_200, best_accuracy_200, _, _ = best_results("../data/stats-s-2000-h-3-w-200-i-10000.csv")
	best_f_measure_450, best_precision_450, best_recall_450, best_accuracy_450, _, _ = best_results("../data/stats-s-2000-h-3-w-450-i-10000.csv")
	best_f_measure_1500, best_precision_500, best_recall_500, best_accuracy_500, _, _ = best_results("../data/stats-s-2000-h-3-w-500-i-10000.csv")
	best_f_measure_1000, best_precision_1000, best_recall_1000, best_accuracy_1000, _, _ = best_results("../data/stats-s-2000-h-3-w-1000-i-10000.csv")
	best_f_measure_2000, best_precision_2000, best_recall_2000, best_accuracy_2000, _, _ = best_results("../data/stats-s-2000-h-3-w-2000-i-10000.csv")

	window_f_measure_perf.write(str(best_f_measure_200) + '\n')
	window_f_measure_perf.write(str(best_f_measure_450) + '\n')
	window_f_measure_perf.write(str(best_f_measure_500) + '\n')
	window_f_measure_perf.write(str(best_f_measure_1000) + '\n')
	window_f_measure_perf.write(str(best_f_measure_2000) + '\n')

	window_precision_perf.write(str(best_precision_200) + '\n')
	window_precision_perf.write(str(best_precision_450) + '\n')
	window_precision_perf.write(str(best_precision_500) + '\n')
	window_precision_perf.write(str(best_precision_1000) + '\n')
	window_precision_perf.write(str(best_precision_2000) + '\n')

	window_recall_perf.write(str(best_recall_200) + '\n')
	window_recall_perf.write(str(best_recall_450) + '\n')
	window_recall_perf.write(str(best_recall_500) + '\n')
	window_recall_perf.write(str(best_recall_1000) + '\n')
	window_recall_perf.write(str(best_recall_2000) + '\n')

	window_accuracy_perf.write(str(best_accuracy_200) + '\n')
	window_accuracy_perf.write(str(best_accuracy_450) + '\n')
	window_accuracy_perf.write(str(best_accuracy_500) + '\n')
	window_accuracy_perf.write(str(best_accuracy_1000) + '\n')
	window_accuracy_perf.write(str(best_accuracy_2000) + '\n')

	window_f_measure_perf.close()
	window_precision_perf.close()
	window_recall_perf.close()
	window_accuracy_perf.close()

	hop_f_measure_perf = open("../data/hop-f-measure-perf.txt", "a+")
	hop_precision_perf = open("../data/hop-precision-perf.txt", "a+")
	hop_recall_perf = open("../data/hop-recall-perf.txt", "a+")
	hop_accuracy_perf = open("../data/hop-accuracy-perf.txt", "a+")

	best_f_measure_1, best_precision_1, best_recall_1, best_accuracy_1, _, _ = best_results("../data/stats-s-2000-h-1-w-450-i-10000.csv")
	best_f_measure_2, best_precision_2, best_recall_2, best_accuracy_2, _, _ = best_results("../data/stats-s-2000-h-2-w-450-i-10000.csv")
	best_f_measure_3, best_precision_3, best_recall_3, best_accuracy_3, _, _ = best_results("../data/stats-s-2000-h-3-w-450-i-10000.csv")
	best_f_measure_4, best_precision_4, best_recall_4, best_accuracy_4, _, _ = best_results("../data/stats-s-2000-h-4-w-450-i-10000.csv")
	best_f_measure_5, best_precision_5, best_recall_5, best_accuracy_5, _, _ = best_results("../data/stats-s-2000-h-5-w-450-i-10000.csv")

	hop_f_measure_perf.write(str(best_f_measure_1) + '\n')
	hop_f_measure_perf.write(str(best_f_measure_2) + '\n')
	hop_f_measure_perf.write(str(best_f_measure_3) + '\n')
	hop_f_measure_perf.write(str(best_f_measure_4) + '\n')
	hop_f_measure_perf.write(str(best_f_measure_5) + '\n')

	hop_precision_perf.write(str(best_precision_1) + '\n')
	hop_precision_perf.write(str(best_precision_2) + '\n')
	hop_precision_perf.write(str(best_precision_3) + '\n')
	hop_precision_perf.write(str(best_precision_4) + '\n')
	hop_precision_perf.write(str(best_precision_5) + '\n')

	hop_recall_perf.write(str(best_recall_1) + '\n')
	hop_recall_perf.write(str(best_recall_2) + '\n')
	hop_recall_perf.write(str(best_recall_3) + '\n')
	hop_recall_perf.write(str(best_recall_4) + '\n')
	hop_recall_perf.write(str(best_recall_5) + '\n')

	hop_accuracy_perf.write(str(best_accuracy_1) + '\n')
	hop_accuracy_perf.write(str(best_accuracy_2) + '\n')
	hop_accuracy_perf.write(str(best_accuracy_3) + '\n')
	hop_accuracy_perf.write(str(best_accuracy_4) + '\n')
	hop_accuracy_perf.write(str(best_accuracy_5) + '\n')

	hop_f_measure_perf.close()
	hop_precision_perf.close()
	hop_recall_perf.close()
	hop_accuracy_perf.close()	







