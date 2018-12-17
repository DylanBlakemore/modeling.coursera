

import numpy as np
import math
import ipdb

class Integrator:
	def __init__(self, xMin, xMax, N):
		self.dx = float(xMax - xMin)/float(N - 1)
		self.N = N
		self.S = 0.0
		self.xMin = float(xMin)

	def f(self, x):
		return x**2 * math.exp(-1*x) * math.sin(x)

	def integrate(self):       
		for i in range(self.N-1):
			xi = self.xMin + float(i)*self.dx
			self.S = self.S + self.f(xi)*self.dx
 
	def show(self):
		print(self.S)

   

examp = Integrator(1,3,200)
examp.integrate()
examp.show()