import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

def encode_binary_column(column_data):
  column_label_encoder = LabelEncoder()
  return column_label_encoder.fit_transform(column_data)

def encode_categorical_column(columns, index):
  ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), index)],
    remainder='passthrough'
  )
  columns = ct.fit_transform(columns)

  return columns

data_from_file = pd.read_excel('stroke_rus_emissions.xlsx')

sex_column = data_from_file.iloc[:, 0].values
married_column = data_from_file.iloc[:, 4].values
place_column = data_from_file.iloc[:, 6].values

sex_column = encode_binary_column(sex_column)
married_column = encode_binary_column(married_column)
place_column = encode_binary_column(place_column)

work_type_column = data_from_file.iloc[:, 5].values
smoke_status_column = data_from_file.iloc[:, 9].values

work_type_column = encode_binary_column(work_type_column)
smoke_status_column = encode_binary_column(smoke_status_column)

data_from_file.iloc[:, 0] = sex_column;
data_from_file.iloc[:, 4] = married_column;
data_from_file.iloc[:, 6] = place_column;

data_from_file.iloc[:, 5] = work_type_column;
data_from_file.iloc[:, 9] = smoke_status_column;

columns = encode_categorical_column(data_from_file, [5, 9])
data_from_file = pd.DataFrame(columns)

dataframe_to_save = pd.DataFrame(data_from_file)
dataframe_to_save.to_excel("stroke_rus_processed.xlsx")

#Перевод категориальных признаков в числовые: