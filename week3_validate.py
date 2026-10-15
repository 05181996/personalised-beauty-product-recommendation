
import pandas as pd

file_name = "week3_prepared_events.csv"
chunk_size = 200000

total_rows = 0
duplicate_count = 0
negative_count = 0
zero_count = 0
outlier_count = 0
missing_session_count = 0
missing_brand_count = 0
missing_category_count = 0
invalid_timestamp_count = 0

for chunk in pd.read_csv(file_name, chunksize=chunk_size):
    total_rows += len(chunk)

    duplicate_count += int(chunk["is_duplicate"].sum())
    negative_count += int(chunk["is_negative_price"].sum())
    zero_count += int(chunk["is_zero_price"].sum())
    outlier_count += int(chunk["is_price_outlier"].sum())
    missing_session_count += int(chunk["missing_user_session"].sum())

    missing_brand_count += int(chunk["brand"].isna().sum())
    missing_category_count += int(chunk["category_code"].isna().sum())

    timestamps = pd.to_datetime(
        chunk["event_time"], utc=True, errors="coerce"
    )
    invalid_timestamp_count += int(timestamps.isna().sum())

print("\n--- VALIDATION RESULTS ---")
print("Total rows:", total_rows)
print("Duplicate rows flagged:", duplicate_count)
print("Negative prices:", negative_count)
print("Zero prices:", zero_count)
print("Potential price outliers:", outlier_count)
print("Missing sessions:", missing_session_count)
print("Missing original brand values:", missing_brand_count)
print("Missing original category codes:", missing_category_count)
print("Invalid timestamps:", invalid_timestamp_count)

print("\nValidation completed.")

