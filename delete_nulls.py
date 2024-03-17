import pandas as pd
from pandas.io.formats.style_render import DataFrame

import numpy as np

data_from_file = pd.read_excel('stroke_rus.xlsx')

def get_nulls_count(data_frame: DataFrame, columns):
  null_column = data_frame[columns].isnull().sum(axis=1)
  return null_column.value_counts()

print("Кол-во пропусков до замены в столбце 'Курение': ")
print(get_nulls_count(data_from_file, ["Индекс массы тела", "Курение"]))

data_from_file.loc[(data_from_file["Курение"].isnull()), ("Курение")] = "Неизвестно"

print("\nКол-во пропусков после замены в столбце 'Курение': ")
print(get_nulls_count(data_from_file, ["Индекс массы тела", "Курение"]))

data_from_file = data_from_file.drop(data_from_file[data_from_file["Индекс массы тела"].isnull()].index)

print("\nКол-во пропусков после удаления в столбце 'Индекс массы тела': ")
print(get_nulls_count(data_from_file, ["Индекс массы тела", "Курение"]))

data_from_file = data_from_file[data_from_file.Пол != 'Other']

data_from_file.to_excel("stroke_rus_cleaned.xlsx")