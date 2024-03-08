import numpy as np
import matplotlib.pyplot as plt

# Она должна частично совпадать с логарифмической ф0ией
# x
# 15 до 500, но есть выбросы
# y
# 0.5 до 10

# Генерируем случайные данные для логарифмических графиков

NUMPER_T = 5000
NUMBER_PLOT = 9
#x = np.linspace(0, 1000, NUMPER_T)
x = np.concatenate((np.linspace(0, 200, NUMPER_T-3000), np.linspace(0, 1000, 3000)))
# Создание двух массивов точек, близких к 0 и 1000
#points_near_zero = np.linspace(0, 200, 1600)
#points_near_1000 = np.logspace(np.log10(200), np.log10(1000), 400)
#
## Соединение двух массивов
#x = np.concatenate((points_near_zero, points_near_1000))
y = []
result = []
# Создаем несколько логарифмических графиков разных цветов
for i in range(1, NUMBER_PLOT):
    new_array = [i] * NUMPER_T  # создаем новый массив из повторений числа i
    result += new_array  # добавляем его в результат
    #print(result)
    y_result = np.random.normal((3-(i/10+1))*np.log(x-i*20)+( i/100 + 1), 0.3)
    y.extend(y_result)
x = np.tile(x, NUMBER_PLOT - 1)
print(len(x))
print(len(y))
print(len(result))
#print(result)
plt.scatter(x, y, c=result,cmap="plasma", s=0.8)
#plt.scatter(x, y, c=result,cmap="plasma", s=24)
plt.colorbar(shrink=0.3,aspect=4, label = "Span of Control",location = 'right')



# Генерируем случайные данные для черных точек
black_x = np.random.uniform(10, 800, 500)
black_y = np.random.normal(1.7*np.log(black_x-100), 1.2)


# Рисуем черные точки
plt.scatter(black_x, black_y, color='black', alpha=1, s=10)

# Настройка графика
plt.xlabel('Energy use per capita (GJ)')
plt.ylabel('Managers (% of Total Employment)')
plt.title('Managers Employment vs. Energy Use')
plt.legend(bbox_to_anchor=(1, 0.8),frameon = False)


plt.grid(True)

plt.xlim(0, 1000)
plt.ylim(0, 16)
# Отображаем график
plt.show()