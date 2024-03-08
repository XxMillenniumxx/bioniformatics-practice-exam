#Опциональное задание. ООП. Создать класс "Биоинформатик", нужно придумать ему атрибуты, например, рост, вес, интелект, скиллы, и прочее, пофантазируйте. Еще надо придумать ему способности (методы класса), например, он умеет ругаться на плохие данные, считать до миллиона, писать код, рисовать случайные картинки и прочее. Тоже что-нибудь придумайте, попробуйте свое видение биоинформатика как-нибудь отобразить в виде сущности на питоне. Сделать хотя бы 5 методов и 5 атрибутов. Кстати, методы могут менять и быть зависимы от атрибутов, например, есть атрибут степень бодрости и от него зависит до скольки может досчитать биоинформатик или насколько много точек отображается на его случайных графиках, или что-то более правдоподобное как в DnD.
from random import randint
from random import choice
from random import choices
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Bioinformatic:
    def __init__(self):
        self.iq = round(np.random.normal(100,15,1)[0])
        self.self_contol = randint(0,100)
        self.extroversion = randint(0,100)
        
        self.tiredness = 0
        self.knowledge = 0
        
    def roll_d20(self):
        return randint(1, 20)
        
    def pass_stepik_coirse(self,with_tasks = False):
        print("Биоинформатик изучает курс на степике")
        if with_tasks:
            self.tiredness += 1000000000000000
            self.knowledge += 20
        else:
            self.tiredness += 10
            print("Биоинформатик кидает кубик d20")
            self.knowledge += self.roll_d20()
        #print(self.tiredness,self.knowledge)
        
    def create_table_with_characteristics_use_pandas(self):
        print("Биоинформатик пытается создать таблицу со своими характеристиками")
        if self.knowledge > 5:
            data = {
            'iq':self.iq,
            'self_contol':self.self_contol,
            'extroversion':self.extroversion,
            'tiredness':self.tiredness,
            'knowledge':self.knowledge,
            }
            df = pd.DataFrame(data=data,index =[0])
            print(df)
        else:
            print("Создать таблицу не получилось")
        
    def create_plot_with_matplotlib(self):
        if self.knowledge > 100:
            data = [33, 25, 20, 12, 10]
            plt.figure(num=1, figsize=(6, 6))
            plt.axes(aspect=1)
            plt.title('Plot 3', size=14)
            plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
            plt.show()
        elif self.knowledge > 80:
            # равномерно распределённые значения от 0 до 5, с шагом 0.2
            t = np.arange(0., 5., 0.2)
            
            # красные чёрточки, синие квадраты и зелёные треугольники
            plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
            plt.show()
        elif self.knowledge > 40:
            t = np.arange(0, 2*np.pi, 0.01)
            r = 4
            plt.plot(r*np.sin(t), r*np.cos(t), lw=3)
            plt.axis('equal')
            plt.show()
        else:
            print("не получилось нарисовать график")
            
    def make_choice(self):
        print("Биоинформатик делает выбор")
        choice = choices(
					["Купить пиццу, торт","Купить овсянку и бананы"],
					weights=[
					        self.tiredness,
							self.self_contol,
				    ]
				)[0]
        if choice == "Купить пиццу, торт":
            self.tiredness = 0
            print(choice)
        else:
            self.tiredness -= 100
            print(choice)
        
            
    def evaluate_future_success(self):
        if self.iq > 120:
            print("Биоинформатик прошёл верхний порог iq для своей профессии, дальнейший успех может быть предсказан по дисциплинированности и экстроверсии "+str(self.self_contol+self.extroversion))
        elif self.iq > 115:
            print("Биоинформатик прошёл минимальный порог iq для своей профессии, дальнейший успех может быть предсказан по дисциплинированности и экстроверсии "+str(self.self_contol+self.extroversion))
        elif self.iq > 100:
            print("Биоинформатик имеет средний iq, дальнейший успех может быть предсказан по дисциплинированности и экстроверсии "+str(self.self_contol+self.extroversion))
        else:
            print("Биоинформатик имеет iq ниже среднего, дальнейший успех может быть предсказан по дисциплинированности и экстроверсии "+str(self.self_contol+self.extroversion))
    
        
bioinformatic = Bioinformatic()


#print(bioinformatic.iq,bioinformatic.self_contol,bioinformatic.extroversion,bioinformatic.tiredness,bioinformatic.knowledge)
bioinformatic.create_table_with_characteristics_use_pandas()
bioinformatic.pass_stepik_coirse()
bioinformatic.make_choice()
bioinformatic.evaluate_future_success()
bioinformatic.create_plot_with_matplotlib()

for i in range(1,9):
    bioinformatic.pass_stepik_coirse()
bioinformatic.create_table_with_characteristics_use_pandas()
bioinformatic.create_plot_with_matplotlib()
