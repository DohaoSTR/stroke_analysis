layers = 10
epoch = 10
learningRate = 0.01
mlp = standard_svc(MLPClassifier(hidden_layer_sizes=(layers), max_iter=int(epoch), learning_rate_init=float(learningRate)), x_scaled, y_scaled)

#!pip install ann_visualizer
from ann_visualizer.visualize import ann_viz

#ann_viz(mlp, filename="dd.gv", title="dd")

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical

model = tf.keras.Sequential()
x_training, x_test, y_training, y_test = train_test_split(x, y, test_size = 0.3)

# Build the model.
model.add(Dense(5, activation='relu', input_shape=(x_training.shape[1],)))
model.add(Dense(5, activation='relu'))
model.add(Dense(5,  activation="softmax"))

# Display the model summary.
model.summary()
ann_viz(model, filename="neuron.gv", title="Перцептрон")