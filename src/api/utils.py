from datetime import datetime
from io import StringIO

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from fastapi import UploadFile
from plotly.subplots import make_subplots

from src.startup import logger


def figures_from_csv_string(csv_dict: dict) -> list | None:
    df = pd.read_csv(StringIO(csv_dict["content"]), sep=';', quoting=3)
    df.columns = df.columns.str.strip('"')
    columns = csv_dict["description"]["columns"]
    df[columns[0]] = df[columns[0]].str.replace('"', '').astype(float)
    for column in columns[1:]:
        df[column] = df[column].str.replace(',', '.').astype(float)
    figures = [px.scatter(df, x=columns[0], y=columns[i],
                          title=f'{columns[i]}({columns[0]})') for i in range(1, len(columns))]
    return figures


def plot_html_from_csv_string(csv_dict: dict):
    figures = figures_from_csv_string(csv_dict)
    plot_html = []
    for figure in figures:
        plot_html.append(figure.to_html(full_html=False))
    return plot_html


def png_bytes_from_csv_string(csv_dict: dict) -> bytes:
    figures = figures_from_csv_string(csv_dict)
    columns = csv_dict["description"]["columns"]
    subplot_titles = [f'{columns[i]}({columns[0]})' for i in range(1, len(columns))]
    united_fig = make_subplots(rows=3, cols=1, subplot_titles=subplot_titles)

    for i in range(len(figures)):
        united_fig.add_trace(go.Figure(figures[i]).data[0], row=i + 1, col=1)
    png_bytes = united_fig.to_image(format="png", engine="kaleido")
    return png_bytes


def csv_file_processing(file: UploadFile) -> dict:
    csv_content = file.file.read().decode('utf-8-sig')
    columns_line = csv_content.split('\n')[0]
    columns_list_no_quotes = [column[1:-1] for column in columns_line.split(';')]
    columns_list_no_quotes[-1] = columns_list_no_quotes[-1][:-1]  # В крайней колонке есть 1 доп символ в окончании

    return {"name": file.filename,
            "content": csv_content,
            "description": {"created_at": datetime.utcnow().strftime("%Y-%m-%d"),
                            "file_format": "csv",
                            "columns": columns_list_no_quotes}
            }


def translate_columns(csv_dict: dict) -> dict:
    VOCABULARY = {"client": "клиент",
                  "tps": "транзакций в секунду",
                  "latency": "время ожидания",
                  "stddev": "cтандартное отклонение"}
    columns = csv_dict["description"]["columns"]
    for i in range(len(columns)):
        if columns[i] in VOCABULARY:
            columns[i] = VOCABULARY[columns[i]]
    first_row = "\"" + "\";\"".join(columns) + "\"\n"
    csv_dict["content"] = first_row + "\n".join(csv_dict["content"].split('\n')[1:])
    return csv_dict
