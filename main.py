from DFT import DFT
from numpy import loadtxt
from pylab import plot, show

rawdata = loadtxt('pitch.txt')

#print(type(rawdata))

#plot(rawdata)
#show()

mydft=DFT()

a=mydft.dft(rawdata)
b=list(map(abs,a))
plot(b)

show()
