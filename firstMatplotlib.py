
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
