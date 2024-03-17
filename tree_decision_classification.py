import pandas as pd
import graphviz
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

x_training, x_test, y_training, y_test = train_test_split(x, y, test_size = 0.3)

model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
model.fit(x_training, y_training)
y_pred = model.predict(x_test)

plt.figure(figsize=(2,2))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='GnBu', fmt = 'd')
plt.title('Матрица ошибок',color='black')
plt.show()

print(classification_report(y_test, y_pred))
print('Точность обучающей выборки:', model.score(x_training, y_training))
print('Точность тестовой выборки:', accuracy_score(y_test, y_pred))

# Экспорт как точка
dot_data = export_graphviz(model, out_file=None, class_names=['Был', 'Не был'],
                           feature_names=data_from_file.drop("Инсульт", axis=1).columns, impurity=False, filled=True)
graph = graphviz.Source(dot_data)
graph.render('tree')

graph.save("graph")

#Классификация методом дерева решений:
#Лучший результат:
#Обучающая выборка - 99 %
#Тестовая выборка - 95 %
#Параметры: без стандартизации данных, criterion - entropy, глубина - 15


#1.Возраст больше 67 лет, наемная работа.
#2.Возраст больше 67 лет, госслужба, средний уровень глюкозы больше 220.
#3.Частный предприниматель, сердечная недостаточность, курит.

#Возраст больше 67 лет, 
#работал на какой либо работе (больше всего вероятность инсульта если работал на наемной работе, 
#далее частный предприниматель и госслужба). Есть параметры которые увеличивают вероятность инсульта, 
#если уровень глюкозы больше 220 ммоль или присутствует сердечная недостаточность и при этом 
#человек курит, наличие гипертонии, был женат/замужем, к тому же у женщин по определению больше 
#вероятность. Индекс массы тела, выше 35, меньше 20.