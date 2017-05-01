#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class SupportSim():

	def __init__(self):
		#print("construct")
		self.pointx = np.array([]).reshape(0,2)
		self.pointy = np.array([]).reshape(0,2)
		self.nodes =  np.array([]).reshape(0,2)
		self.beams= []


	def drawstructure(self):
		for n1,n2 in self.beams:
			p = np.array([self.nodes[n1], self.nodes[n2]]).T
			plt.plot(p[0], p[1])
			print("plotting ", self.nodes[n1],";", self.nodes[n2])

		plt.show()
	
	def beamlength(self):
		length = 0
		for n1,n2 in self.beams:
			#length = sqrt(self.nodes[n1])
			print(self.nodes[n1], self.nodes[n2])
			length += np.linalg.norm(self.nodes[n1]- self.nodes[n2])
		return length

	def addnode(self, x, y):
		self.nodes = np.append(self.nodes, [[x, y]], axis=0)
	
	def addbeam(self, n1, n2):
		self.beams.append([n1,n2])

