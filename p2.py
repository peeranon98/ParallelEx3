import multiprocessing

def calculate():
    x = 1.0
    while True:
        x = x + 1.0
 
if __name__ == '__main__':  
	for i in range(multiprocessing.cpu_count()):
	    p = multiprocessing.Process(target=calculate)
	    p.start()
