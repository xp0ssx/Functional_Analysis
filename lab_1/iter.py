import numpy as np

def num_of_iterations(eps: float, L: float, x0: np.ndarray, x1: np.ndarray) -> int:

    initial_error = np.max(np.abs(x1 - x0))
    
    if initial_error == 0:
        return 0
    
    n = np.ceil(np.log((eps * (1 - L)) / initial_error) / np.log(L))
    return int(n)


t = np.arange(0, 1.01, 0.01)  
x0 = np.zeros_like(t)          


x1 = np.zeros_like(t)
for n in range(len(t)):
    tn = t[n]
    if 0 <= tn <= 1/3:
        x1[n] = (1/13) * x0[int(3 * tn * (len(t) - 1))] - 5
    elif 1/3 < tn <= 4/9:
        a = (1/13) * x0[-1] - 5
        x1[n] = 9 * tn - 3 + (4 - 9 * tn) * a
    elif 4/9 < tn <= 5/9:
        x1[n] = 9 * (1 - 2 * tn)
    elif 5/9 < tn < 2/3:
        b = (1/13) * x0[0] + 5
        x1[n] = 9 * tn - 6 + (9 * tn - 5) * b
    elif 2/3 <= tn <= 1:
        x1[n] = (1/13) * x0[int((3 * tn - 2) * (len(t) - 1))] + 5


L = 1 / 13  


n_iter = num_of_iterations(1e-1, L, x0, x1)
print(f"Количество итераций для точности {1e-1}: {n_iter}")

n_iter = num_of_iterations(1e-2, L, x0, x1)
print(f"Количество итераций для точности {1e-2}: {n_iter}")

n_iter = num_of_iterations(1e-3, L, x0, x1)
print(f"Количество итераций для точности {1e-3}: {n_iter}")

n_iter = num_of_iterations(1e-4, L, x0, x1)
print(f"Количество итераций для точности {1e-4}: {n_iter}")
