# importing the multiprocessing module
import multiprocessing
from time import sleep

def print2():
	for i in range(30,1000):
		print(i)
		sleep(1)
	

def print1():
	for i in range(5000,10000):
		print(i)
		sleep(0.5)

if __name__ == "__main__":
	# creating processes
	p1 = multiprocessing.Process(target=print1)
	p2 = multiprocessing.Process(target=print2)

	# starting process 1
	p1.start()
	# starting process 2
	p2.start()

	# wait until process 1 is finished
	p1.join()
	# wait until process 2 is finished
	p2.join()

	# both processes finished
	print("Done!")
