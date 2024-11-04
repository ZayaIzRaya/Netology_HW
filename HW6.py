import pandas as pd

# Функция для анализа возраста
def age_analysis(age):
    if age > 25:
        return "Старше 25"
    else:
        return "Младше или равен 25"

# Загрузка данных из CSV-файла
df = pd.read_csv("web_clients_correct.csv")

# Применение функции age_analysis к столбцу age
df["age_category"] = df["age"].apply(age_analysis)

# Вывод результата задания 1
print("Задание 1:")
print(df["age_category"].values)

# Отбор DataFrame по условиям поля 'sex' и 'age'
filtered_df = df[(df["sex"] == "мужской") & (df["age"] > 30)]

# Вывод результата задания 2
print("\nЗадание 2:")
print(filtered_df)
