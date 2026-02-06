# Одностраничный Power BI отчет - визуализация Brazilian E-Commerce

Дашборд в Power BI по открытым данным бразильского маркетплейса Olist. Данные загружаются в локальную SQLite-базу скриптом и подключаются к отчёту через ODBC.

---

## Данные

- **Источник:** [Brazilian E-Commerce (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) 
- Необходимо скачать набор данных, и положить в папку `kaggle_data`
- Набор содержит заказы, товары, платежи, геолокацию
- Добален [справочник](spr_category.xlsx) классификатор продуктов в категории для удобства.

---

## Преобразовать csv в БД

- Требуется SQLite

```bash
pip install -r requirements.txt
python build_sqlite_db.py
```

Скрипт создаёт файл **SQLite_bi_sample.db** в корне проекта.

---

## Результаты

| Файл | Описание |
|------|----------|
| [**Report.pbix**](Report.pbix) | Отчёт Power BI (открывается в Power BI Desktop с версии 2.150.2102.0 64-bit (Январь 2026)) |
| [**Report.pdf**](Report.pdf) | PDF-версия отчёта для быстрого просмотра |

---

## Структура репозитория

- `build_sqlite_db.py` - скрипт загрузки CSV из `kaggle_data/` в SQLite  
- `kaggle_data/` - папка с CSV датасета Olist  
- `SQLite_bi_sample.db` - база SQLite (создаётся скриптом)  
- `Report.pbix` - отчёт Power BI  
- `Report.pdf` - отчёт в PDF  
- `spr_category.xlsx` - справочник в эскселе
