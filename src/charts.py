import plotly.express as px
import pandas as pd


def get_plot_html() -> list:
    # Загрузка данных из CSV файла
    df = pd.read_csv('data/short.csv')

    # Создание интерактивного графика
    fig1 = px.scatter(df, x='client', y='tps', title='tps Plot Title')
    fig2 = px.scatter(df, x='client', y='latency', title='latency Plot Title')
    fig3 = px.scatter(df, x='client', y='stddev', title='stddev Plot Title')
    # Конвертация графика в HTML

    plot_html = []
    plot_html.append(fig1.to_html(full_html=False))
    plot_html.append(fig2.to_html(full_html=False))
    plot_html.append(fig3.to_html(full_html=False))
    return plot_html
