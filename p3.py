import random
import time
import multiprocessing
NUM_RANDOMS = 100000000
proc = []
def myfunc(TASK,count,lock) :
	for x in range(TASK):
		rnd = random.random()
		if rnd < 0.5:
			with lock:
				count.value += 1
if __name__ == '__main__':
	NUM_CPU = int(input("Enter number of CPU: "))
	TASK = int(NUM_RANDOMS/NUM_CPU)
	count = multiprocessing.Value('i',0)
	lock = multiprocessing.Lock()
	st = time.time()
	for i in range (NUM_CPU):
		p = multiprocessing.Process(target = myfunc, args = (TASK,count,lock))
		proc.append(p)
	for p in proc:
		p.start()
	for p in proc:
		p.join()
	et = time.time()
	print(f"Percentage = {count.value/NUM_RANDOMS}")
	print(f"Execution time: {((et-st)*1000)} ms.")