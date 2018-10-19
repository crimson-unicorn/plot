import os, sys

def decompose(input_file, mem_filepath, core_filepath):
	mem = open(mem_filepath, "a+")
	fcore = open(core_filepath, "a+")

	with open(input_file, 'r') as f:
		core0 = 0.0
		core1 = 0.0
		core2 = 0.0
		core3 = 0.0
		for line in f:
			data = line.strip().split()
			if data[0] == '%CPU':
				next_is_mem = True
				next_is_cpu = False
				fcore.write(str(max(core0, core1, core2, core3)) + '\n')
				core0 = 0.0
				core1 = 0.0
				core2 = 0.0
				core3 = 0.0
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
					core0 += float(data[1])
				elif data[0] == '1':
					core1 += float(data[1])
				elif data[0] == '2':
					core2 += float(data[1])
				elif data[0] == '3':
					core3 += float(data[1])

	f.close()
	mem.close()
	fcore.close()

if __name__ == "__main__":
	if (len(sys.argv) < 4):
		print("""
			Usage: python prepare-cpu-mem.py <input_file> <mem_output> <core_output>
		"""
		)
		sys.exit(1)
	decompose(sys.argv[1], sys.argv[2], sys.argv[3])

