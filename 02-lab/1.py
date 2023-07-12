import matplotlib.pyplot as plt
import numpy as np
import math as m

count = 100
xs = np.linspace(0.1, 4, count)
ys_const = [1 for x in xs]
ys_log = [m.log(x) for x in xs]
ys_linear = [x for x in xs]
ys_linearithmic = [x*m.log(x) for x in xs]
ys_quadratic = [x**2 for x in xs]
ys_exponential = [2**x for x in xs]

plt.plot(xs, ys_const, 'c')
plt.plot(xs, ys_log, 'r')
plt.plot(xs, ys_linear, 'b')
plt.plot(xs, ys_linearithmic, 'g')
plt.plot(xs, ys_quadratic, 'y')
plt.plot(xs, ys_exponential, 'm')
plt.show()