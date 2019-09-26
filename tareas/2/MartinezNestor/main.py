from foundations import * 
from rr1 import *
from rr4 import *
from fcfs import *

#Main method
f = Foundation()

def main():
	procs = generateTest()
	#Round Robin with quantum = 1
	rr1(procs)
	#Round Robin with quantum = 4
	rr4(procs,4)


#generateTest() generates a hard coded data set of processes
def generateTest():
	a = Process("A",0,3)
	b = Process("B",1,5)
	c = Process("C",3,2)
	d = Process("D",9,5)
	e = Process("E",12,5)
	return [a,b,c,d,e]



#---------------------------
if __name__ == '__main__':
	main()
#---------------------------