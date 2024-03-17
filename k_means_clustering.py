import matplotlib.pyplot as plt
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D

def plot2D(x, y, labels, x_label, y_label):
  fig = plt.figure(figsize=(20,7))
  ax = fig.add_subplot()
  scatter = ax.scatter(x, y, c = labels, cmap="Dark2", linewidths = 0.1);
  ax.legend(*scatter.legend_elements())
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()

def plot3D(x, y, z, labels, x_label, y_label, z_label):
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')
  scatter = ax.scatter3D(x, y, z, c = labels, cmap="Dark2");
  ax.legend(*scatter.legend_elements())
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_zlabel(z_label)
  plt.show()

from sklearn.cluster import KMeans

def kmeans(df, n_clusters):
    kmeans = KMeans(n_clusters = n_clusters)
    kmeans.fit(df)

    return model, kmeans.labels_

model, labels = kmeans(x, 2)
plot2D(x['Возраст'], x['Средний уровень глюкозы'], labels, 'Возраст', 'Средний уровень глюкозы')
plot2D(x['Возраст'], x['Индекс массы тела'], labels, 'Возраст', 'Индекс массы тела')
plot2D(x['Средний уровень глюкозы'], x['Индекс массы тела'], labels, 'Средний уровень глюкозы', 'Индекс массы тела')

plot3D(x['Возраст'], x['Средний уровень глюкозы'], x['Индекс массы тела'], labels, 'Возраст', 'Средний уровень глюкозы', 'Индекс массы тела')