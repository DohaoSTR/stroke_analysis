import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_from_file = pd.read_excel('stroke_rus_cleaned.xlsx')

fig, ((ax1, ax2) ,(ax3,ax4)) = plt.subplots(2,2, figsize=(14,8))
sns.countplot(data=data_from_file, x="Пол", hue="Инсульт",ax=ax1)
sns.countplot(data=data_from_file, x="Был женат/замужем", hue="Инсульт",ax=ax2)
sns.countplot(data=data_from_file, x="Тип работы", hue="Инсульт",ax=ax3)
sns.countplot(data=data_from_file, x="Курение", hue="Инсульт",ax=ax4)

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,6))
sns.countplot(data=data_from_file, x="Гипертония", hue="Инсульт",ax=ax1)
sns.countplot(data=data_from_file, x="Сердечная недостаточность", hue="Инсульт",ax=ax2)

fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(18,7))
sns.histplot(data=data_from_file, x='Возраст', hue='Инсульт', element="step",ax=ax1)
sns.histplot(data=data_from_file, x='Средний уровень глюкозы', hue='Инсульт', element="step",ax=ax2)
sns.histplot(data=data_from_file, x='Индекс массы тела', hue='Инсульт', element="step",ax=ax3)

numerical_data = data_from_file[['Возраст','Средний уровень глюкозы','Индекс массы тела','Инсульт']]
numerical_data = sns.pairplot(numerical_data, hue='Инсульт')

#Вывод графиков соотношения различных столбцов и столбца инсультов: