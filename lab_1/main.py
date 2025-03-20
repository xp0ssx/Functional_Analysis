import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

t = np.arange(0, 1.01, 0.01)
n_points = len(t)

x = np.zeros_like(t)

y_iterations = []

for iteration in range(1, 10):

    a = (1/13) * x[-1] - 5  
    b = (1/13) * x[0] + 5  

    y = np.zeros_like(t)
    for n in range(n_points):
        tn = t[n]
        if 0 <= tn <= 1/3:
            idx = int(3 * tn * (n_points - 1))
            y[n] = (1/13) * x[idx] - 5
        elif 1/3 < tn <= 4/9:
            y[n] = 9 * tn - 3 + (4 - 9 * tn) * a
        elif 4/9 < tn <= 5/9:
            y[n] = 9 * (1 - 2 * tn)
        elif 5/9 < tn < 2/3:
            y[n] = 9 * tn - 6 + (9 * tn - 5) * b
        elif 2/3 <= tn <= 1:
            scaled_t = 3 * tn - 2
            idx = int(scaled_t * (n_points - 1))
            y[n] = (1/13) * x[idx] + 5

    y_iterations.append(y)

    x = y.copy()

plt.figure(figsize=(10, 6))
for i, y in enumerate(y_iterations):
    plt.plot(t, y, label=f'Итерация {i+1}')
plt.grid(True)
plt.legend()
plt.title('Неподвижная точка на всех итерациях')
plt.xlabel('t')
plt.ylabel('y(t)')

# plt.show()
plt.savefig('dot.png')