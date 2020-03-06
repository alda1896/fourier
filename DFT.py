import math as mt
from cmath import exp, pi
class DFT:
	def __init__(self):
		self.c=[]
	def dft (self,datos):
		N=len(datos)		
		for k in range (N//2):
			ck=0.+0j
			for n in range (N):
				ck += datos[n]*exp(-2j*pi*k*n/N)
			self.c.append(ck)
		        
		return(self.c)
