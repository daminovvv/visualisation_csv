from io import StringIO

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def figures_from_csv_string(csv_string: str) -> list | None:
    df = pd.read_csv(StringIO(csv_string), sep=';', quoting=3)
    df.columns = df.columns.str.strip('"')

    figures = [px.scatter(df, x='client', y='tps', title='tps(client)'),
               px.scatter(df, x='client', y='latency', title='latency(client)'),
               px.scatter(df, x='client', y='stddev', title='stddev(client)')]

    return figures


def plot_html_from_csv_string(csv_string: str):
    figures = figures_from_csv_string(csv_string)
    plot_html = []
    for figure in figures:
        plot_html.append(figure.to_html(full_html=False))
    return plot_html


def png_bytes_from_csv_string(csv_string: str):
    figures = figures_from_csv_string(csv_string)
    united_fig = make_subplots(rows=3, cols=1, subplot_titles=["tps(client)", "latency(client)", "stddev(client)"])
    for i in range(len(figures)):
        united_fig.add_trace(go.Figure(figures[i]).data[0], row=i + 1, col=1)
    png_bytes = united_fig.to_image(format="png", engine="kaleido")
    return png_bytes
