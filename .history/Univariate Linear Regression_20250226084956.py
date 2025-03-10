import numpy as np
from matplotlib import pyplot as plt

x = np.array([56, 72, 69, 88, 102, 86, 76, 79, 94, 74])
y = np.array([92, 102, 86, 110, 130, 99, 96, 102, 105, 92])

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()