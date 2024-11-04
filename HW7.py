import pandas as pd
import seaborn as sns
from plotly.offline import iplot
import plotly.graph_objs as go

# Функция для загрузки данных из CSV-файла
def load_data():
    df = pd.read_csv("web_clients_correct.csv")
    return df

# Преобразование данных (при необходимости)
def preprocess_data(df):
    # Здесь можно выполнить необходимые преобразования данных
    return df

# Формирование диаграммы разброса зависимости возраста клиента от расходов (scatterplot) с помощью Seaborn и Plotly
def create_scatterplot(df):
    sns.set(style="darkgrid")
    g = sns.scatterplot(x="age", y="expenses", data=df)
    iplot(g)

# Сформировать линию регрессии к диаграмме рассеяния (regplot) с помощью Seaborn
def create_regression_plot(df):
    sns.regplot(x="age", y="expenses", data=df, scatter=False)

# Загрузка данных и преобразование
df = load_data()
df = preprocess_data(df)

# Задание 1: создание диаграммы разброса
create_scatterplot(df)

# Задание 2: создание линии регрессии
create_regression_plot(df)
