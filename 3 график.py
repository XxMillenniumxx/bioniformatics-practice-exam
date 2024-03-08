import matplotlib.pyplot as plt
import numpy as np
import joypy
import pandas as pd
from matplotlib import cm
# Создаем данные для графика

#NUMBER_PROBEL = 1000
#y = [0, NUMBER_PROBEL, NUMBER_PROBEL*2, NUMBER_PROBEL*3, NUMBER_PROBEL*4,NUMBER_PROBEL*5,NUMBER_PROBEL*6,NUMBER_PROBEL*7,NUMBER_PROBEL*8,NUMBER_PROBEL*9,NUMBER_PROBEL*10,NUMBER_PROBEL*11]



labels = ["December","November","October","September","August","July","June","May","April","March","February","January"]
import numpy as np

n_samples = 1000  # Количество случайных выборок
temperature_mean = [5, 10, 15, 20, 25, 30, 35, 30, 25, 20, 15, 10]  # Средние температуры для каждого месяца
temperature_std = [2, 2.5, 3, 3.5, 4, 4.5, 5, 4.5, 4, 3.5, 3, 2.5]  # Стандартное отклонение температуры для каждого месяца

x_DEC = {}
for i, month in enumerate(labels):
    x_DEC[month] = np.random.normal(temperature_mean[i], temperature_std[i], n_samples)

print(x_DEC)


#x_DEC = np.clip(np.random.normal(-1.7, 2, 6000), -5.3, 3.5)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#fig, axes = joypy.joyplot(x_DEC, column=labels, by="class", ylim='own', figsize=(14,10))
joypy.joyplot(x_DEC, column=labels,ylim='own',grid=True, fade=True,linewidth=0, colormap=cm.inferno)
#plt.colorbar(orientation='vertical',shrink=0.3,aspect=4, label = "Span of Control")
#x_DEC = np.clip(np.random.normal(-1.7, 2, 6000), -5.3, 3.5)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#
#plt.hist(x_DEC)
#
#x_NOV = np.clip(np.random.normal(5.7, 2, 6000), 1.7, 11.3)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_NOV, bottom=NUMBER_PROBEL)
#
#x_OCT = np.clip(np.random.normal(12.9, 2, 6000), 8.5, 18.8)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_OCT, bottom=NUMBER_PROBEL*2)
#
#x_SEP = np.clip(np.random.normal(20.5, 2, 6000), 15.8, 26.4)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_SEP, bottom=NUMBER_PROBEL*3)
#
#x_AUG = np.clip(np.random.normal(24.7, 2, 6000), 20, 30.2)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_AUG, bottom=NUMBER_PROBEL*4)
#
#x_JUL = np.clip(np.random.normal(26.3, 2, 6000), 21.4, 31.9)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_JUL, bottom=NUMBER_PROBEL*5)
#
#x_JUN = np.clip(np.random.normal(23.3, 2, 6000), 18.4, 28.9)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_JUN, bottom=NUMBER_PROBEL*6)
#
#x_MAY = np.clip(np.random.normal(17.6, 2, 6000), 12.6, 23.6)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_MAY, bottom=NUMBER_PROBEL*7)
#
#x_APR = np.clip(np.random.normal(11.7, 2, 6000), 6.7, 18.4)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_APR, bottom=NUMBER_PROBEL*8)
#
#x_MAR = np.clip(np.random.normal(5.1, 2, 6000), 0.2, 12)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_MAR, bottom=NUMBER_PROBEL*9)
#
#x_FEB = np.clip(np.random.normal(-2.1, 2, 6000), -6.4, 4.3)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_FEB, bottom=NUMBER_PROBEL*10)
#
#x_JAN = np.clip(np.random.normal(-3.4, 2, 6000), -7.2, 2.3)  ##mean std_dev size Ограничиваем полученные значения в диапазоне [-20, -10]
#plt.hist(x_JAN, bottom=NUMBER_PROBEL*11)

plt.xlabel('Mean Temperature (t)')
plt.ylabel('Month')
plt.title('Temperature in Lincoln NE')
#plt.yticks(y, labels)  # Задаем текстовые метки для оси x

plt.show()