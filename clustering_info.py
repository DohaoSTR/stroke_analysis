import numpy as np

labeled_dataset = x.copy()
labeled_dataset['Инсульт'] = y
labeled_dataset['Кластер'] = labels

first_cluster = labeled_dataset[labeled_dataset['Кластер'] == 0]
second_cluster = labeled_dataset[labeled_dataset['Кластер'] == 1]

labeled_real_values = x.copy()
labeled_real_values['Инсульт'] = y
labeled_real_values['Кластер'] = labeled_dataset['Кластер']

y[y == "Не был"] = 0
y[y == "Был"] = 1

print('Mean Absolute Error:', metrics.mean_absolute_error(y, labels))
print('Mean Squared Error:', metrics.mean_squared_error(y, labels))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y, labels)))

print(len(first_cluster))
print(len(second_cluster))

#first_cluster
#second_cluster
labeled_real_values