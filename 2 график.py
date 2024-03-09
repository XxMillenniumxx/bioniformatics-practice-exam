import numpy as np
import matplotlib.pyplot as plt


def  normal_distributions_with_linear_dependency(began, end_range ,end, n_points):
    def split_integer(n, ratio):
        # Проверка, что длина списка долей равна 3
        if len(ratio) != 3:
            raise ValueError("Список долей должен содержать три элемента")
        
        # Расчет суммы всех долей
        total_ratio = sum(ratio)
        
        # Расчет значений для каждой переменной
        var1 = n * ratio[0] // total_ratio
        var2 = n * ratio[1] // total_ratio
        var3 = n * ratio[2] // total_ratio
        
        # Расчет остатка, если необходимо
        remainder = n - (var1 + var2 + var3)
        
        # Добавление остатка к первой переменной, чтобы сумма была равна исходному числу n
        var1 += remainder
        
        return var1, var2, var3

    ratio = [1, 40, 30]  # Процентное соотношение для каждой переменной
    var1, var2, var3 = split_integer(n_points, ratio)


    x = []
    y = []
    sizes = []
    belonging = []
    for i in range(began,end_range,5):
        x.extend(np.linspace(0 + i, 5 + i, n_points))
        y.extend(np.linspace(0 + i, 5 + i, n_points) + np.random.normal(0, 3 + (i/5), n_points)) # в итоге 1 + end_range/5

        sizes.extend(list(np.random.randint(500,800,var1)))
        sizes.extend(list(np.random.randint(50,70,var2)))
        sizes.extend(list(np.random.randint(0,10,var3)))
        belonging.extend(list(np.random.randint(0,7,n_points)))
    for i in range(end_range,end,5):
        x.extend(np.linspace(0 + i, 5 + i, n_points))
        y.extend(np.linspace(0 + i, 5 + i, n_points) + np.random.normal(0,3 + end_range/5 - (i-end_range)/5, n_points))
        sizes.extend(list(np.random.randint(30,500,var1)))
        sizes.extend(list(np.random.randint(0,15,var2)))
        sizes.extend(list(np.random.randint(0,10,var3)))
        belonging.extend(list(np.random.randint(0,7,n_points)))
    #print("Это x -",x)
    #print("Это y -",y)
    return x,y,sizes,belonging
    
    
x,y,sizes,belonging = normal_distributions_with_linear_dependency(0, 50, 100 , 50)

# Нужно разделить рандомно x,y,sizes на 7 участков
for i in range(7):
    # Фильтрация точек по принадлежности
    x_subset = [x[j] for j in range(len(x)) if belonging[j] == i]
    y_subset = [y[j] for j in range(len(y)) if belonging[j] == i]
    sizes_subset = [sizes[j] for j in range(len(sizes)) if belonging[j] == i]
    
    # Визуализация данных
    plt.scatter(x_subset, y_subset, s=sizes_subset, alpha=0.2, edgecolor='black', label=f'Belonging {i}')
    

#plt.scatter(x, y, s=sizes, alpha=0.2,edgecolor='black')


plt.gca().set_facecolor('lightblue')
plt.gca().patch.set_alpha(0.1)
plt.grid(axis='y')

x_plot_l = np.linspace(0, 100, 2)
plt.plot(x_plot_l, x_plot_l, linestyle='--', color='black', alpha=0.3)
# Легенда
plt.legend(['Wholesale', 'Retail', 'Finance', 'Manufacturing', 'Health care', 'IT', 'Other'], loc='upper left')

plt.xlabel('1997')
plt.ylabel('Latest')
plt.title('A widespread effect')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()
