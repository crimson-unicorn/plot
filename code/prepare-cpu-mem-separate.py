import os, sys

def decompose(input_file, mem_filepath, core0_filepath, core1_filepath, core2_filepath, core3_filepath, core4_filepath, core5_filepath, core6_filepath, core7_filepath):
	mem = open(mem_filepath, "a+")
	fcore0 = open(core0_filepath, "a+")
	fcore1 = open(core1_filepath, "a+")
	fcore2 = open(core2_filepath, "a+")
	fcore3 = open(core3_filepath, "a+")
	fcore4 = open(core4_filepath, "a+")
	fcore5 = open(core5_filepath, "a+")
	fcore6 = open(core6_filepath, "a+")
	fcore7 = open(core7_filepath, "a+")

	with open(input_file, 'r') as f:
		core0 = 0.0
		core1 = 0.0
		core2 = 0.0
		core3 = 0.0
		core4 = 0.0
		core5 = 0.0
		core6 = 0.0
		core7 = 0.0
		for line in f:
			data = line.strip().split()
			if data[0] == '%CPU':
				next_is_mem = True
				next_is_cpu = False
				fcore0.write(str(core0) + '\n')
				fcore1.write(str(core1) + '\n')
				fcore2.write(str(core2) + '\n')
				fcore3.write(str(core3) + '\n')
				fcore4.write(str(core4) + '\n')
				fcore5.write(str(core5) + '\n')
				fcore6.write(str(core6) + '\n')
				fcore7.write(str(core7) + '\n')
				core0 = 0.0
				core1 = 0.0
				core2 = 0.0
				core3 = 0.0
				core4 = 0.0
				core5 = 0.0
				core6 = 0.0
				core7 = 0.0
				continue
			if next_is_mem:
				mem.write(str(float(data[1]) * 61 * 1024 * 0.01) + '\n')
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
				elif data[0] == '4':
					core4 += float(data[1])
				elif data[0] == '5':
					core5 += float(data[1])
				elif data[0] == '6':
					core6 += float(data[1])
				elif data[0] == '7':
					core7 += float(data[1])

	f.close()
	mem.close()
	fcore0.close()
	fcore1.close()
	fcore2.close()
	fcore3.close()
	fcore4.close()
	fcore5.close()
	fcore6.close()
	fcore7.close()

if __name__ == "__main__":
	if (len(sys.argv) < 7):
		print("""
			Usage: python prepare-cpu-mem.py <input_file> <mem_output> <core0_output> <core1_output> <core2_output> <core3_output> <core4_output> <core5_output> <core6_output> <core7_output>
		"""
		)
		sys.exit(1)
	decompose(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])

