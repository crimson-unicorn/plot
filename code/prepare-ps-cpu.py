import os, sys

def decompose(input_file, mem_filepath, cpu_filepath):
	mem = open(mem_filepath, "a+")
	cpu = open(cpu_filepath, "a+")

	with open(input_file, 'r') as f:
		for line in f:
			data = line.strip().split()
			if data[0] == '%CPU':
				next_is_mem = True
				continue
			if next_is_mem:
				mem.write(str(float(data[1]) * 4096 * 0.01) + '\n')
				cpu.write(str(float(data[0])) + '\n')
				next_is_mem = False
				continue

	f.close()
	mem.close()
	cpu.close()

if __name__ == "__main__":
	if (len(sys.argv) < 4):
		print("""
			Usage: python prepare-cpu-mem.py <input_file> <mem_output> <cpu_output>
		"""
		)
		sys.exit(1)
	decompose(sys.argv[1], sys.argv[2], sys.argv[3])

