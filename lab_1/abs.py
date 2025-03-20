import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

t = np.arange(0, 1.01, 0.01)
n_points = len(t)

x = np.zeros_like(t)

absolute_differences = []

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

    ab = np.abs(x - y)
    absolute_differences.append(ab)  

    plt.figure(iteration * 2 - 1)
    plt.plot(t, x, label='x')
    plt.plot(t, y, label='y')
    plt.grid(True)
    plt.legend()
    plt.title(f'Итерация {iteration}: x и y')

    plt.figure(iteration * 2)
    plt.plot(t, ab, label='|x - y|')
    plt.grid(True)
    plt.legend()
    plt.title(f'Итерация {iteration}: Абсолютная разность')

    x = y.copy()


plt.figure(figsize=(10, 6))
for i, ab in enumerate(absolute_differences):
    plt.plot(t, ab, label=f'Итерация {i+1}')
plt.grid(True)
plt.legend()
plt.title('Абсолютная разность на всех итерациях')
plt.xlabel('t')
plt.ylabel('|x - y|')

# plt.show()
plt.savefig('abs.png')