import random
import time
import multiprocessing
import numpy
arrsize = 1000
NUM_CPU = 4
chunksize = int(arrsize/NUM_CPU)
lock = multiprocessing.Lock()
def generate():
    arr = []
    for i in range(arrsize):
        arr.append(random.randint(0,9))
    return arr
def generateC():
	manager = multiprocessing.Manager()
	arr = manager.list()
	for i in range(arrsize):
	    arr.append(0)
	return arr
def add(start,stop,A,B,C):
    for i in range (start,stop):
        c = A[i] + B[i]
        with lock:
        	C[i] = c
if __name__ == '__main__':
    ptr = 0
    A = generate()
    B = generate()
    C = generateC()
    proc = []
    st = time.time()
    for i in range (NUM_CPU):
        p = multiprocessing.Process(target = add, args = (ptr,ptr+chunksize,A,B,C))
        proc.append(p)
        ptr = ptr+chunksize
    for p in proc:
        p.start()
    for p in proc:
        p.join()
    et = time.time()
    out = numpy.reshape(C,(50,20))
    a = numpy.reshape(A,(50,20))
    b = numpy.reshape(B,(50,20))
    print(f"Matrix A :\n{a}")
    print(f"Matrix B :\n{b}")
    print(f"Matrix C :\n{out}")
    print(f"\nExecution time: {((et-st)*1000)} ms.")