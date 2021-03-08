import numpy as np #import the numpy library for math operations
import matplotlib.pyplot as plt #imports the graphing function library
def math_fun(t): #creates function for receving math result
 return np.exp(-t) * np.cos(2*np.pi*t) #math operations on t
t1 = np.arange(0.0, 5.0, 0.1) #scale for first graph
t2 = np.arange(0.0, 5.0, 0.02) #scale fore second graph
plt.figure(1) #plot everything within fig1
plt.subplot(211) #placement for first graph
plt.plot(t1, math_fun(t1), 'r+', t2, math_fun(t2), 'k') #places points on the graph according to math fucntion's manipulation of t1 and t2 
plt.grid() #dsiplay gridlines on the chart

plt.subplot(212) #placement of second graph
plt.plot(t2, np.cos(2*np.pi*t2), 'b--') #plots a wave for second graph
plt.grid() #dsiplay gridlines on the chart
plt.show() #displays the graphs