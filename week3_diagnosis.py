
import pandas as pd

# Load the original dataset
df = pd.read_csv("2019-Dec.csv")

print("DATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nEXACT DUPLICATE ROWS")
print(df.duplicated().sum())

print("\nPRICE SUMMARY")
print(df["price"].describe())

print("\nNEGATIVE PRICES")
print((df["price"] < 0).sum())

print("\nZERO PRICES")
print((df["price"] == 0).sum())

print("\nEVENT COUNTS")
print(df["event_type"].value_counts())

print("\nTIMESTAMP CHECK")
timestamps = pd.to_datetime(
    df["event_time"], utc=True, errors="coerce"
)
print("Invalid timestamps:", timestamps.isna().sum())

print("\nDIAGNOSIS COMPLETE")

import pandas as pd

# Load the original dataset
df = pd.read_csv("2019-Dec.csv")

# 1. Inspect exact duplicate rows
print("\n--- DUPLICATE INSPECTION ---")
print("Exact duplicate rows:", df.duplicated().sum())

print("\nExamples of duplicate rows:")
print(df[df.duplicated(keep=False)].head(10).to_string(index=False))

# 2. Check event types
print("\n--- EVENT TYPE COUNTS ---")
print(df["event_type"].value_counts(dropna=False))

# 3. Inspect negative prices
print("\n--- NEGATIVE PRICE RECORDS ---")
print(df[df["price"] < 0].head(20).to_string(index=False))

# 4. Inspect zero prices
print("\n--- ZERO PRICE RECORDS ---")
print(df[df["price"] == 0].head(10).to_string(index=False))

# 5. Calculate price quartiles and IQR
print("\n--- PRICE OUTLIER CHECK ---")
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower investigation limit:", lower_limit)
print("Upper investigation limit:", upper_limit)

outliers = df[
    (df["price"] < lower_limit) |
    (df["price"] > upper_limit)
]

print("Potential price outliers:", len(outliers))
print("\nExamples of potential price outliers:")
print(outliers[["product_id", "brand", "price", "event_type"]]
      .head(10).to_string(index=False))

# 6. Check timestamp conversion
print("\n--- TIMESTAMP CHECK ---")
df["event_time"] = pd.to_datetime(
    df["event_time"], utc=True, errors="coerce"
)
print("Invalid timestamps:", df["event_time"].isna().sum())
print("Earliest timestamp:", df["event_time"].min())
print("Latest timestamp:", df["event_time"].max())

print("\nDiagnostic inspection completed.")

