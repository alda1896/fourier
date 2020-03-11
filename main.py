from DFT import DFT
from numpy import loadtxt
from pylab import plot, show

data = loadtxt('co2_mm_mlo.txt',float)

mydft=DFT()

a=mydft.dft(data[:,3])
b=list(map(abs,a))

plot(b)
show()
