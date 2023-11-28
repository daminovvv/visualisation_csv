# Visualisation CSV

![example workflow](https://github.com/daminovvv/visualisation_csv/actions/workflows/main.yml/badge.svg)

---
## Описание
Приложение позволяет создавать графики из csv файлов с помощью plotly. Загруженные файлы хранятся в БД, можно получить графики по айди документа. 
Есть поддержка Apache ECharts. Добавлена возможность экспорта графиков в формате png и данных в формате csv.

## Стек
FastAPI, SQLAlchemy, Alembic, Postgres, Plotly, Jinja2

---
## Установка и запуск

---

#### 1. Клонирование репозитория
```
git clone https://github.com/daminovvv/game-of-life.git
```


#### 2. Запуск контейнеров
```
docker compose up
```

### 3. Перейти на стартовую страницу

http://127.0.0.1:8000/

