import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats

data_from_file = pd.read_excel('stroke_rus_cleaned.xlsx')

ages = data_from_file["Возраст"]
print("Максимальный возраст - ", max(ages))
print("Минимальный возраст - ", min(ages))

# обычно - глюкоза от 50 до 120 ммоль (к тому же есть дети у которых
# уровень глюкозы ниже)
glucose = data_from_file["Средний уровень глюкозы"]
print()
print("Максимальный уровень глюкозы - ", max(glucose))
print("Минимальный уровень глюкозы - ", min(glucose))

# индекс массы тела
mass = data_from_file["Индекс массы тела"]
print()
print("Максимальный индекс массы тела - ", max(mass))
print("Минимальный индекс массы тела - ", min(mass))

data_from_file = pd.read_excel('stroke_rus_cleaned.xlsx')

sns.catplot(data=data_from_file, x="Инсульт", y="Возраст", kind="box")
index = data_from_file[((data_from_file['Возраст'] < 20) & (data_from_file['Инсульт'] == 1)) ].index
data_from_file.drop(index , inplace=True)

sns.catplot(data=data_from_file, x="Инсульт", y="Средний уровень глюкозы", kind="box")
index = data_from_file[((data_from_file['Средний уровень глюкозы'] > 220) & (data_from_file['Инсульт'] == 0)) ].index
data_from_file.drop(index , inplace=True)

sns.catplot(data=data_from_file, x="Инсульт", y="Индекс массы тела", kind="box")
index = data_from_file[((data_from_file['Индекс массы тела'] > 50) & (data_from_file['Инсульт'] == 0)) ].index
data_from_file.drop(index , inplace=True)

index = data_from_file[((data_from_file['Индекс массы тела'] > 40) & (data_from_file['Инсульт'] == 1)) ].index
data_from_file.drop(index , inplace=True)

index = data_from_file[((data_from_file['Индекс массы тела'] < 19) & (data_from_file['Инсульт'] == 1)) ].index
data_from_file.drop(index , inplace=True)

dataframe_to_save = pd.DataFrame(data_from_file)
dataframe_to_save.to_excel("stroke_rus_emissions.xlsx")