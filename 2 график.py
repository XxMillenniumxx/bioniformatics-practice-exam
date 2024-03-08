import matplotlib.pyplot as plt
import numpy as np

for x in range(1,8):
    x = np.linspace(0, 100, 50)
    y = np.random.normal(x, 15)
    #y = np.clip(0.05*(x-50)**2 + y, 0, 100)
    #sizes = np.concatenate((np.linspace(400, 600, 6),np.linspace(0, 300, 44)))
    sizes = np.abs(-1/25 * x ** 2 + 2 * x + 200)
    sizes = np.clip(sizes, 50, 800)
    #sizes = np.clip(800 - np.abs(x - 50) * 10, 100, 800)
    print(sizes)
    plt.scatter(x, y, s=sizes, alpha=0.3, marker='o')


x_plot_l = np.linspace(0, 100, 2)
plt.plot(x_plot_l, x_plot_l, linestyle='--', color='black')
# Легенда
plt.legend(['Wholesale', 'Retail', 'Finance', 'Manufacturing', 'Health care', 'IT', 'Other'], loc='upper left')

plt.xlabel('1997')
plt.ylabel('Latest')
plt.title('A widespread effect')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()