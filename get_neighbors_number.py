import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import numpy as np

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, test_size = 0.3)

def get_neighbors():
  error_rates = []
  plt.figure(figsize=(5,5))

  for i in np.arange(1, 20):
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(x_train, y_train)
    new_predictions = new_model.predict(x_test)
    error_rates.append(np.mean(new_predictions != y_test))

  plt.plot(error_rates)

get_neighbors()

#Определение оптимального значения k: