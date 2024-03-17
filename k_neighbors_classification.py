from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score

from sklearn.model_selection import cross_validatae
from sklearn.model_selection import cross_val_predict

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def cross_val(model,x, y, cv = 10):
    cv_res = cross_validate(estimator=model,X=x,y=y,n_jobs=-1,cv=cv,return_train_score = True)
    y_pred = cross_val_predict(estimator=model,X=x,y=y,n_jobs=-1,cv=cv)
    print('Точность обучающей выборки:',cv_res['train_score'].mean())
    print('Точность тестовой выборки:',accuracy_score(y,y_pred))
    plt.figure(figsize=(5,5))
    sns.heatmap(confusion_matrix(y,y_pred),annot=True,cmap='GnBu',fmt = 'd')
    plt.title('Матрица ошибок',color='black')
    plt.show()
    print(classification_report(y,y_pred))

def standard_classification(model, x, y):
  x_training, x_test, y_training, y_test = train_test_split(x, y, test_size = 0.3)

  model.fit(x_training, y_training)
  y_pred = model.predict(x_test)

  plt.figure(figsize=(2,2))
  sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='GnBu', fmt = 'd')
  plt.title('Матрица ошибок',color='black')
  plt.show()

  print(classification_report(y_test, y_pred))
  print('Точность обучающей выборки:', model.score(x_training, y_training))
  print('Точность тестовой выборки:', accuracy_score(y_test, y_pred))

def standard_svc(model, x, y):
  x_training, x_test, y_training, y_test = train_test_split(x, y, test_size = 0.3)

  model.fit(x_training, y_training)
  y_pred = model.predict(x_test)

  plt.figure(figsize=(2,2))
  sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='GnBu', fmt = 'd')
  plt.title('Матрица ошибок',color='black')
  plt.show()

  print(classification_report(y_test, y_pred))
  print('Точность обучающей выборки:', model.score(x_training, y_training))
  print('Точность тестовой выборки:', accuracy_score(y_test, y_pred))

  return model

#cross_val(KNeighborsClassifier(n_neighbors=1), x_scaled, y_scaled)
standard_classification(KNeighborsClassifier(n_neighbors = 3), x_scaled, y_scaled)
#standard_svc(SVC(probability=True), x_scaled, y_scaled)