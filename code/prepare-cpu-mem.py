import os, sys

def decompose(input_file, mem_filepath, cpu_filepath):
	mem = open(mem_filepath, "a+")
	cpu = open(cpu_filepath, "a+")

	with open(input_file, 'r') as f:
		cpu_val = 0.0
		for line in f:
			data = line.strip().split()
			if data[0] == '%CPU':
				next_is_mem = True
				next_is_cpu = False
				cpu.write(str(float(cpu_val) / 4) + '\n')
				cpu_val = 0.0
				continue
			if next_is_mem:
				mem.write(str(float(data[1]) * 4096 * 0.01) + '\n')
				next_is_mem = False
				continue
			if data[0] == 'PSR':
				next_is_cpu = True
				continue
			if next_is_cpu:
				if data[0] == '0':
					cpu_val += float(data[1])
				elif data[0] == '1':
					cpu_val += float(data[1])
				elif data[0] == '2':
					cpu_val += float(data[1])
				elif data[0] == '3':
					cpu_val += float(data[1])

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

