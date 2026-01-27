import pandas as pd
from pathlib import Path

# Define project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_PROCESSED = PROJECT_ROOT / 'data' / 'processed'

# Load the cleaned dataset
df = pd.read_csv(DATA_PROCESSED / 'clean_operationtime_departure.csv')

print('VERIFICATION OF CLEANED DATA')
print('='*80)

print('\n1. OPERATIONTIME VALIDATION:')
print(f'   - Data type: {df["operationtime"].dtype}')
print(f'   - Total values: {len(df)}')
print(f'   - Non-null values: {df["operationtime"].notna().sum()}')
print(f'   - Null values: {df["operationtime"].isna().sum()}')
print(f'   - Sample values:')
print(df[["operationtime"]].head())

print('\n2. DERIVED FEATURES VALIDATION:')
print(f'   - hour range: {df["hour"].min()} to {df["hour"].max()}')
print(f'   - Unique weekdays: {sorted(df["weekday"].unique())}')
print(f'   - Unique months: {sorted(df["month"].unique())}')
print(f'   - Date format sample: {df["date"].head(3).tolist()}')

print('\n3. DEPARTUREORARRIVAL VALIDATION:')
print(f'   - Unique values: {sorted(df["departureorarrival"].unique())}')
print(f'   - Value counts:')
print(df["departureorarrival"].value_counts(dropna=False))

print('\n4. NO ROWS DROPPED:')
print(f'   - Original rows: 5856')
print(f'   - Final rows: {len(df)}')
print(f'   - Rows dropped: {5856 - len(df)}')

print('\n5. SAMPLE OF CLEANED DATA:')
print(df[["operationtime", "departureorarrival", "hour", "weekday", "month", "date"]].head(15))

print('\n6. DISTRIBUTION OF HOURS:')
print(df["hour"].value_counts().sort_index())

print('\n7. DISTRIBUTION OF WEEKDAYS:')
print(df["weekday"].value_counts())

print('\n8. DISTRIBUTION OF MONTHS:')
print(df["month"].value_counts())
