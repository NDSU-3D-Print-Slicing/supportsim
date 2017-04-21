import support
import numpy as np

a = support.SupportSim()

def diagonalsplit(size):
	supportpoints = np.zeros((size[0], 2))
	for i in range(len(supportpoints)):
		supportpoints[i] = [i,size[1]]
		a.addnode(i, size[1])
	print("nodelist")
	print(a.nodes)


	print("supportpoints ")
	print(supportpoints)
	for n in range(len(a.nodes)):
		a.addbeam(n, 0)

diagonalsplit((10,10))
a.drawlines()
