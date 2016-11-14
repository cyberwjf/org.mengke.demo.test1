from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
S = np.sin(X)

plot(X, S)

show()
