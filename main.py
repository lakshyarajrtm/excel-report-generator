import pandas as pd

COLUMN_ALIASES = {
    "date": ["date", "sale_date", "order_date"],
    "product": ["product", "product_name", "item"],
    "quantity": ["quantity", "qty", "units"],
    "revenue": ["revenue", "sales", "total", "amount"]
}

def read_csv(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    cols = df.columns
    required_cols = {"Date", "Product", "Quantity", "Revenue"}
    missing_cols = required_cols - set(df.columns)

    if missing_cols:
        raise ValueError(f"Missing columns {', '.join(sorted(missing_cols))}")

    
    