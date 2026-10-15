
import pandas as pd

# 1. Load original dataset
df = pd.read_csv("2019-Dec.csv")
original_rows = len(df)

print("Original dataset shape:", df.shape)

# 2. Flag duplicate rows before adding new columns
df["is_duplicate"] = df.duplicated(keep="first")

# 3. Standardize event types
df["event_type"] = df["event_type"].str.strip().str.lower()

# 4. Create cleaned brand and category columns
df["brand_clean"] = (
    df["brand"].fillna("Unknown").astype(str).str.strip().str.lower()
)

df["category_code_clean"] = (
    df["category_code"].fillna("Unknown").astype(str).str.strip()
)

# 5. Convert timestamps to UTC
df["event_time"] = pd.to_datetime(
    df["event_time"], utc=True, errors="coerce"
)

# 6. Create time-based features
df["event_date"] = df["event_time"].dt.strftime("%Y-%m-%d")
df["event_hour"] = df["event_time"].dt.hour
df["day_of_week"] = df["event_time"].dt.day_name()

# 7. Flag unusual prices
df["is_nonpositive_price"] = df["price"] <= 0
df["is_negative_price"] = df["price"] < 0
df["is_zero_price"] = df["price"] == 0

# 8. Identify potential outliers using IQR
q1 = df["price"].quantile(0.25)
q3 = df["price"].quantile(0.75)
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

df["is_price_outlier"] = (
    (df["price"] < lower_limit) |
    (df["price"] > upper_limit)
)

# 9. Flag missing session IDs
df["missing_user_session"] = df["user_session"].isna()

# 10. Print cleaning summary
print("\n--- CLEANING SUMMARY ---")
print("Original rows:", original_rows)
print("Prepared rows:", len(df))
print("Duplicate rows flagged:", df["is_duplicate"].sum())
print("Invalid timestamps:", df["event_time"].isna().sum())
print("Negative prices:", df["is_negative_price"].sum())
print("Zero prices:", df["is_zero_price"].sum())
print("Potential price outliers:", df["is_price_outlier"].sum())
print("Missing brand values:", df["brand"].isna().sum())
print("Missing category codes:", df["category_code"].isna().sum())
print("Missing sessions:", df["missing_user_session"].sum())

print("\nIQR lower limit:", lower_limit)
print("IQR upper limit:", upper_limit)

# 11. Save as a new file
output_file = "week3_prepared_events.csv"
df.to_csv(output_file, index=False)

print("\nPrepared dataset saved as:", output_file)
print("Original dataset was not modified.")

