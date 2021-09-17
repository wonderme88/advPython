
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


# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# Create four polar axes and access them through the returned array
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)

# Create figure number 10 with a single subplot
# and clears it if it already exists.
fig, ax = plt.subplots(num=10, clear=True)
