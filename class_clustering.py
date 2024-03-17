from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2)
model.fit(x)

labels = model.fit_predict(x)
labeled_dataset = x.copy()
labeled_dataset['Labels'] = labels

print(model.cluster_centers_)

pca_object = PCA(n_components=2, svd_solver='auto')
pca_dataset = pca_object.fit_transform(x)
pca_dataset_df = pd.DataFrame(pca_dataset, columns= ['X', 'Y'])
scaled_pca_dataset_array = scale(pca_dataset_df)
scaled_pca_dataset_df = pd.DataFrame(scaled_pca_dataset_array, columns= ['X','Y'])
scaled_pca_dataset_df['Labels'] = model.labels_

plt.figure(figsize=(10,7))
sns.scatterplot(x= scaled_pca_dataset_df['X'], y= scaled_pca_dataset_df['Y'], hue = scaled_pca_dataset_df['Labels'] )
plt.show()