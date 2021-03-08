import matplotlib.pyplot as plt #imports the graphing function library
plt.plot([0,1,2,3,4], [0,1,4,9,16]) #picks points on the graph using x and y coordinates with two arrays
plt.ylabel('y') #label for the Y-axis of the graph
plt.xlabel('x') #label for the X-axis of the graph
plt.axis([0, 4, 0, 16]) #sets the scale for each axis (0-4 and 0-16)
plt.show() #displays the graph