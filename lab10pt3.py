import numpy as np #import the numpy library for math operations
import matplotlib.pyplot as plt #imports the graphing function library
fig = plt.figure() #plots figure in fig1 window 
ax = plt.axes(projection="3d") #allows for 3d dataset figure
z_line = np.linspace(0, 15, 1000) #setups parameters for z axis
x_line = np.exp(-0.1*z_line) * np.cos(z_line) #setups parameters for x axis
y_line = np.exp(-0.1*z_line) * np.sin(z_line) #setups parameters for y axis
ax.plot3D(x_line, y_line, z_line, 'red') #combines axis data to create a figure and sets it to display in red 
ax.set_xlabel("x") #label for x axis
ax.set_ylabel("y") #label for y axis
ax.set_zlabel("z") #label for z axis
plt.show() #display figure 