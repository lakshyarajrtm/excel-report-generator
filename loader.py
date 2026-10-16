

import pandas as pd

COLUMN_ALIASES = {
    "order_date": ["sale_date", "order_date", "orderdate"],
    "product": ["product", "product_name", "item", "productname"],
    "quantity": ["quantity", "qty", "units"],
    "revenue": ["revenue", "sales", "total", "amount", "total_price", "totalprice"]
}

def read_csv(filename, required_cols):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    df.columns = (
                    df.columns
                        .str.strip()
                        .str.lower()
                        .str.replace(" ", "_")
                 )
    columns_mapping = {}
    for col in df.columns:
        new_col = find_col(col, COLUMN_ALIASES)
        columns_mapping[col] = new_col if new_col else col
    df = df.rename(columns=columns_mapping)
    missing_cols = set()
    for col in required_cols:
        if col not in df.columns:
            missing_cols.add(col)
    if missing_cols:
        raise ValueError(f"Columns missing: {", ".join(sorted(missing_cols))}")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    return df

    
def find_col(col_name, aliases):
    for col in aliases.keys():
            if col_name in aliases[col]:
                return col
    return None