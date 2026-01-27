import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

# Define project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / 'data' / 'raw'
DATA_PROCESSED = PROJECT_ROOT / 'data' / 'processed'

# Load the dataset
df = pd.read_csv(DATA_RAW / 'flights_clean.csv')

print("=" * 80)
print("INITIAL DATASET ANALYSIS")
print("=" * 80)
print(f"Total rows: {len(df)}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst 5 rows of operationtime:\n{df['operationtime'].head()}")
print(f"\nFirst 5 rows of departureorarrival:\n{df['departureorarrival'].head()}")
print(f"\nUnique values in departureorarrival:\n{df['departureorarrival'].value_counts(dropna=False)}")

# ============================================================================
# STEP 1: CLEAN operationtime
# ============================================================================
print("\n" + "=" * 80)
print("STEP 1: CLEANING operationtime")
print("=" * 80)

# Function to parse datetime safely
def parse_datetime_safe(dt_string):
    """Parse datetime string, return pd.NaT if invalid"""
    try:
        return pd.to_datetime(dt_string, utc=True, format='ISO8601')
    except:
        try:
            # Fallback to general datetime parsing
            return pd.to_datetime(dt_string, utc=True)
        except:
            # Return NaT for invalid/malformed timestamps
            return pd.NaT

# Apply parsing
original_operationtime = df['operationtime'].copy()
df['operationtime'] = df['operationtime'].apply(parse_datetime_safe)

# Count invalid timestamps
invalid_count = df['operationtime'].isna().sum()
valid_count = df['operationtime'].notna().sum()

print(f"Valid timestamps: {valid_count}")
print(f"Invalid/malformed timestamps (set to NULL): {invalid_count}")

# ============================================================================
# STEP 2: EXTRACT DERIVED FEATURES FROM operationtime
# ============================================================================
print("\n" + "=" * 80)
print("STEP 2: EXTRACTING DERIVED FEATURES")
print("=" * 80)

# Extract hour (0-23)
df['hour'] = df['operationtime'].dt.hour

# Extract weekday (Monday-Sunday)
df['weekday'] = df['operationtime'].dt.day_name()

# Extract month (January-December)
df['month'] = df['operationtime'].dt.month_name()

# Extract date (YYYY-MM-DD)
df['date'] = df['operationtime'].dt.date

print(f"Extracted features:")
print(f"  - hour: {df['hour'].notna().sum()} non-null values (range: {df['hour'].min()}-{df['hour'].max()})")
print(f"  - weekday: {df['weekday'].notna().sum()} non-null values")
print(f"  - month: {df['month'].notna().sum()} non-null values")
print(f"  - date: {df['date'].notna().sum()} non-null values")

print(f"\nSample of extracted features:")
print(df[['operationtime', 'hour', 'weekday', 'month', 'date']].head(10))

# ============================================================================
# STEP 3: CLEAN departureorarrival
# ============================================================================
print("\n" + "=" * 80)
print("STEP 3: CLEANING departureorarrival")
print("=" * 80)

# Store original values for comparison
original_departureorarrival = df['departureorarrival'].copy()

# Trim leading and trailing spaces
df['departureorarrival'] = df['departureorarrival'].astype(str).str.strip()

# Convert all values to uppercase
df['departureorarrival'] = df['departureorarrival'].str.upper()

# Count values before replacement
before_cleanup = df['departureorarrival'].value_counts(dropna=False)
print(f"Values before cleanup:\n{before_cleanup}")

# Replace any value that is not ARRIVAL or DEPARTURE with NULL
df['departureorarrival'] = df['departureorarrival'].apply(
    lambda x: x if x in ['ARRIVAL', 'DEPARTURE'] else None
)

# Count values after replacement
after_cleanup = df['departureorarrival'].value_counts(dropna=False)
print(f"\nValues after cleanup:\n{after_cleanup}")

invalid_departure_count = df['departureorarrival'].isna().sum()
print(f"\nInvalid values replaced with NULL: {invalid_departure_count}")

# ============================================================================
# STEP 4: VALIDATION
# ============================================================================
print("\n" + "=" * 80)
print("STEP 4: VALIDATION")
print("=" * 80)

# Check that no rows were dropped
assert len(df) == 5856, "ERROR: Rows were dropped!"
print(f"✓ All {len(df)} rows retained (no rows dropped)")

# Check operationtime is datetime-compatible
print(f"✓ operationtime dtype: {df['operationtime'].dtype}")
assert pd.api.types.is_datetime64_any_dtype(df['operationtime']), "ERROR: operationtime is not datetime!"

# Check departureorarrival contains only ARRIVAL, DEPARTURE, or NULL
unique_values = df['departureorarrival'].dropna().unique()
print(f"✓ departureorarrival unique values (excluding NULL): {sorted(unique_values)}")
assert all(v in ['ARRIVAL', 'DEPARTURE'] for v in unique_values), "ERROR: Invalid values in departureorarrival!"

# Check consistency
print(f"\n✓ All column values are consistent and standardized")

# ============================================================================
# STEP 5: SAVE CLEANED DATASET
# ============================================================================
print("\n" + "=" * 80)
print("STEP 5: SAVING CLEANED DATASET")
print("=" * 80)

# Save to new CSV file
output_file = DATA_PROCESSED / 'clean_operationtime_departure.csv'
df.to_csv(output_file, index=False)
print(f"✓ Cleaned dataset saved to: {output_file}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)

print(f"\nDataset shape: {df.shape}")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

print(f"\nColumn names:")
for col in df.columns:
    print(f"  - {col}")

print(f"\nData types:")
print(df.dtypes)

print(f"\nNull counts:")
print(df.isnull().sum())

print(f"\nFirst 10 rows of key columns:")
print(df[['operationtime', 'departureorarrival', 'hour', 'weekday', 'month', 'date']].head(10))

print("\n" + "=" * 80)
print("CLEANING COMPLETED SUCCESSFULLY")
print("=" * 80)
