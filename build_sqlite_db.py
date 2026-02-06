"""
Build a SQLite test database from Kaggle Olist CSV files in kaggle_data/.
Run: python build_sqlite_db.py
"""
import sqlite3
from pathlib import Path

import pandas as pd

# Paths
KAGGLE_DIR = Path(__file__).resolve().parent / "kaggle_data"
DB_PATH = Path(__file__).resolve().parent / "SQLite_bi_sample.db"

# CSV file -> table name
CSV_TABLES = [
    ("olist_customers_dataset.csv", "customers"),
    ("olist_geolocation_dataset.csv", "geolocation"),
    ("olist_order_items_dataset.csv", "order_items"),
    ("olist_order_payments_dataset.csv", "order_payments"),
    ("olist_order_reviews_dataset.csv", "order_reviews"),
    ("olist_orders_dataset.csv", "orders"),
    ("olist_products_dataset.csv", "products"),
    ("olist_sellers_dataset.csv", "sellers"),
    ("product_category_name_translation.csv", "product_category_translation"),
]


def main():
    if not KAGGLE_DIR.exists():
        raise FileNotFoundError(f"Folder not found: {KAGGLE_DIR}")

    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)

    for csv_name, table_name in CSV_TABLES:
        csv_path = KAGGLE_DIR / csv_name
        if not csv_path.exists():
            print(f"  Skip (missing): {csv_name}")
            continue
        print(f"Loading {csv_name} -> {table_name} ...")
        df = pd.read_csv(csv_path, low_memory=False)
        df.to_sql(table_name, conn, index=False, if_exists="replace")
        print(f"  -> {len(df):,} rows")

    conn.close()
    print(f"\nDone. Database: {DB_PATH}")


if __name__ == "__main__":
    main()
