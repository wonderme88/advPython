
import matplotlib.pyplot as plt
import numpy as np

#https://matplotlib.org/stable/contents.html
# jupyter notebook -- run jupyter

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

plt.show()


students = ['A', 'B', 'C', 'D']
marks = [50,60,80,90]
plt.bar(students,marks,label = 'CS')
plt.title('Result')
plt.xlabel('Students')
plt.ylabel('Marks Obtained')
plt.legend()
plt.show()


students = ['A', 'B', 'C', 'D']
marks = [50,60,80,90]
plt.barh(students,marks,label = 'CS')
plt.title('Result')
plt.xlabel('Students')
plt.ylabel('Marks Obtained')
plt.legend()
plt.show()


csStud = ['A', 'B', 'C', 'D']
mechStud = ['E','F','G','H']
csmarks = [50,60,80,90]
mechmarks= [40,50,92,85]

plt.bar(csStud,csmarks,label = 'CS')
plt.bar(mechStud,mechmarks,label = 'MECH')
plt.title('Result')
plt.xlabel('Students')
plt.ylabel('Marks Obtained')
plt.legend()
plt.show()

#####

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

