import numpy as np
from matplotlib import pyplot as plt

x = np.array([56, 72, 69, 88, 102, 86, 76, 79, 94, 74])
y = np.array([92, 102, 86, 110, 130, 99, 96, 102, 105, 92])

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')

def square_loss(x: np.ndarray, y: np.ndarray, a: float, b: float) -> float:
    loss = sum(np.square(y - (a * x + b)))
    return loss

def least_squares_algebraic(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    a = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
    b = np.mean(y) - a * np.mean(x)
    return a, b

a, b = least_squares_algebraic(x, y)
square_loss(x, y, a, b)

x_temp = np.linspace(50, 120, 100)
plt.scatter(x, y)
plt.plot(x_temp, a * x_temp + b, color='red')

plt.show()