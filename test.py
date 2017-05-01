import support
import numpy as np

a = support.SupportSim()

def diagonalsplit(size):
	supportpoints = np.zeros((size[0], 2))
	a.addnode(5,0)
	for i in range(len(supportpoints)):
		supportpoints[i] = [i,size[1]]
		a.addnode(i, size[1])
	print("nodelist")
	print(a.nodes)


	print("supportpoints ")
	print(supportpoints)
	for n in range(len(a.nodes)):
		a.addbeam(n, 0)
	#a.addnode(1,3)
	#a.addnode(10,8)
	#a.addbeam(0,1)

diagonalsplit((10,10))
print(a.beamlength())
a.drawstructure()
