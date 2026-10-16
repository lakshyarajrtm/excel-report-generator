from loader import *

required_cols = set(COLUMN_ALIASES.keys())

df = read_csv("sales.csv", required_cols)
print(df.columns)