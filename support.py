#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

class SupportSim():

	def __init__(self):
		print("construct")
		self.pointx = np.array([]).reshape(0,2)
		self.pointy = np.array([]).reshape(0,2)
		self.nodes =  np.array([]).reshape(0,2)
		self.beams= []


	def drawlines(self):
		for n1,n2 in self.beams:
			plt.plot(self.nodes[n1], self.nodes[n2])
			print("plotting ", self.nodes[n1],";", self.nodes[n2])

		plt.show()

	def addnode(self, x, y):
		self.nodes = np.append(self.nodes, [[x, y]], axis=0)
	
	def addbeam(self, n1, n2):
		self.beams.append([n1,n2])

