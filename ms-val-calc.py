import pandas as pd
license_vals = {
    "Power BI Pro": 13.07,
    "Office 365 E1": 9.45,
    "Microsoft Power Apps for Developer": 4.67,
    "Power Automate Premium": 13.12,
    "Clipchamp Editor Standard": 2.8,
    "Security E3": 9.89,
    "Microsoft 365 Apps for business": 7.74,
    "Microsoft 365 Business Basic": 5.72,
    "Microsoft 365 Business Premium": 20.53,
    "Microsoft Defender Suite": 11.20,
    "Microsoft Intune Plan 1 Device": 2.52
}
# Read MS User Report CSV
df = pd.read_csv('file_name_here')

# Calculate License Cost
def calculate_license_cost(licenses):
    if pd.isna(licenses):
        return 0

    total = 0

    for license_name in str(licenses).split("+"):
        license_name = license_name.strip()
        total += license_vals.get(license_name, 0)

    return total

# Calculate Cost
df["Totals"] = df["Licenses"].apply(calculate_license_cost)
total_cost = df["Totals"].sum()

# Export results
df.to_excel('Microsoft_Report.xlsx', index=False)

print("Doc Successfully Created!")


