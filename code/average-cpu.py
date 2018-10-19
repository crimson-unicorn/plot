import os, sys

def average(input_file):
	with open(input_file, 'r') as f:
		cpu_val = 0.0
		for total,line in enumerate(f):
			cpu_val += float(line.strip())
	cpu_val = cpu_val/total
	f.close()
	print str(cpu_val)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("""
			Usage: python prepare-cpu-mem.py <input_file> 
		"""
		)
		sys.exit(1)
	average(sys.argv[1])

