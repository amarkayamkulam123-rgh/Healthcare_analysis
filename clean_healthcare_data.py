"""
Healthcare Dataset Cleaning Script
===================================
Cleans healthcare_dataset.csv and outputs a Power BI-ready CSV.

Issues addressed:
  1. Name casing (random mixed case → Proper Case)
  2. Name prefixes/suffixes (Mr., Dr., Md, Dds, Jr., etc.)
  3. Hospital names (scrambled words, trailing commas)
  4. Billing Amount (rounding, negative values, suspicious lows)
  5. Date columns (parse to proper datetime)
  6. Column data types (enforce correct types)
  7. Whitespace (trim all text columns)
  8. Duplicates (detect and remove)
"""

import pandas as pd
import numpy as np
import re
import os


# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
INPUT_FILE = os.path.join(os.path.dirname(__file__), "healthcare_dataset.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "healthcare_dataset_cleaned.csv")
CLEANING_REPORT_FILE = os.path.join(os.path.dirname(__file__), "cleaning_report.txt")


def load_data(filepath):
    """Load the raw CSV file."""
    print(f"Loading data from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"  Loaded {len(df):,} rows × {len(df.columns)} columns")
    return df


# ──────────────────────────────────────────────
# Step 1: Trim whitespace from all text columns
# ──────────────────────────────────────────────
def trim_whitespace(df):
    """Strip leading/trailing whitespace and collapse internal double spaces."""
    print("\n[Step 1] Trimming whitespace from all text columns...")
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].str.replace(r"\s{2,}", " ", regex=True)  # collapse double spaces
    print(f"  Trimmed {len(text_cols)} text columns")
    return df


# ──────────────────────────────────────────────
# Step 2: Fix Name casing → Proper Case
# ──────────────────────────────────────────────
def fix_name_casing(df):
    """Convert names to Proper Case (Title Case)."""
    print("\n[Step 2] Fixing Name column casing...")
    sample_before = df["Name"].head(5).tolist()
    df["Name"] = df["Name"].str.title()
    sample_after = df["Name"].head(5).tolist()
    for b, a in zip(sample_before, sample_after):
        if b != a:
            print(f"  '{b}' -> '{a}'")
    return df


# ──────────────────────────────────────────────
# Step 3: Remove name prefixes and suffixes
# ──────────────────────────────────────────────
PREFIXES = ["Mr. ", "Mrs. ", "Ms. ", "Dr. ", "Miss "]
SUFFIXES = [" Jr.", " Sr.", " Md", " Phd", " Dds", " Ii", " Iii", " Iv"]


def clean_name_titles(name):
    """Remove titles/prefixes and professional suffixes from a name."""
    if pd.isna(name):
        return name

    cleaned = name.strip()

    # Remove prefixes
    for prefix in PREFIXES:
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix):]
            break  # only one prefix expected

    # Remove suffixes
    for suffix in SUFFIXES:
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
            break  # only one suffix expected

    return cleaned.strip()


def remove_name_titles(df):
    """Apply prefix/suffix removal to the Name column."""
    print("\n[Step 3] Removing name prefixes/suffixes...")

    # Count affected rows
    has_prefix = df["Name"].str.match(
        r"^(Mr\.|Mrs\.|Ms\.|Dr\.|Miss)\s", case=False, na=False
    )
    has_suffix = df["Name"].str.contains(
        r"\s(Jr\.|Sr\.|Md|Phd|Dds|Ii|Iii|Iv)$", case=False, na=False, regex=True
    )
    print(f"  Rows with prefix: {has_prefix.sum():,}")
    print(f"  Rows with suffix: {has_suffix.sum():,}")

    df["Name"] = df["Name"].apply(clean_name_titles)
    return df


# ──────────────────────────────────────────────
# Step 4: Clean Hospital names
# ──────────────────────────────────────────────
def clean_hospital_names(df):
    """Remove stray commas from hospital names and trim."""
    print("\n[Step 4] Cleaning Hospital names...")

    # Count hospitals with commas
    has_comma = df["Hospital"].str.contains(",", na=False)
    print(f"  Hospital names with embedded commas: {has_comma.sum():,}")

    # Remove commas and collapse whitespace
    df["Hospital"] = (
        df["Hospital"]
        .str.replace(",", "", regex=False)
        .str.replace(r"\s{2,}", " ", regex=True)
        .str.strip()
    )

    unique_hospitals = df["Hospital"].nunique()
    print(f"  Unique hospitals after cleaning: {unique_hospitals:,}")
    return df


# ──────────────────────────────────────────────
# Step 5: Fix Billing Amount
# ──────────────────────────────────────────────
def fix_billing_amount(df):
    """Round billing to 2 decimals, flag/fix negatives and suspicious values."""
    print("\n[Step 5] Fixing Billing Amount...")

    # Ensure numeric
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors="coerce")

    # Report issues
    neg_count = (df["Billing Amount"] < 0).sum()
    low_count = ((df["Billing Amount"] >= 0) & (df["Billing Amount"] < 100)).sum()
    null_count = df["Billing Amount"].isna().sum()
    print(f"  Negative values: {neg_count:,}")
    print(f"  Suspiciously low (< $100): {low_count:,}")
    print(f"  Null/invalid values: {null_count:,}")

    # Add a flag column before fixing
    df["Billing_Flag"] = np.where(
        df["Billing Amount"] < 0,
        "Negative",
        np.where(df["Billing Amount"] < 100, "Low", "OK"),
    )

    # Replace negatives with absolute value
    df["Billing Amount"] = df["Billing Amount"].abs()

    # Round to 2 decimal places
    df["Billing Amount"] = df["Billing Amount"].round(2)

    print(f"  Billing range after fix: ${df['Billing Amount'].min():,.2f} – ${df['Billing Amount'].max():,.2f}")
    return df


# ──────────────────────────────────────────────
# Step 6: Parse and validate dates
# ──────────────────────────────────────────────
def fix_dates(df):
    """Parse date columns, add Length of Stay, Year, and Month columns."""
    print("\n[Step 6] Parsing date columns & adding calculated fields...")

    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], errors="coerce")
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], errors="coerce")

    # Report invalid dates
    null_admission = df["Date of Admission"].isna().sum()
    null_discharge = df["Discharge Date"].isna().sum()
    print(f"  Invalid admission dates: {null_admission:,}")
    print(f"  Invalid discharge dates: {null_discharge:,}")

    # Length of Stay (in days)
    df["Length of Stay (Days)"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

    # Flag negative LOS
    neg_los = (df["Length of Stay (Days)"] < 0).sum()
    print(f"  Negative Length of Stay (discharge before admission): {neg_los:,}")

    # Admission Year & Month
    df["Admission Year"] = df["Date of Admission"].dt.year
    df["Admission Month"] = df["Date of Admission"].dt.month_name()

    print(f"  Date range: {df['Date of Admission'].min().date()} to {df['Date of Admission'].max().date()}")
    return df


# ──────────────────────────────────────────────
# Step 7: Enforce correct data types
# ──────────────────────────────────────────────
def enforce_data_types(df):
    """Set explicit data types for each column."""
    print("\n[Step 7] Enforcing column data types...")

    # Age → integer (handle any non-numeric gracefully)
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    invalid_age = ((df["Age"] < 0) | (df["Age"] > 120)).sum()
    print(f"  Out-of-range ages (< 0 or > 120): {invalid_age:,}")
    df["Age"] = df["Age"].astype("Int64")  # nullable integer

    # Room Number → integer
    df["Room Number"] = pd.to_numeric(df["Room Number"], errors="coerce").astype("Int64")

    # Validate categorical columns
    expected_genders = {"Male", "Female"}
    unexpected_genders = set(df["Gender"].dropna().unique()) - expected_genders
    if unexpected_genders:
        print(f"  [!] Unexpected Gender values: {unexpected_genders}")
    else:
        print(f"  Gender values OK: {sorted(expected_genders)}")

    expected_blood = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
    unexpected_blood = set(df["Blood Type"].dropna().unique()) - expected_blood
    if unexpected_blood:
        print(f"  [!] Unexpected Blood Type values: {unexpected_blood}")
    else:
        print(f"  Blood Type values OK: {sorted(expected_blood)}")

    expected_admission = {"Urgent", "Emergency", "Elective"}
    unexpected_admission = set(df["Admission Type"].dropna().unique()) - expected_admission
    if unexpected_admission:
        print(f"  [!] Unexpected Admission Type values: {unexpected_admission}")
    else:
        print(f"  Admission Type values OK: {sorted(expected_admission)}")

    expected_results = {"Normal", "Abnormal", "Inconclusive"}
    unexpected_results = set(df["Test Results"].dropna().unique()) - expected_results
    if unexpected_results:
        print(f"  [!] Unexpected Test Results values: {unexpected_results}")
    else:
        print(f"  Test Results values OK: {sorted(expected_results)}")

    return df


# ──────────────────────────────────────────────
# Step 8: Remove duplicates
# ──────────────────────────────────────────────
def remove_duplicates(df):
    """Remove exact duplicate rows and duplicates by key columns."""
    print("\n[Step 8] Checking for duplicates...")

    # Exact duplicates
    exact_dupes = df.duplicated().sum()
    print(f"  Exact duplicate rows: {exact_dupes:,}")
    if exact_dupes > 0:
        df = df.drop_duplicates()
        print(f"  Removed {exact_dupes:,} exact duplicates")

    # Logical duplicates (same patient + admission date + hospital)
    key_cols = ["Name", "Date of Admission", "Hospital"]
    logical_dupes = df.duplicated(subset=key_cols).sum()
    print(f"  Logical duplicates (Name + Admission Date + Hospital): {logical_dupes:,}")
    if logical_dupes > 0:
        df = df.drop_duplicates(subset=key_cols, keep="first")
        print(f"  Removed {logical_dupes:,} logical duplicates (kept first occurrence)")

    return df


# ──────────────────────────────────────────────
# Generate cleaning report
# ──────────────────────────────────────────────
def generate_report(df_original, df_cleaned, report_path):
    """Write a summary report of all cleaning actions."""
    print(f"\n{'='*55}")
    print("CLEANING SUMMARY")
    print(f"{'='*55}")

    lines = []
    lines.append("=" * 55)
    lines.append("HEALTHCARE DATA CLEANING REPORT")
    lines.append("=" * 55)
    lines.append(f"")
    lines.append(f"Original rows:  {len(df_original):,}")
    lines.append(f"Cleaned rows:   {len(df_cleaned):,}")
    lines.append(f"Rows removed:   {len(df_original) - len(df_cleaned):,}")
    lines.append(f"Original cols:  {len(df_original.columns)}")
    lines.append(f"Cleaned cols:   {len(df_cleaned.columns)} (added: Billing_Flag, Length of Stay, Year, Month)")
    lines.append(f"")
    lines.append("COLUMN SUMMARY:")
    lines.append("-" * 55)
    for col in df_cleaned.columns:
        dtype = df_cleaned[col].dtype
        nulls = df_cleaned[col].isna().sum()
        unique = df_cleaned[col].nunique()
        lines.append(f"  {col:<28} | {str(dtype):<15} | Nulls: {nulls:>5} | Unique: {unique:>6}")

    lines.append("")
    lines.append("SAMPLE DATA (first 5 rows):")
    lines.append("-" * 55)
    lines.append(df_cleaned.head().to_string())

    report_text = "\n".join(lines)
    print(report_text)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"\nReport saved to: {report_path}")


# ──────────────────────────────────────────────
# Main pipeline
# ──────────────────────────────────────────────
def main():
    print("=" * 55)
    print("  HEALTHCARE DATA CLEANING PIPELINE")
    print("=" * 55)

    # Load
    df = load_data(INPUT_FILE)
    df_original = df.copy()

    # Run cleaning steps in order
    df = trim_whitespace(df)       # Step 1
    df = fix_name_casing(df)       # Step 2
    df = remove_name_titles(df)    # Step 3
    df = clean_hospital_names(df)  # Step 4
    df = fix_billing_amount(df)    # Step 5
    df = fix_dates(df)             # Step 6
    df = enforce_data_types(df)    # Step 7
    df = remove_duplicates(df)     # Step 8

    # Reorder columns for a clean output
    column_order = [
        "Name",
        "Age",
        "Gender",
        "Blood Type",
        "Medical Condition",
        "Date of Admission",
        "Discharge Date",
        "Length of Stay (Days)",
        "Admission Year",
        "Admission Month",
        "Doctor",
        "Hospital",
        "Insurance Provider",
        "Billing Amount",
        "Billing_Flag",
        "Room Number",
        "Admission Type",
        "Medication",
        "Test Results",
    ]
    df = df[column_order]

    # Save cleaned data
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n[OK] Cleaned data saved to: {OUTPUT_FILE}")

    # Generate report
    generate_report(df_original, df, CLEANING_REPORT_FILE)

    print(f"\n{'='*55}")
    print("  CLEANING COMPLETE!")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
