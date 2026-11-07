import pandas as pd
import re
from urllib.parse import urlparse

# 1. LOAD THE DATASET (Updated to read directly from the data folder)
df = pd.read_csv("data/research.csv")

print("CLONEGUARD KE - INCIDENT REGISTER AUDIT")
print("=" * 45)

# 2. INSPECT THE DATASET
print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

# 3. CHECK MISSING VALUES
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. CHECK DUPLICATE RECORDS
print("\nDuplicate rows:")
print(df.duplicated().sum())

# 5. CHECK DOMAIN AVAILABILITY
domain_column = "suspicious_domain"

if domain_column in df.columns:
    df["domain_missing"] = df[domain_column].isna()

    print("\nRecords with disclosed domains:")
    print(df[domain_column].notna().sum())

    print("\nRecords without disclosed domains:")
    print(df[domain_column].isna().sum())

# 6. VALIDATE SOURCE URL FORMATS
def valid_url(value):
    if pd.isna(value):
        return False

    try:
        parsed = urlparse(str(value).strip())
        return parsed.scheme in ["http", "https"] and bool(parsed.netloc)
    except Exception:
        return False


if "source_url" in df.columns:
    df["source_url_valid"] = df["source_url"].apply(valid_url)

    print("\nValid source URLs:")
    print(df["source_url_valid"].sum())

    print("\nMissing or invalid source URLs:")
    print((~df["source_url_valid"]).sum())

# 7. EXAMINE INCIDENT TYPES
if "incident_channel" in df.columns:
    print("\nIncident channels:")
    print(df["incident_channel"].value_counts(dropna=False))

# 8. EXAMINE IMPERSONATED ORGANISATIONS
if "organisation_impersonated" in df.columns:
    print("\nOrganisations impersonated:")
    print(
        df["organisation_impersonated"]
        .value_counts(dropna=False)
    )

# 9. CHECK CAMPAIGN GROUPS
if "case_group_id" in df.columns:
    print("\nRecords per campaign group:")
    print(
        df.groupby("case_group_id", dropna=False)
        .size()
        .sort_values(ascending=False)
    )

# 10. IDENTIFY WEBSITE RECORDS
if "incident_channel" in df.columns:
    website_records = df[
        df["incident_channel"]
        .astype(str)
        .str.lower()
        .str.contains("website", na=False)
    ]

    print("\nWebsite-related records:")
    print(len(website_records))

# 11. IDENTIFY POTENTIAL EVALUATION RECORDS
# These are candidates for manual review, NOT confirmed labels.

required_columns = [
    "suspicious_domain",
    "source_url",
    "incident_channel"
]

if all(col in df.columns for col in required_columns):

    candidates = df[
        df["incident_channel"]
        .astype(str)
        .str.lower()
        .str.contains("website", na=False)
        & df["suspicious_domain"].notna()
        & df["source_url"].apply(valid_url)
    ]

    print("\nPotential website evaluation candidates:")
    print(len(candidates))

# 12. EXPORT AUDITED DATASET (Updated to save straight inside your data folder)
df.to_csv("data/cloneguard_incident_audited.csv", index=False)

print("\nAudit completed!")
print("Output saved as data/cloneguard_incident_audited.csv")



